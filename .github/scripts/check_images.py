#!/usr/bin/env python3
"""检查 Markdown 图片引用。

按项目图片规则检查四类违例：
1. 悬空插图 —— .gitbook/assets/ 内的图片未被任何 Markdown 引用；
2. 失效引用 —— 图片引用指向仓库内不存在的文件；
3. 外部链接 —— 图片引用使用外部 URL（插图必须本地化）；
4. 大小写不一致 —— 引用路径与磁盘真实文件名大小写不符（Linux 构建会 404）。

有违例时写出 image-report.md（供 CI 开 issue），无违例时清空该文件。始终以 0 退出。
"""
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ASSETS_DIR = os.path.join(REPO, '.gitbook', 'assets')
REPORT_PATH = os.path.join(REPO, 'image-report.md')
IMG_REF = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
SKIP_DIRS = {'.git', '.gitbook', 'node_modules', 'en', 'script'}


def iter_md_files():
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        for name in sorted(files):
            if name.endswith('.md'):
                yield os.path.join(root, name)


def on_disk_case(path):
    """返回 path 逐段按磁盘真实大小写还原后的路径；任一层不存在则返回 None。"""
    path = os.path.normpath(path)
    prefix = os.path.commonpath([REPO, path])
    rest = os.path.relpath(path, prefix)
    cur = prefix
    for part in rest.split(os.sep):
        try:
            entries = os.listdir(cur)
        except OSError:
            return None
        hit = next((e for e in entries if e == part), None)
        if hit is None:
            return None
        cur = os.path.join(cur, hit)
    return cur


def main():
    external = []      # (md 文件, 引用)
    missing = []       # (md 文件, 引用, 解析路径)
    case_mismatch = [] # (md 文件, 引用, 磁盘真实大小写)
    referenced = set() # 按磁盘真实大小写归一的资产绝对路径

    for md in iter_md_files():
        rel_md = os.path.relpath(md, REPO)
        with open(md, encoding='utf-8', errors='ignore') as f:
            content = f.read()
        for ref in IMG_REF.findall(content):
            ref = ref.strip()
            if not ref or ref.startswith('<'):
                continue
            if re.match(r'^https?://', ref, re.I):
                external.append((rel_md, ref))
                continue
            resolved = os.path.normpath(os.path.join(os.path.dirname(md), ref))
            if not resolved.startswith(REPO):
                missing.append((rel_md, ref, resolved))
                continue
            true_path = on_disk_case(resolved)
            if true_path is None:
                missing.append((rel_md, ref, resolved))
                continue
            if true_path != resolved:
                case_mismatch.append((rel_md, ref, os.path.relpath(true_path, REPO)))
            referenced.add(true_path.lower())

    dangling = []
    if os.path.isdir(ASSETS_DIR):
        for root, _dirs, files in os.walk(ASSETS_DIR):
            for name in sorted(files):
                full = os.path.join(root, name)
                if full.lower() not in referenced:
                    dangling.append(os.path.relpath(full, REPO))

    issues = bool(external or missing or case_mismatch or dangling)
    if issues:
        lines = ['# 图片检查报告', '']
        if dangling:
            lines.append('## 悬空插图（未被任何 Markdown 引用）')
            lines += ['- %s' % p for p in dangling] + ['']
        if missing:
            lines.append('## 失效引用（指向不存在的文件）')
            lines += ['- `%s`，引用于 %s' % (ref, md) for md, ref, _ in missing] + ['']
        if external:
            lines.append('## 外部链接（插图必须本地化）')
            lines += ['- `%s`，引用于 %s' % (ref, md) for md, ref in external] + ['']
        if case_mismatch:
            lines.append('## 大小写不一致（与磁盘真实文件名不符）')
            lines += ['- `%s`，引用于 %s，磁盘为 `%s`' % (ref, md, true)
                      for md, ref, true in case_mismatch] + ['']
        with open(REPORT_PATH, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(lines))
    elif os.path.exists(REPORT_PATH):
        os.remove(REPORT_PATH)

    print('悬空插图 %d，失效引用 %d，外部链接 %d，大小写不一致 %d'
          % (len(dangling), len(missing), len(external), len(case_mismatch)))
    return 0


if __name__ == '__main__':
    sys_exit = main()
    raise SystemExit(sys_exit)

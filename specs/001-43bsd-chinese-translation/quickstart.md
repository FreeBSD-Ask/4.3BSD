# Quickstart: 端到端验证指南

证明"从 PDF 到可检查的中文页面"整条管线可用的最小验证场景。前置条件：Windows + `py`（Python ≥3.14）+ pymupdf；`2.pdf` 在仓库根；`markdownlint-cli2` 已全局安装。

## 场景 A：原文管线（渲染 → 视觉转录）

```sh
py script/render_pages.py vii xii     # 渲染前言（印刷页 vii–xii）
py script/render_pages.py 26 40 300   # 代码页用 300 DPI
```

然后派 1–2 路 general-purpose 子代理按 `contracts/en-transcription.md` 转录 `script/pages/` 指定区间到 `en/01-preface.txt`。

**预期**: `en/01-preface.txt` 存在；`[[PAGE vii]]`…`[[PAGE xii]]`（或对应数字页码）齐全单调；`grep -c UNCLEAR` 为 0 或全部有裁决注记；抽 1 页与 PNG 对读一致。

## 场景 B：翻译一节并过检查

以前言或第 1 章任一节为例：

1. 按 `AGENTS.md` 规范从 `en/` 译出对应 `.md`（H1 与 `SUMMARY.md` 一致）。
2. 运行：

   ```sh
   py script/check_quotes.py <文件>
   py script/check_bold.py <文件>
   markdownlint-cli2 "<文件>" --config .github/.markdownlint.json
   ```

**预期**: 三项违例均为 0。

## 场景 C：结构对账

```sh
py script/compare_structure.py
```

**预期**: `SUMMARY.md` 章节树与原书目录差异为 0（骨架阶段：全树就位即可，正文可为空占位但文件必须存在）。

## 场景 D：插图引用闭环

```sh
py script/extract_figures.py   # 甄别并导出插图到 .gitbook/assets/
```

任取一图，在对应页面以 `![图注](../.gitbook/assets/fig-...png)` 引用后运行 check-images（本地或 CI）。

**预期**: 引用可解析、大小写与磁盘一致、无悬空资产。

## 场景 E：CI 预演

推送前本地全量：`check_quotes.py`、`check_bold.py`、markdownlint-cli2 全目录、`compare_structure.py`。

**预期**: 全部 0 违例/0 差异；推送后 GitHub Actions 十个工作流全绿。

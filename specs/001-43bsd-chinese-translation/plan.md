# Implementation Plan: 《4.3BSD UNIX 操作系统的设计与实现》简体中文 GitBook 翻译项目

**Branch**: `001-43bsd-chinese-translation` | **Date**: 2026-10-24 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-43bsd-chinese-translation/spec.md`

## Summary

把仓库根目录的 `2.pdf`（《The Design and Implementation of the 4.3BSD UNIX Operating System》，Addison-Wesley 1989，496 页扫描件）完整翻译为简体中文 GitBook 项目：前言 + 5 部分 13 章（每节一页）+ 词汇表附录 + 中文术语索引。核心路线：**完全不信任 PDF 内嵌 OCR 文本层**——先把页面渲染成高分辨率图像，由 1–2 路并行子代理视觉转录生成权威英文原文（`en/`），再按逐句对照工作流翻译、三轮校对加复查；治理上先改写 `AGENTS.md`、建立全局术语表（不少于 150 条，高风险术语联网核查）与进度文件，全部提交 `main`。

## Technical Context

**Language/Version**: 内容产物为 Markdown（GitBook 方言，无 HTML）；本地工具脚本 Python 3.15（`py`）+ pymupdf；CI 为 GitHub Actions（既有工作流，PowerShell 无关）。

**Primary Dependencies**: GitBook（`SUMMARY.md` 驱动导航）；`.github/workflows/` 既有 10 个工作流（sync-headers、mulu、file-name-check、markdownlint2、md-padding、AutoCorrect、check-images、links、create-pdf、Auto-Assign）；pymupdf（页面渲染与插图提取，本地）；markdownlint-cli2（本地已装）；ZCode general-purpose 子代理（读页面图像做视觉转录，1–2 路并行）。

**Storage**: Git 仓库纯文件（Markdown + PNG 资产）；无数据库。`en/`、`script/`、`2.pdf`、页面渲染图均在 `.gitignore` 外围排除。

**Testing**: `script/check_quotes.py`（引号）、`script/check_bold.py`（加粗空格）、markdownlint-cli2（`.github/.markdownlint.json`）、`script/compare_structure.py`（中英结构对比差异为 0）、CI 全套。

**Target Platform**: GitBook/GitHub Markdown 渲染；文件名须兼容 Windows（无空格、无中文、无英文冒号、大小写敏感引用）。

**Project Type**: documentation-translation（文档翻译工程，非软件）。

**Performance Goals**: 质量目标取代性能目标——全部检查违例为 0；转录 `[UNCLEAR]` 标记人工清零后才可进入翻译。

**Constraints**: ①扫描件仅页面图像可信，OCR 文本层不得作为内容来源（用户 2026-10-24 裁定）；②子代理并行度 1–2 路；③渲染分辨率正文 ≥200 DPI、代码页 ≥300 DPI；④直接提交 `main`，不 push。

**Scale/Scope**: 496 PDF 页（印刷页 1–480 + 前置页）；13 章约 90 个节页面；词汇表约 38 印刷页；索引约 45 印刷页；插图数百幅（嵌入图像 898 个，需甄别去重）。

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

`.specify/memory/constitution.md` 为初始化占位模板（未配置任何原则），无门禁约束——本计划按仓库既有 `AGENTS.md` 治理文化执行（高频中文提交、CI 为准、进度文件强制更新）。**Gate: PASS（无宪法约束）**。

## Project Structure

### Documentation (this feature)

```text
specs/001-43bsd-chinese-translation/
├── spec.md              # 规格（$speckit-specify 产物）
├── plan.md              # 本文件
├── research.md          # Phase 0 决策记录
├── data-model.md        # Phase 1 数据模型
├── quickstart.md        # Phase 1 验证指南
├── contracts/           # Phase 1 格式契约
│   ├── en-transcription.md
│   ├── summary-and-pages.md
│   ├── terminology-table.md
│   └── progress-files.md
├── checklists/
│   └── requirements.md  # 规格质量清单
└── tasks.md             # $speckit-tasks 产物
```

### Source Code (repository root)

```text
./
├── AGENTS.md                     # 项目治理（本计划改写适配）
├── README.md                     # GitBook 首页/项目说明
├── SUMMARY.md                    # 全书目录唯一数据源（首行 # Table of contents）
├── mu-lu.md                      # CI 自动生成，禁止手改
├── yi-zhe-shuo-ming.md           # 全局术语表（译者说明）
├── CHANGELOG.md                  # 翻译里程碑日志
├── PROJECT-PROGRESS.md           # 当前任务/轮次/下一步（会话接手必读）
├── qian-yan/                     # 前言（献词、序）
│   ├── xian-ci.md
│   └── xu-yan.md
├── di-yi-bu-fen-gai-lan/         # 第一部分 概览
│   ├── 1.-li-shi-yu-mu-biao.md
│   ├── 1.1.-unix-xi-tong-de-li-shi.md
│   ├── ... (每节一页)
│   ├── 2.-4.3bsd-she-ji-zong-lan.md
│   ├── ... 
│   └── 3.-nei-he-fu-wu.md ...
├── di-er-bu-fen-jin-cheng/       # 第二部分 进程（第 4–5 章）
├── di-san-bu-fen-shu-ru-shu-chu-xi-tong/  # 第三部分 I/O 系统（第 6–9 章）
├── di-si-bu-fen-jin-cheng-jian-tong-xin/   # 第四部分 进程间通信（第 10–12 章）
├── di-wu-bu-fen-xi-tong-yun-xing/          # 第五部分 系统运行（第 13 章）
├── fu-lu/                        # 附录
│   ├── ci-hui-biao.md            # Glossary 全文翻译
│   └── shu-yu-suo-yin.md         # 中文术语索引（拼音排序）
├── .gitbook/assets/              # 从 PDF 提取的插图
├── .github/                      # 既有 CI（不新增冲突规则）
├── en/                           # [本地不入库] 子代理视觉转录的英文原文
└── script/                       # [本地不入库] 渲染/检查/对比脚本
    └── pages/                    # [本地不入库] 渲染出的页面 PNG
```

**Structure Decision**: 沿用 FreeBSD 中文社区 GitBook 项目布局（`SUMMARY.md` 唯一数据源、拼音 slug 文件名、分部目录、`.gitbook/assets` 插图），因为 CI 工作流（sync-headers/mulu/file-name-check 等）按此约定运作；`en/`、`script/` 不入库以保持仓库即成品的性质。

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

无宪法违例，不适用。

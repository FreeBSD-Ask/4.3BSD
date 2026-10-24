---
description: "Task list for 《4.3BSD UNIX 操作系统的设计与实现》中文 GitBook 翻译项目"
---

# Tasks: 《4.3BSD UNIX 操作系统的设计与实现》简体中文 GitBook 翻译

**Input**: Design documents from `/specs/001-43bsd-chinese-translation/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: 本项目无单元测试；验收以 `contracts/` 各契约的判定项 + `quickstart.md` 场景代替。

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

* **[P]**: Can run in parallel (different files, no dependencies)
* **[Story]**: Which user story this task belongs to (e.g. US1, US2, US3)
* Include exact file paths in descriptions

## Path Conventions

* 仓库根：`AGENTS.md`、`README.md`、`SUMMARY.md`、`yi-zhe-shuo-ming.md`、`PROJECT-PROGRESS.md`、`CHANGELOG.md`
* 分部目录：`qian-yan/`、`di-yi-bu-fen-gai-lan/`、`di-er-bu-fen-jin-cheng/`、`di-san-bu-fen-shu-ru-shu-chu-xi-tong/`、`di-si-bu-fen-jin-cheng-jian-tong-xin/`、`di-wu-bu-fen-xi-tong-yun-xing/`、`fu-lu/`
* 本地不入库：`script/`（脚本与页面渲染图 `script/pages/`）、`en/`、`2.pdf`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: 仓库基础与入库范围整理

* [ ] T001 更新 `.gitignore`：确保包含 `en/`、`script/pages/`、`*.pdf`（2.pdf 本体不入库），保留既有条目
* [ ] T002 [P] 改写 `README.md` 为 GitBook 首页：书名《4.3BSD UNIX 操作系统的设计与实现》（括注英文原名）、四位作者、原书简介（据 PDF 第 2–13 页视觉转录内容撰写）、项目链接
* [ ] T003 提交基础设施：`.github/`、`.autocorrectrc`、`.gitattributes`、`.specify/`、`.zcode/`、`specs/001-43bsd-chinese-translation/` 全部入库（提交信息注明"项目治理与 CI 基础设施"）

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: 治理文件、工具链、全书骨架——未完成前不得开始任何故事

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

* [ ] T010 完整改写 `AGENTS.md` 适配本项目（FR-001 全部判定项）：书名、2.pdf（496 页扫描件、ClearScan OCR 完全不信任）、结构（前言 + 5 部分 13 章 + 词汇表 413–450 + 索引 451–496）、1–2 路子代理视觉转录工作流、检查命令、进度文件制度；不得残留《Life With UNIX》专属内容
* [ ] T011 [P] 编写 `script/render_pages.py`：参数＝印刷页起止 + DPI（默认 200，代码页 300）；内置印刷页↔PDF 页偏移（印刷 1 = PDF 24，即 PDF = 印刷 + 23；前置罗马页 vii–xxii = PDF 8–23）；输出 `script/pages/pNNNN.png`
* [ ] T012 [P] 编写 `script/check_quotes.py`（引号检查：成对弯引号、方向、直引号/直角引号/半角引号排查，代码块与行内代码豁免——实现参照 `AGENTS.md` 引号规范全部条款）
* [ ] T013 [P] 编写 `script/check_bold.py`（加粗两侧恰好一个半角空格检查，代码块与行内代码豁免）
* [ ] T014 [P] 编写 `script/compare_structure.py`（对比 `en/` 目录结构与 `SUMMARY.md` 章节树，输出差异清单）
* [ ] T015 编写 `script/extract_figures.py`：提取 PDF 嵌入图像，按尺寸/位置甄别正文插图，导出 `.gitbook/assets/fig-<章>-<序号>-<slug>.png` 并生成页码→文件对照表 `script/figures-map.md`
* [ ] T016 创建 `SUMMARY.md` 全书骨架 + 各页面占位文件（每页仅 H1，与条目逐字一致）：`qian-yan/`（献词、前言）、五个分部、13 章每章的章首页与每节一页（节号 X.Y 全集以原书目录为准）、`fu-lu/ci-hui-biao.md`、`fu-lu/shu-yu-suo-yin.md`；首行 `# Table of contents`；完成后运行 `py script/compare_structure.py` 确认差异为 0
* [ ] T017 [P] 渲染词汇表页（印刷 413–450）与前置页（vii–xii、目录 xiii–xxii）：`py script/render_pages.py`
* [ ] T018 派 1–2 路子代理视觉转录词汇表 → `en/15-glossary.txt`（契约 `contracts/en-transcription.md`：`[[PAGE n]]` 单调、`[UNCLEAR]` 清零或裁决、词条按原字母序）
* [ ] T019 创建 `PROJECT-PROGRESS.md`（当前任务/下一步/轮次记录空表）与 `CHANGELOG.md`（首条记录"项目启动"）

**Checkpoint**: 骨架就位、工具链可运行、词汇表底稿可用——各故事可开始

---

## Phase 3: User Story 2 - 贡献者按治理文件无缝接手 (Priority: P1)

**Goal**: `AGENTS.md` + 全局术语表 + 进度文件构成自洽治理体系，任何新会话可直接接手

**Independent Test**: `AGENTS.md` 检索书名/2.pdf/496/结构描述全部与实际一致且无 Life With UNIX 残留；`yi-zhe-shuo-ming.md` ≥150 条；`PROJECT-PROGRESS.md` 可复述当前状态

### Implementation for User Story 2

* [ ] T020 [US2] 创建 `yi-zhe-shuo-ming.md` 骨架（按 `contracts/terminology-table.md` 六段结构）
* [ ] T021 [US2] 从 `en/15-glossary.txt` 词头提取术语清单，拟定初版译名（参照系优先级见 research.md R-5）
* [ ] T022 [US2] 术语总表扩充至 ≥150 条（覆盖词汇表主干 + 各章标题高频术语）
* [ ] T023 [US2] 联网核查 ≥10 个高风险术语（kluster、silly-window syndrome、scatter/gather、C-list、line discipline、core map、swap space、mbuf、socket、daemon 等），备注留来源链接（FR-003）
* [ ] T024 [P] [US2] 编制人名表（四位作者 + 原书致谢/正文中出现者，一律不音译）入 `yi-zhe-shuo-ming.md`
* [ ] T025 [P] [US2] 编制公司/机构表（有通行中译者用中译，无者英文）与书名/文献表（有中译本者中文译名+括注英文）入 `yi-zhe-shuo-ming.md`
* [ ] T026 [US2] 自检 FR-001：全文检索 "LifeWithUNIX/Life With UNIX/mu-lu 模板残留/372 页" 等痕迹为 0；提交（"AGENTS.md 适配与全局术语表初版"）

**Checkpoint**: 治理体系闭环，翻译工作可以开始

---

## Phase 4: User Story 4 - 扫描件内容保真提取 (Priority: P2)

**Goal**: 全书英文底稿 `en/` 由 1–2 路子代理视觉转录完成，插图资产导出并建立对照

**Independent Test**: 抽 3 页转录文本与 PNG 逐词一致；`[UNCLEAR]` 清零；`.gitbook/assets/` 图与 `[FIGURE]` 标记一一对应

### Implementation for User Story 4

* [ ] T030 [P] [US4] 渲染全书正文页（印刷 1–412，代码密集章第 8/13 章用 300 DPI）
* [ ] T031 [US4] 视觉转录前言（vii–xii + 献词 + 系列页说明取舍）→ `en/01-preface.txt`
* [ ] T032 [P] [US4] 视觉转录第 1 章（3–17）→ `en/02-ch01-history-and-goals.txt`
* [ ] T033 [P] [US4] 视觉转录第 2 章（19–41）→ `en/03-ch02-design-overview.txt`
* [ ] T034 [P] [US4] 视觉转录第 3 章（43–67）→ `en/04-ch03-kernel-services.txt`
* [ ] T035 [P] [US4] 视觉转录第 4 章（69–107）→ `en/05-ch04-process-management.txt`
* [ ] T036 [P] [US4] 视觉转录第 5 章（109–165）→ `en/06-ch05-memory-management.txt`
* [ ] T037 [P] [US4] 视觉转录第 6 章（167–185）→ `en/07-ch06-io-overview.txt`
* [ ] T038 [P] [US4] 视觉转录第 7 章（187–223）→ `en/08-ch07-filesystem.txt`
* [ ] T039 [P] [US4] 视觉转录第 8 章（225–257）→ `en/09-ch08-device-drivers.txt`
* [ ] T040 [P] [US4] 视觉转录第 9 章（259–277）→ `en/10-ch09-terminal-handling.txt`
* [ ] T041 [P] [US4] 视觉转录第 10 章（279–309）→ `en/11-ch10-ipc.txt`
* [ ] T042 [P] [US4] 视觉转录第 11 章（311–341）→ `en/12-ch11-network-communication.txt`
* [ ] T043 [P] [US4] 视觉转录第 12 章（343–389）→ `en/13-ch12-network-protocols.txt`
* [ ] T044 [P] [US4] 视觉转录第 13 章（391–411）→ `en/14-ch13-system-startup.txt`
* [ ] T045 [US4] 视觉转录索引页（451–496）词条骨架 → `en/16-index.txt`（供 US5 使用，不直接成页）
* [ ] T046 [US4] 运行 `py script/extract_figures.py` 导出全部插图；按 `[FIGURE]` 标记核对 `script/figures-map.md` 页码对应；粘连/碎图逐个裁决
* [ ] T047 [US4] 转录抽检：随机 3 页与 PNG 逐词比对（含脚注与标点）；`[UNCLEAR]` 逐条裁决清零

**Checkpoint**: `en/` 16 个文件齐备可信，插图资产就位——翻译底稿锁定

---

## Phase 5: User Story 1 - 读者在线阅读完整中文译本 (Priority: P1) 🎯

**Goal**: 前言 + 13 章 + 词汇表附录全部译出，每节一页、图表代码习题参考文献齐全

**Independent Test**: `SUMMARY.md` 每个条目对应页面非空；任一页面 H1 与条目一致；原书各元素（图/表/习题/文献）在对应页面可找到

**注**: 本故事按分部推进；每节翻译流程：读 `en/` 对应段 → 逐句翻译（`AGENTS.md` 语言质量标准）→ 新术语先录 `yi-zhe-shuo-ming.md` → 插图引用（`../.gitbook/assets/…`，大小写与磁盘一致）→ 本地三项检查 0 违例 → 提交

### Implementation for User Story 1

* [ ] T050 [US1] 译前言与献词：`qian-yan/xian-ci.md`、`qian-yan/xu-yan.md`（版权/商标页保留原文不译，在 README 说明）
* [ ] T051 [US1] 译第一部分（第 1–3 章）：`di-yi-bu-fen-gai-lan/` 下全部页面（3 个章首页 + 1.1–1.4、2.1–2.13、3.1–3.9 各节页）
* [ ] T052 [US1] 译第二部分（第 4–5 章）：`di-er-bu-fen-jin-cheng/`（2 个章首页 + 4.1–4.8、5.1–5.13 各节页；代码清单以页面图像逐字符核对）
* [ ] T053 [US1] 译第三部分（第 6–9 章）：`di-san-bu-fen-shu-ru-shu-chu-xi-tong/`（4 个章首页 + 6.1–6.2、7.1–7.8、8.1–8.7、9.1–9.10 各节页）
* [ ] T054 [US1] 译第四部分（第 10–12 章）：`di-si-bu-fen-jin-cheng-jian-tong-xin/`（3 个章首页 + 10.1–10.7、11.1–11.8、12.1–12.11 各节页）
* [ ] T055 [US1] 译第五部分（第 13 章）：`di-wu-bu-fen-xi-tong-yun-xing/`（1 个章首页 + 13.1–13.5 各节页）
* [ ] T056 [US1] 译词汇表附录：`fu-lu/ci-hui-biao.md`（`en/15-glossary.txt` 全部词条，按原字母序，附编排译注；与 `yi-zhe-shuo-ming.md` 译名相互校准，冲突以校准结果双向更新）
* [ ] T057 [US1] 全书交叉引用清理：正文 "see page N/see Chapter X" 全部改写为语义化描述或相对链接（`AGENTS.md` 禁止硬编码章引用条款）

**Checkpoint**: 全书初译完成，GitBook 可整本阅读

---

## Phase 6: User Story 3 - 译文忠实、地道且保留历史视角 (Priority: P2)

**Goal**: 已译内容按"三轮逐句校对 + 一轮复查"递归流程全部过审

**Independent Test**: 任一章节抽 20 句对照 `en/` 无漏译无错译；语言问题类别表逐项过；1989 视角未被改写；每轮记录在 `PROJECT-PROGRESS.md`

### Implementation for User Story 3

* [ ] T060 [US3] 前言轮次：三轮逐句校对 + 一轮复查（递归直至无问题），每轮更新 `PROJECT-PROGRESS.md` 并提交
* [ ] T061 [P] [US3] 第一部分轮次（第 1–3 章）
* [ ] T062 [P] [US3] 第二部分轮次（第 4–5 章）
* [ ] T063 [P] [US3] 第三部分轮次（第 6–9 章）
* [ ] T064 [P] [US3] 第四部分轮次（第 10–12 章）
* [ ] T065 [P] [US3] 第五部分轮次（第 13 章）
* [ ] T066 [US3] 词汇表附录轮次（重点：与全书正文译名一致性双向核对）

**Checkpoint**: 全书过审；`PROJECT-PROGRESS.md` 轮次表与 git 历史可对账

---

## Phase 7: User Story 5 - 中文术语索引 (Priority: P3)

**Goal**: `fu-lu/shu-yu-suo-yin.md` 成页：中文词条 + 英文原词、拼音排序、链接全部可解析

**Independent Test**: 每词条 ≥1 个链接指向存在页面；links 检查 0 死链；排序无乱序段

### Implementation for User Story 5

* [ ] T070 [US5] 以 `en/16-index.txt` 词条 ∪ 词汇表词条 ∪ 正文高频术语并集建词条清单，逐条定中文译名（与 `yi-zhe-shuo-ming.md` 一致）
* [ ] T071 [US5] 为每词条确定指向章节页面的链接集合；重建原索引 see/see also 关系
* [ ] T072 [US5] 生成 `fu-lu/shu-yu-suo-yin.md`（拼音排序，附编排方式译注）并跑链接检查

---

## Phase 8: Polish & Cross-Cutting Concerns (User Story 6)

**Purpose**: 全书门禁与收尾

* [ ] T080 [P] [US6] 全量本地检查：`py script/check_quotes.py`、`py script/check_bold.py`、markdownlint-cli2（排除 `en/`、`script/`、`node_modules/`）——三项 0 违例
* [ ] T081 [US6] `py script/compare_structure.py` 差异为 0；`SUMMARY.md` 条目↔文件↔H1 三方一致
* [ ] T082 [P] [US6] 图片闭环：`.gitbook/assets/` 无悬空文件、引用 100% 可解析且大小写一致
* [ ] T083 [US6] 术语表终检：抽查 30 条零冲突；`yi-zhe-shuo-ming.md` 与 `fu-lu/ci-hui-biao.md` 译名一致
* [ ] T084 [US6] `PROJECT-PROGRESS.md` 与 `CHANGELOG.md` 收口；README 项目状态更新
* [ ] T085 [US6] 运行 `quickstart.md` 全部场景 A–E 通过；向用户汇报并等待是否 push

---

## Dependencies & Execution Order

### Phase Dependencies

* **Setup (Phase 1)**: 无依赖，立即开始
* **Foundational (Phase 2)**: 依赖 Phase 1；**阻塞全部故事**（AGENTS.md、骨架、脚本、词汇表底稿皆在此）
* **US2 (Phase 3)**: 依赖 T018（词汇表转录）
* **US4 (Phase 4)**: 依赖 T011/T015（渲染与插图脚本）；转录任务间互相独立
* **US1 (Phase 5)**: 逐分部依赖对应转录任务（T051←T032–T034；T052←T035–T036；……）；T056←T018
* **US3 (Phase 6)**: 逐分部依赖对应翻译任务；校对期间冻结该分部底稿
* **US5 (Phase 7)**: 依赖 T045 与 Phase 5/6 大体完成（词条来源需要全书译名稳定）
* **Polish (Phase 8)**: 依赖全部故事完成

### User Story Dependencies

* **US2 (P1)**: Foundational 后即可开始（实际在本会话优先完成——它是用户点名的交付物）
* **US4 (P2)**: 与 US2 并行度高，但每章转录完成才解锁该章翻译
* **US1 (P1)**: 逐分部跟进 US4；MVP = Phase 1+2 + US2 + T031/T032 + T050 + 第 1 章翻译
* **US3 (P2)**: 跟随 US1 逐分部滚动
* **US5/US6 (P3)**: 收尾

### Parallel Opportunities

* Phase 2 的 T011–T015 五个脚本任务互不依赖，可并行
* Phase 4 的 T032–T045 各章转录互相独立：**按用户裁定以 1–2 路子代理并行**（同一时刻最多 2 路在飞）
* Phase 6 的 T061–T065 五个分部校对互相独立（如有多会话能力可并行）
* Phase 8 的 T080/T082/T083 可并行

## Parallel Example: Phase 4 transcription

```text
同时派发（2 路上限）：
Worker A: "视觉转录第 1 章 → en/02-ch01-history-and-goals.txt"
Worker B: "视觉转录第 2 章 → en/03-ch02-design-overview.txt"
# 每路完成后按顺序取下一章，直至 T045
```

---

## Implementation Strategy

### MVP First

1. Phase 1 + Phase 2 全部
2. US2（治理闭环：AGENTS.md + 术语表 ≥150 条）
3. T030/T031/T032 + T050 + 第 1 章翻译
4. **STOP and VALIDATE**: `quickstart.md` 场景 A/B/C 通过；GitBook 中前言与第 1 章可读

### Incremental Delivery

1. 基础设施 + 治理 → 2. 前言 + 第一部分（译 + 校） → 3. 第二部分 → 4. 第三部分 → 5. 第四部分 → 6. 第五部分 → 7. 词汇表附录 → 8. 术语索引 → 9. 全量门禁

### Session Strategy（多会话）

每个会话：读 `PROJECT-PROGRESS.md` → 领取下一个未完成单元（转录/翻译/校对）→ 完成后提交并更新进度 → 会话结束前更新 `PROJECT-PROGRESS.md`。

---

## Notes

* [P] tasks = different files, no dependencies
* 转录/翻译/校对均遵守"禁止批量机械替换、逐句逐个手动修改"总则
* 每完成一个任务或逻辑组即以中文一行提交信息提交到 main；不 push
* 所有判定以 CI（`.github/workflows/`）为最终标准，本地检查是预演

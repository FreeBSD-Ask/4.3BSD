# Phase 0 Research: 决策记录

**日期**: 2026-10-24
**输入**: spec.md Technical Context 的未知项与用户两条裁定（2026-10-24：书名/索引/词汇表；OCR 完全不信任、1–2 路子代理视觉转录）。

## R-1 原文获取：OCR 文本层完全弃用，改为页面图像视觉转录

* **Decision**: `en/` 原文一律由子代理读取渲染后的页面 PNG 视觉转录生成；PDF 内嵌 ClearScan OCR 文本层仅允许用于页码定位与结构普查，禁止进入任何译文。
* **Rationale**: 用户明确裁定"完全不信任 OCR 文本层"。实测 OCR 层有系统性错误（`I/O`→`1/0`、`Inode`→`!node`、`45`→`4S`、`Terminal`→`Terrninal`、`so`→`50`），且代码清单与数字最易错——恰是本书最不能错的内容。
* **Alternatives considered**: ①沿用 OCR 层 + 人工抽查（Life With UNIX 模板做法，因那本是文本型 PDF）——被用户裁定否决；②重OCR（本地引擎）——仍属 OCR，未被信任背书，且无优于视觉转录之处。

## R-2 视觉转录执行形态：1–2 路并行子代理

* **Decision**: 每次转录任务按章（或章内分段）切给 general-purpose 子代理；主会话同一时刻最多派发 2 路并行，每路内部顺序处理自己的页区间。转录协议见 `contracts/en-transcription.md`（`[[PAGE n]]` 印刷页码、`[FIGURE ...]`、`[TABLE ...]`、`[UNCLEAR]` 标记）。
* **Rationale**: 用户指定"使用 1-2 路子代理处理 ocr"。2 路并行已可平衡吞吐与主会话上下文开销；每子代理只回报摘要与 `[UNCLEAR]` 清单，不回传全文（全文由子代理直接写入 `en/`）。
* **Alternatives considered**: ①单路串行——更稳但吞吐减半，用户明言"不计成本代价"，故取 2 路；②3 路以上——超出用户给定上限，且页面渲染与校对将成为瓶颈，无收益。

## R-3 页码体系：印刷页码为唯一基准

* **Decision**: 渲染脚本计算偏移（印刷第 1 页 = PDF 第 24 页，即 PDF = 印刷 + 23；锚点实测：印刷 3 = PDF 26 第 1 章起始、印刷 413 = PDF 436 词汇表、印刷 451 = PDF 474 索引；前置罗马页 vii–xxii = PDF 8–23），所有 `[[PAGE n]]`、图注、交叉引用一律使用印刷页码。
* **Rationale**: 原书交叉引用与索引都基于印刷页码；PDF 页码是扫描产物，对读者无意义。
* **Alternatives considered**: 用 PDF 物理页号——与原书页码脱节，读者无法回溯纸质书，弃用。

## R-4 章节切分与文件粒度

* **Decision**: 完全沿用社区 GitBook 约定：每章一个章首页 `X.-slug.md` + 每节 `X.Y.-slug.md`；节内子节 H2/H3 不拆页。分部目录按拼音命名。全书预计约 100 个页面文件。
* **Rationale**: CI（sync-headers、file-name-check）与既有 AGENTS.md 规范均按此约定设计；每节一页的粒度便于高频提交与逐节校对记账。
* **Alternatives considered**: 每章一页——页面过长（第 5 章 55 印刷页），GitBook 阅读体验差，弃用。

## R-5 术语体系来源与冲突处理

* **Decision**: 术语表初版以原书 Glossary（印刷 413–450）词条为骨架，译名参照系依优先级：①《4.4BSD 操作系统的设计与实现》官方中译本（中国电力出版社）既有译法；②TCP/IP 与操作系统经典教材通行译法（谢希仁《计算机网络》、Silberschatz《操作系统概念》中译本等）；③FreeBSD 中文社区既有项目译法。三者冲突时取①；均无先例且无把握者保留英文并备注待议。高风险术语逐一联网核查。
* **Rationale**: 本书与 4.4BSD 版是同一作者的姊妹篇，内核术语高度重叠，沿用官方中译本译法可让两书中文版术语互通；教材通行译法保证读者熟悉度。
* **Alternatives considered**: 全部自创译名——破坏与姊妹篇及教材的术语互通，弃用。

## R-6 插图处理

* **Decision**: 用 pymupdf 提取 PDF 嵌入图像（898 个，含页面装饰性碎片），按尺寸与所在页甄别为"正文插图"后导出到 `.gitbook/assets/`，命名 `fig-<章>-<序号>-<slug>.png`；由视觉转录的 `[FIGURE p.nnn ...]` 标记建立页→图对应。原图不做任何修饰。
* **Rationale**: ClearScan 扫描页里插图保留为位图，直接提取保真度最高；重绘违反"禁止篡改"。
* **Alternatives considered**: 整页截图裁剪——插图边缘与正文粘连，提取嵌入图像更干净；混合方案（小图截页、大图提取）——增加规则复杂度，先统一提取，确有粘连再逐个裁决。

## R-7 Index（索引）转译方案

* **Decision**: 不做逐词条 1:1 硬译（原索引含大量页码交叉与子词条，机械翻译会产出大量死页码）。做法：全书译完后，以原书 Index 词条 + 原书 Glossary 词条 + 全书正文高频术语并集生成中文术语索引，按拼音排序，每词条保留英文原词并链接到对应中文页面；原索引的"见/参见"（see/see also）关系在中文词条间重建。
* **Rationale**: 用户选择"翻译为中文术语索引"，其价值在检索与导航而非页码复刻；链接指向中文页面才能真正可用。
* **Alternatives considered**: ①逐词条照搬英文+页码——GitBook 中页码失效，弃用；②完全不做——用户已否决。

## R-8 治理与提交策略

* **Decision**: 本特性（项目引导）一次性完成：改写 AGENTS.md → 建术语表 → 渲染/转录管线 → SUMMARY 骨架 → PROJECT-PROGRESS/CHANGELOG，随后按章推进翻译，每章提交至少一次；`specs/`、`.specify/`、`.zcode/`、`.github/`、`.autocorrectrc` 随首次基础设施提交入库。
* **Rationale**: AGENTS.md 的提交策略条款要求高频提交；治理文件入库使任何新会话/协作者可复现流程。
* **Alternatives considered**: 治理文件也不入库——违反社区项目惯例与 AGENTS.md 自身要求，弃用。

# Feature Specification: 《4.3BSD UNIX 操作系统的设计与实现》简体中文 GitBook 翻译项目

**Feature Branch**: `001-43bsd-chinese-translation`

**Created**: 2026-10-24

**Status**: Draft

**Input**: User description: "把 2.pdf 翻译为简体中文的 gitbook 项目。先使得 AGENTS.md 适配本项目，并严格落实。要求建立全局术语表。不计成本代价。有问题问我，术语不清楚的联网查询。"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - 读者在线阅读完整中文译本 (Priority: P1)

中文读者打开本项目生成的 GitBook，按原书结构（前言、五个部分共 13 章、词汇表附录、中文术语索引）逐页阅读《4.3BSD UNIX 操作系统的设计与实现》（The Design and Implementation of the 4.3BSD UNIX Operating System，Leffler、McKusick、Karels、Quarterman 著，Addison-Wesley 1989）的简体中文译文；导航树完整，无缺章缺节，插图、表格、代码、习题、参考文献齐全。

**Why this priority**: 全书完整可读是本项目存在的根本目的，其余一切故事都服务于它。

**Independent Test**: 逐条核对 `SUMMARY.md` 导航树与原书目录（印刷页 xiii–xxii）：前言（vii–xii）、第 1–13 章、词汇表（413–450）、索引（451–496）各单元均有对应中文页面且内容非空。

**Acceptance Scenarios**:

1. **Given** GitBook 侧边栏，**When** 读者展开任一分部，**Then** 该分部下每一节的条目都存在且可点开，页面 H1 与条目文字一致。
2. **Given** 任一章节页面，**When** 读者阅读，**Then** 正文、信息性内容（习题、参考文献）、插图与表格均可在页内找到，不因翻译被删除或跳过。
3. **Given** 原书某节含插图或表格，**When** 读者查看对应中文页，**Then** 真插图以本地图片呈现、表格以 Markdown 表格呈现、图注表题已译；算法伪代码/结构体/配置清单/表格类图（2026-10-25 裁定共 26 幅）转写为代码块或表格呈现，不引用图片。

---

### User Story 2 - 贡献者按治理文件无缝接手 (Priority: P1)

任何后续会话的 AI 代理或人类译者打开本仓库，读 `AGENTS.md`、`PROJECT-PROGRESS.md`、`specs/001-43bsd-chinese-translation/` 四件与全局术语表后，无需重新询问项目背景即可继续翻译或校对；所有跨会话决策（书名、索引处理、术语译名、排版规范）都有据可查。

**Why this priority**: 用户明确要求"先使 AGENTS.md 适配本项目，并严格落实"与"建立全局术语表"；本书 496 页的翻译必然跨大量会话，治理文件是质量与一致性的前提。

**Independent Test**: `AGENTS.md` 中不残留任何《Life With UNIX》项目专属内容；`yi-zhe-shuo-ming.md` 术语表存在且初版条目不少于 150 条；`PROJECT-PROGRESS.md` 记录了当前任务、轮次与下一步。

**Acceptance Scenarios**:

1. **Given** `AGENTS.md`，**When** 贡献者检索书名、源 PDF 文件名、页数、结构描述，**Then** 全部与本项目实际（2.pdf、496 页、5 部分 13 章 + 词汇表 + 索引、扫描件）一致。
2. **Given** 正文出现争议术语，**When** 贡献者查术语表，**Then** 能找到唯一译名；表中查不到的按工作流先补录再使用。
3. **Given** 一次新会话，**When** 代理按 `AGENTS.md` 指引读进度文件，**Then** 能复述当前正在翻译/校对的单元与下一步动作。

---

### User Story 3 - 译文忠实、地道且保留历史视角 (Priority: P2)

专业读者逐句对照英文原文抽检，确认中文译文无漏译、无事实性错译（人名、版本号、时间线、结构体字段、算法名），语言符合中文技术写作习惯（无欧化句式、无机翻腔）；原书 1989 年视角的陈述未被今况改写，必要补充仅以"（译注：……）"形式出现。

**Why this priority**: 翻译质量是本书作为技术经典的性命；错误的内核细节比不译更有害。

**Independent Test**: 对任一已完成章节抽样 20 句与 `en/` 原文逐句对照，漏译数、事实性错误数为 0；语言问题按 `AGENTS.md` 问题类别表判定。

**Acceptance Scenarios**:

1. **Given** 已完成某节的三轮校对记录，**When** 复查者随机抽 20 句对照原文，**Then** 语义一致且无漏句。
2. **Given** 原文含 "4.3BSD 将……" 的时代性论断，**When** 译出，**Then** 译文保持原时态视角，不夹带 2020 年代现状。
3. **Given** 原文人名（如 Kirk McKusick）、命令（如 `ps`）、结构体（如 `proc`），**When** 译出，**Then** 与原文逐字符一致。

---

### User Story 4 - 扫描件内容保真提取与呈现 (Priority: P2)

读者在中文页面看到的插图、C/汇编代码、终端会话与表格，内容与 1989 年原书一致：插图从 PDF 提取原始图像而非重绘；代码逐字符保真；表格重排为居中 Markdown 表格且行列数与原书一致。原文本身由 1–2 路子代理读取页面图像视觉转录得到，PDF 内嵌 OCR 文本层完全不作为内容来源。

**Why this priority**: 本书是扫描件（ClearScan OCR），文本层存在系统性识别错误（如 I/O→1/0、Inode→!node、数字 45→4S），用户已裁定完全不信任 OCR 文本层，一切原文以页面图像为唯一权威源。

**Independent Test**: 任一代码块与对应 PDF 页图像逐字符比对一致；`.gitbook/assets/` 中每个文件都被至少一处引用且引用大小写与磁盘一致。

**Acceptance Scenarios**:

1. **Given** 原书第 X 页含 C 代码清单，**When** 译者提取，**Then** 中文页代码块内容以页图像核对后录入，注释译为中文、代码本体不动。
2. **Given** `.gitbook/assets/` 内一图片文件，**When** 运行图片引用检查，**Then** 至少被一个 `.md` 引用且能解析。
3. **Given** 原书一张 N 行 M 列表格，**When** 译出，**Then** Markdown 表格同为 M 列，缺项以 `| |` 占位。

---

### User Story 5 - 中文术语索引可检索 (Priority: P3)

读者想按术语查找内容时，使用书末的中文术语索引页：原书 Index（451–496）的词条已译为中文并按拼音排序，每条链接指向相关章节页面；英文原词保留在词条内便于反查。

**Why this priority**: 用户明确选择"翻译为中文术语索引"（工作量最大但检索价值最高的方案）；依赖全书译完后才有完整词条来源，故优先级靠后。

**Independent Test**: 索引页每个词条格式为"中文术语（English term）"，含至少一个指向已存在页面的相对链接；`links.yml` CI 通过。

**Acceptance Scenarios**:

1. **Given** 读者在索引页查"页面置换（page replacement）"，**When** 点击其链接，**Then** 跳转到第 5 章对应小节页面。
2. **Given** 全书翻译完成，**When** 运行链接检查，**Then** 索引页无死链。

---

### User Story 6 - 质量门禁全自动通过 (Priority: P3)

维护者推送后，CI（markdownlint、图片、链接、SUMMARY 一致性、AutoCorrect 空格）全部通过；本地 `check_quotes.py`、`check_bold.py` 违例为 0，与 CI 结果一致。

**Why this priority**: 门禁是交付的最后一道闸，依赖前五个故事的产物质量。

**Independent Test**: 在仓库根运行 AGENTS.md 记载的本地检查命令组合，输出违例数为 0。

**Acceptance Scenarios**:

1. **Given** 任一已完成章节，**When** 本地运行引号/加粗/markdownlint 检查，**Then** 违例数为 0。
2. **Given** 推送到远端，**When** CI 运行，**Then** markdownlint、check-images、links、file-name-check 均绿。

---

### Edge Cases

* OCR 文本层的系统性识别错误（`I/O`→`1/0`、`Inode`→`!node`、数字 `45`→`4S`、`Terminal`→`Terrninal`）：一律不从 OCR 文本层取内容；`en/` 原文由子代理视觉转录页面图像生成，翻译遇疑仍回到页面图像核对。
* 印刷页码与 PDF 页码存在固定偏移（印刷第 1 页 = PDF 第 24 页，即 PDF = 印刷 + 23；已按页脚锚点实测校准）：渲染与转录必须输出并维护 [[PAGE n]] 印刷页码标记，防止错位。
* 页面图像中代码/表格字号小或扫描噪点：渲染分辨率按需提高（不低于 200 DPI，代码页 300 DPI），子代理转录代码时逐字符照录并在存疑处标记 `[UNCLEAR]` 供人工复核。
* 正文中的原书页内交叉引用（如 "see page 210"）：改写为语义化描述或指向对应中文页面的相对链接，不得保留印刷页码。
* 扫描插图不清晰：仍提取原图，不重绘、不"修复"内容；确无法辨识的内容以译注说明。
* 双栏排版页（如参考文献、Glossary、Index）的 OCR 文本顺序错乱：按栏切分提取，人工核对顺序。
* 原书 trademark 说明页、版权页：版权信息页不译（保留原样说明），献词页照译。
* 同一英文术语在内核语境与日常语境含义不同（如 block 块/阻塞、channel）：术语表按义项分别登记译名。
* PDF 中无法确定的技术细节（人名职务、公司沿革）：联网复核至少三次后再落笔，查证过程记入术语表备注或进度文件。

## Requirements *(mandatory)*

### Functional Requirements

* **FR-001**: `AGENTS.md` 必须完整改写为本项目版本：书名《4.3BSD UNIX 操作系统的设计与实现》、源文件 `2.pdf`（496 页、扫描件、ClearScan OCR）、结构（前言 + 5 部分 13 章 + 词汇表 413–450 + 索引 451–496）、治理文件清单与工作流全部指向本项目；不得残留《Life With UNIX》专属描述（如 LifeWithUnux_LibesRessler.pdf、20 个提取文件、3 张插图等）。
* **FR-002**: 必须建立全局术语表 `yi-zhe-shuo-ming.md`：初版登记不少于 150 条术语，每条含英文原词、唯一中文译名、必要备注（义项、来源、查证链接）；人名、公司译名规则单列；译名与《4.4BSD 操作系统的设计与实现》官方中译本及 FreeBSD 中文社区既有译法保持兼容，不冲突。
* **FR-003**: 不确定的术语译名必须联网核查后方可登记入表；至少对 10 个高风险术语（如 kluster、silly-window syndrome、scatter/gather、C-list、line discipline、core map、swap space、mbuf、socket、daemon 等）留存认证来源。
* **FR-004**: `SUMMARY.md` 必须覆盖原书全部结构：前言、5 个分部标题、13 章（每章章首页 + 每节独立一页）、词汇表附录、中文术语索引；第一行保持 `# Table of contents` 不变。
* **FR-005**: 章节页面必须按 `AGENTS.md` 命名规则创建：章首页 `X.-<拼音slug>.md`、节页面 `X.Y.-<拼音slug>.md`；节内子节 `X.Y.Z` 用 H2、`X.Y.Z.W` 用 H3，不跳级；文件名不含空格、中文与英文冒号，兼容 Windows。
* **FR-006**: 必须建立原文提取管线（`script/render_pages.py` 等）：将 PDF 各页渲染为高分辨率页面图像，产出带 `[[PAGE n]]` 印刷页码标记的 `en/` 文本，按章切分；`en/` 与 `script/` 不入版本控制。
* **FR-016**: 完全不信任 PDF 内嵌 OCR 文本层（用户 2026-10-24 裁定）：`en/` 原文必须由子代理读取页面图像视觉转录生成；OCR 文本层不得作为任何译文内容的来源，至多用于页码定位与结构普查。视觉转录以 1–2 路并行子代理执行，转录范围含正文、脚注、图注、表格结构与代码清单（代码逐字符照录）。
* **FR-007**: 插图必须提取到 `.gitbook/assets/` 并以相对路径引用；引用写法与磁盘文件名逐字符大小写一致；每个资产文件至少被一处引用。
* **FR-008**: 译文必须逐项遵守 `AGENTS.md` 编写规范：中文弯引号成对且方向正确、加粗两侧恰好一个半角空格、CJK 与西文间半角空格（书名号内同样）、代码块按内容选语言标记（禁 `text`）、表格居中且列数一致（复杂表格按 2026-10-24 用户裁定允许 HTML `<table>`，仅限表格场景）、路径与 IP 用加粗、第二人称"你"。
* **FR-009**: 已译内容必须执行"三轮逐句校对 + 一轮复查"递归工作流（仍有问题则再来三轮，直至无问题）；每轮在 `PROJECT-PROGRESS.md` 登记，未执行不得勾选。
* **FR-010**: 词汇表（Glossary，413–450）必须全文翻译为附录页面，词条按原书字母序或拼音序组织并在译注中说明编排方式。
* **FR-011**: 索引（Index，451–496）必须转译为中文术语索引：词条译为中文（保留英文原词）、按拼音排序、每个词条链接到至少一个存在的章节页面。
* **FR-012**: 原书 1989 年视角的陈述不得以今况改写；确需补充现状时仅以"（译注：……）"单独成段，且全书译注保持克制。
* **FR-013**: 版本号、人名、书名、URL、邮箱、命令、结构体字段、错误信息等必须与原文逐字符一致；代码块与终端输出禁止篡改，代码注释译为中文。
* **FR-014**: 提交策略：每完成一章/一节/一批文件立即以中文一行提交信息提交到 `main`；未经用户要求不 push、不 force。
* **FR-015**: 必须创建 `PROJECT-PROGRESS.md` 与 `CHANGELOG.md`：前者记录当前任务、轮次、下一步，后者记录翻译与校对里程碑。

### Key Entities *(include if feature involves data)*

* **术语条目（Glossary Entry）**：英文原词、义项、唯一中文译名、备注（查证来源）；隶属全局术语表，只增不删，译名一经登记不得二义。
* **章节页面（Chapter Page）**：与原书 `X`/`X.Y` 一一对应；属性有文件名 slug、H1（与 `SUMMARY.md` 条目逐字一致）、层级、所属分部。
* **SUMMARY 条目（TOC Entry）**：导航树节点；分部为 `##` 纯标题，章/节为 `*` 链接条目；是标题与文件存在性的唯一数据源。
* **图片资产（Image Asset）**：从 PDF 提取的原始插图；属性有文件名（引用大小写必须一致）、被引用页面集合。
* **en/ 原文文件（Source Text）**：按章切分的英文文本，含 `[[PAGE n]]` 印刷页码标记；仅供对照，不入库不修改。
* **索引词条（Index Entry）**：中文术语、英文原词、拼音序键、指向章节页面的链接集合。
* **进度记录（Progress Record）**：单元（章/节）、轮次（初译/校对 1–3/复查）、完成日期、遗留问题。

## Success Criteria *(mandatory)*

### Measurable Outcomes

* **SC-001**: `SUMMARY.md` 的章/节条目与原书目录逐条对应，缺项为 0（以 `script/compare_structure.py` 对比差异为 0 判定）。
* **SC-002**: 术语表初版条目数 ≥ 150；此后任意时点同一英文术语在同一义项下最多一个译名（人工抽查 30 条零冲突）。
* **SC-003**: 全部内容页通过本地检查：`check_quotes.py` 违例 0、`check_bold.py` 违例 0、markdownlint 违例 0。
* **SC-004**: `.gitbook/assets/` 内文件 100% 被引用且引用可解析、大小写与磁盘一致（check-images CI 通过）。
* **SC-005**: 术语索引页与全部正文内链接 100% 可解析（links CI 通过）。
* **SC-006**: 每个已宣称完成的章/节在 `PROJECT-PROGRESS.md` 有对应轮次记录，抽查 10 个单元记录与 git 提交历史一致，虚记为 0。
* **SC-007**: 全书最终状态：前言、13 章（含各章习题与参考文献）、词汇表附录、中文术语索引全部非空且经过至少一轮完整校对流程。

## Assumptions

* 书名定为《4.3BSD UNIX 操作系统的设计与实现》，首次出现处括注英文原名（用户 2026-10-24 确认）。
* Index 译为中文术语索引（拼音排序、链接到章节）；Glossary 全文翻译为附录（用户 2026-10-24 确认）。
* `2.pdf` 是唯一权威源：其内嵌 ClearScan OCR 文本层完全不信任（用户 2026-10-24 裁定），一切内容以渲染出的页面图像为准，由 1–2 路子代理视觉转录。PDF 本体不入版本控制，渲染页图像与转录产物（`en/`）同样不入库。
* 本地工作目录 `en/`（提取原文）与 `script/`（工具脚本）被 `.gitignore` 排除，不随仓库分发；新克隆需重跑提取脚本。
* `.github/workflows/` 沿用 FreeBSD 中文社区既有 CI 约定（sync-headers、mulu、file-name-check、markdownlint、md-padding、AutoCorrect、check-images、links、create-pdf、Auto-Assign），不新增与之冲突的本地规则。
* 翻译与校对直接提交 `main` 分支；未经用户要求不 push。
* 术语风格以简体中文技术出版惯例为准，参考《4.4BSD 操作系统的设计与实现》官方中译本与社区既有译法；无法确定者保留英文并登记。
* 各章 Exercises 译出（题号保持），References 保留英文文献原样、仅节标题译为"参考文献"；献词页照译，版权/商标说明页保留原文不译。

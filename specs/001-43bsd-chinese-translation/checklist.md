# 验收检查点：《4.3BSD UNIX 操作系统的设计与实现》简体中文 GitBook 翻译项目

**用途**：本项目最终验收。勾选权归复核人——`[x]` 表示该判据经复核通过；生成时一律 `[ ]`。
**追溯**：spec.md（FR-001–FR-016、SC-001–SC-007、US1–US6 场景）与 tasks.md（T001–T085）；无对应检查点的条目在文末"缺口清单"列明。

## 一、实现完整性

* [ ] Check 1: `AGENTS.md` 存在且为项目专属版本：文中出现书名《4.3BSD UNIX 操作系统的设计与实现》、源文件名 `2.pdf`、页数 496、结构"前言 + 5 部分 13 章 + 词汇表（413–450）+ 索引（451–496）"。（来源：FR-001／T010）
* [ ] Check 2: `AGENTS.md` 全文检索 `Life With UNIX`、`LifeWithUnux`、`372`、`LibesRessler`、`mu-lu` 手编指引等模板项目痕迹，命中数为 0。（来源：FR-001／T026）
* [ ] Check 3: `AGENTS.md` 含"完全不信任 OCR 文本层"与"1–2 路子代理视觉转录"两条裁定的成文规则。（来源：FR-016／T010）
* [ ] Check 4: `SUMMARY.md` 第一行为 `# Table of contents`（逐字符判定）。（来源：FR-004／T016）
* [ ] Check 5: `SUMMARY.md` 含前言条目、5 个 `## 第N部分` 纯标题、13 章全部章/节条目、词汇表与术语索引条目；与原书目录（印刷 xiii–xxii）逐条对应，缺项 0。（来源：FR-004／T016、SC-001）
* [ ] Check 6: `SUMMARY.md` 每个链接路径指向存在的 `.md` 文件，且该文件 H1 与条目文字逐字一致（抽样 ≥30 条全通过）。（来源：FR-004/FR-005／T016）
* [ ] Check 7: 章节文件名全部形如 `X.-slug.md`/`X.Y.-slug.md`，无空格、无中文字符、无英文冒号，Windows 下可创建（实际列目录验证）。（来源：FR-005／T016）
* [ ] Check 8: 全书全部页面非空：前言 2 页、13 章全部节页、`fu-lu/ci-hui-biao.md`、`fu-lu/shu-yu-suo-yin.md` 每页正文不少于 1 段实质内容。（来源：US1 场景 2／T050–T056、SC-007）
* [ ] Check 9: `yi-zhe-shuo-ming.md` 存在且术语总表条目数 ≥150（表格行计数），每条含英文原词与中文译名（保留英文者中文列为"—"）。（来源：FR-002／T020–T022）
* [ ] Check 10: `yi-zhe-shuo-ming.md` 至少 10 个高风险术语（kluster、silly-window syndrome、scatter/gather、C-list、line discipline、core map、swap space、mbuf、socket、daemon）备注列含查证来源。（来源：FR-003／T023）
* [ ] Check 11: 人名表、公司/机构表、书名/文献表三节齐备且各有 ≥5 条。（来源：FR-002／T024–T025）
* [ ] Check 12: `PROJECT-PROGRESS.md` 存在且顶部含"当前任务/下一步/轮次记录"三段；`CHANGELOG.md` 存在且含项目启动条目。（来源：FR-015／T019）
* [ ] Check 13: `en/` 下 16 个转录文件（01 前言、02–14 第 1–13 章、15 词汇表、16 索引底稿）全部存在。（来源：FR-006／T031–T045）
* [ ] Check 14: `en/` 每个文件 `[[PAGE n]]` 标记每页恰一个且页码单调递增（脚本或逐文件 grep 验证）。（来源：FR-006／contracts/en-transcription.md）
* [ ] Check 15: `en/` 全部文件 `[UNCLEAR]` 计数为 0，或每条附有主会话裁决注记。（来源：FR-006／T047）
* [ ] Check 16: 随机抽 3 页，`en/` 转录文本与 `script/pages/` 对应 PNG 逐词一致（含脚注与标点）。（来源：US4 场景／T047）
* [ ] Check 17: `py script/render_pages.py`、`check_quotes.py`、`check_bold.py`、`compare_structure.py`、`extract_figures.py` 五个脚本存在且各自可运行退出码 0。（来源：T011–T015）
* [ ] Check 18: `.gitbook/assets/` 内全部插图文件与 `en/` 的 `[FIGURE p.n …]` 标记按页码一一对应（对照 `script/figures-map.md`）。（来源：FR-007／T046）
* [ ] Check 19: `README.md` 含书名（中英对照）、四位作者、原书简介与项目链接。（来源：T002）
* [ ] Check 20: `.gitignore` 含 `en/`、`script/pages/`、`*.pdf`；`git status` 中 2.pdf、en/、script/ 不出现为未跟踪内容。（来源：T001）

## 二、需求覆盖

* [ ] Check 21: `en/` 全部内容的生成过程不含"从 PDF 文本层复制"路径——转录任务提示词与子代理回报记录均指向页面图像。（来源：FR-016／R-1）
* [ ] Check 22: 视觉转录过程中同时运行的子代理数 ≤2（任务派发记录验证）。（来源：FR-016／T030–T045）
* [ ] Check 23: 任选 3 个已完成章节，每章抽 20 句与 `en/` 对照：漏译句数 0、事实性错译（人名/版本号/时间线/结构体字段/算法名）0。（来源：US3 场景 1／T060–T065）
* [ ] Check 24: 抽 10 处原书时代性论断（如"4.3BSD 将……"），译文均保持 1989 视角、无今况改写；全书"（译注："出现处逐条审阅均属克制补充。（来源：FR-012／US3 场景 2）
* [ ] Check 25: 抽 20 处人名/命令/结构体/版本号（如 `proc`、`ps`、4.2BSD、VAX-11/780），与原文逐字符一致。（来源：FR-013／US3 场景 3）
* [ ] Check 26: 任选 3 个含代码清单的页面，代码块与 `script/pages/` 对应 PNG 逐字符比对一致；块内注释为中文、代码本体无改动。（来源：FR-013／US4 场景 1）
* [ ] Check 27: 任选 3 张原书表格，中文页 Markdown 表格列数与原书一致、居中声明、缺项以 `| |` 占位、无省略管道符。（来源：FR-008／US4 场景 3）
* [ ] Check 28: 全部内容页 `py script/check_quotes.py` 违例 0（弯引号成对、方向正确，无直引号/直角引号/日式半角引号）。（来源：FR-008／SC-003、T080）
* [ ] Check 29: 全部内容页 `py script/check_bold.py` 违例 0（`**加粗**` 两侧恰好一个半角空格）。（来源：FR-008／SC-003、T080）
* [ ] Check 30: 全部内容页 markdownlint-cli2（`.github/.markdownlint.json` 配置，排除 en/、script/、node_modules/）违例 0。（来源：FR-008／SC-003、T080）
* [ ] Check 31: 抽 30 处中西文混排（含书名号内），中英文/中文与数字间均有半角空格。（来源：FR-008）
* [ ] Check 32: 全书检索 `<div`/`<span`/`xref:`/`link:`/行尾 `+` 软换行，命中 0；正文无 HTML。（来源：FR-008）
* [ ] Check 33: 正文抽 20 处路径与 IP，均为加粗而非反引号；代码块内路径保持原样。（来源：FR-008）
* [ ] Check 34: 全书检索"您"，命中 0（第二人称统一"你"）。（来源：FR-008）
* [ ] Check 35: `fu-lu/ci-hui-biao.md` 覆盖 `en/15-glossary.txt` 全部词条（词条计数一致），开头有编排方式译注。（来源：FR-010／T056）
* [ ] Check 36: `fu-lu/ci-hui-biao.md` 与 `yi-zhe-shuo-ming.md` 共同术语的译名 100% 一致（全量比对，冲突 0）。（来源：FR-010／T066）
* [ ] Check 37: `fu-lu/shu-yu-suo-yin.md` 词条格式为"中文术语（English term）"，按拼音排序无乱序段，每词条 ≥1 个链接。（来源：FR-011／US5 场景）
* [ ] Check 38: 术语索引全部链接（含正文内链接）可解析，死链 0。（来源：FR-011／SC-005、T072）
* [ ] Check 39: 正文检索 `see page`/`See Chapter`/`参见第 … 章` 式硬编码引用，命中 0；抽查改写处语义正确或为可解析相对链接。（来源：FR-008 交叉引用条款／T057）
* [ ] Check 40: 每章习题（Exercises）与参考文献（References）在中文页面存在：题号一致、文献条目为英文原样且编号一致、节标题为"习题/参考文献"。（来源：US1 场景 2／T051–T055）
* [ ] Check 41: `PROJECT-PROGRESS.md` 轮次表抽 10 个单元与 `git log --oneline` 对账，虚记 0（宣称完成的轮次均有对应提交）。（来源：FR-009／SC-006）
* [ ] Check 42: 全部提交在 `main` 分支、提交信息为中文一行；`git log` 中无 push 强制/force 痕迹，远端未经用户要求未被推送（`git status -sb` 无 ahead/pushed 争议）。（来源：FR-014）
* [ ] Check 43: 各章翻译期间新术语先录入 `yi-zhe-shuo-ming.md` 再使用——抽 10 个译后新增术语，表中登记日期不晚于首次正文提交。（来源：FR-002／US2 场景 2）

## 三、边界与异常

* [ ] Check 44: `en/` 转录文本中检索 OCR 典型错误串 `1/0 System`、`!node`、`4S`（作为页码/数字），命中 0——证明内容取自图像而非文本层。（来源：Edge Cases／FR-016）
* [ ] Check 45: `[[PAGE n]]` 使用的页码与 `script/pages/` 文件名页码、原书印刷页码三方一致（抽 5 页对账，含前置罗马页 vii–xii）。（来源：Edge Cases／R-3）
* [ ] Check 46: 代码密集页（第 8、13 章代码清单页）的渲染 PNG 分辨率 ≥300 DPI（文件属性或渲染参数记录验证）。（来源：Edge Cases／T030）
* [ ] Check 47: 双栏页（References/Glossary/Index 转录）抽 2 页验证栏序：先左栏后右栏，无跨栏串行。（来源：Edge Cases／contracts/en-transcription.md）
* [ ] Check 48: 版权/商标说明页未译，`README.md` 或前言页有保留原文的说明；献词页已照译。（来源：Assumptions／T050）
* [ ] Check 49: 多义术语（block、channel 等至少 5 个）在 `yi-zhe-shuo-ming.md` 按义项分行登记，各义项译名唯一。（来源：Edge Cases／FR-002）
* [ ] Check 50: 高风险术语查证记录可定位：备注列的来源链接可访问或引用了可核查出处（抽 10 条全部可定位）。（来源：FR-003／R-5）
* [ ] Check 51: 插图引用大小写抽 20 处与磁盘文件名逐字符一致（Windows 大小写不敏感陷阱检查）。（来源：Edge Cases／FR-007、T082）
* [ ] Check 52: `.gitbook/assets/` 无悬空文件（每个文件被 ≥1 处引用）、引用无外链 URL。（来源：FR-007／SC-004）

## 四、既有功能未回归

* [ ] Check 53: `.github/workflows/` 十个工作流文件零改动（`git diff --stat HEAD -- .github` 为空，Phase 1 提交后）。（来源：Assumptions／T003）
* [ ] Check 54: `mu-lu.md` 由 CI 生成且首行为 `# 目录`；本地无手改记录（`git log -- mu-lu.md` 仅 CI/mulu 提交）。（来源：Assumptions）
* [ ] Check 55: 推送前（经用户同意后）CI 十个工作流全部绿：markdownlint、check-images、links、file-name-check、sync-headers、mulu、md-padding、AutoCorrect、create-pdf、Auto-Assign。（来源：US6 场景 2／T085）
* [ ] Check 56: `.specify/`、`.zcode/`、`specs/` 已入库且不干扰 CI（markdownlint 排除规则覆盖）。（来源：T003）
* [ ] Check 57: `quickstart.md` 场景 A–E 全部通过并留有运行记录（进度文件或会话汇报）。（来源：T085）
* [ ] Check 58: `script/compare_structure.py` 最终运行差异为 0。（来源：SC-001／T081）
* [ ] Check 59: 术语表抽查 30 条：同一英文术语同一义项最多一个译名，冲突 0。（来源：SC-002／T083）
* [ ] Check 60: `PROJECT-PROGRESS.md` 末次更新晚于最后一个内容提交（会话结束收口动作完成）。（来源：FR-015／T084）

## 缺口清单（无对应检查点的需求/任务）

* tasks.md T017（渲染词汇表与前置页）：已由 Check 14/45 覆盖其产物判定，渲染动作本身不设独立检查点——属过程性任务，产物可判定即可。
* tasks.md T030（渲染全书正文页）：同上，由 Check 16/46 覆盖。
* tasks.md T034–T045 各章转录任务：逐章检查点不单列（同构任务），由 Check 13–16、44、47 统一判定。
* tasks.md T060–T066 各轮校对：由 Check 23、24、41 统一判定轮次真实性与效果。
* spec US1 场景 1（GitBook 侧边栏导航）：依赖 GitBook 渲染环境，本地以 Check 5/6（SUMMARY↔文件↔H1 三方一致）代替判定，CI 同步机制兜底。
* spec SC-007"至少一轮完整校对流程"：由 Check 41 抽样对账 + `PROJECT-PROGRESS.md` 轮次表完整性（Check 12/60）共同覆盖。

# 译者说明与全局术语表

本书译自 *The Design and Implementation of the 4.3BSD UNIX Operating System*（Samuel J. Leffler、Marshall Kirk McKusick、Michael J. Karels、John S. Quarterman 著，Addison-Wesley，1989）。本表是全书翻译的 **唯一术语依据**：正文用词与本表冲突时，以本表为准；本表未登记的术语，须先补录再使用。

**译名参照系**（优先级从高到低）：

1. 《4.4BSD 操作系统的设计与实现》官方中译本（本书姊妹篇，术语高度重叠）；
2. 操作系统与网络经典教材通行译法（《操作系统概念》《计算机网络》等中译本）；
3. FreeBSD 中文社区既有项目译法（含 FreeBSD 中文使用手册）。

三者冲突时取①；均无先例且无把握者保留英文，备注“待议”。

## 高频约定

* **shell**：不译为“壳/外壳”，保留 shell。
* **daemon** → 守护进程；**kernel** → 内核；**source** → 源码；**copy** → 复制（禁止“拷贝”）。
* **repository** → 存储库（禁止“仓库”）。
* **memory management** → 存储管理（4.4BSD 官方中译本第 5 章标题译法）；**main memory** → 主存；**virtual memory** → 虚拟存储（4.4BSD 中译本语系），行文需要时亦可作“虚拟内存”，以本表为准。
* **paging** → 调页；**swapping** → 交换；**swap space** → 交换空间。
* **人名一律保留英文原名**，不音译（见人名表）。
* **UNIX** 大小写随原书；原书刻意用 Unix 处保持原样。
* 第二人称一律“你”。

## 术语对照总表

同一英文词多义时按义项分行；“—”表示保留英文不译。

| 英文 | 中文 | 备注 |
| ---- | ---- | ---- |
| absolute pathname | 绝对路径名 | |
| access rights | 访问权限 | |
| accounting | 记账 | 系统记账（system accounting） |
| address space | 地址空间 | |
| address translation | 地址转换 | |
| ARP（Address Resolution Protocol） | 地址解析协议（ARP） | |
| ARPANET | — | 专名保留 |
| assembler | 汇编器 | |
| association | 关联 | 12.1 节，端口与地址的关联 |
| asynchronous | 异步 | |
| autoconfiguration | 自动配置 | |
| backing store | 后备存储 | |
| block（存储） | 块 | 磁盘/文件系统块 |
| block（等待） | 阻塞 | 进程状态；按义项区分 |
| block device | 块设备 | |
| block special file | 块特殊文件 | |
| bootstrap | 自举 | 百度百科“自举引导”；FreeBSD 手册亦用“引导”，两词同义时统一“自举” |
| buffer | 缓冲区 | |
| buffer cache | 缓冲区高速缓存 | |
| bus | 总线 | |
| byte | 字节 | |
| cache | 高速缓存 | |
| canonical mode | 规范模式 | 终端行规程模式 |
| carrier | 载波 | modem 控制语境 |
| character device | 字符设备 | |
| C-list | C 链表（C-list） | 终端字符链表，正文可保留 C-list |
| client | 客户端 | |
| clock interrupt | 时钟中断 | |
| cluster（磁盘） | 簇 | |
| kluster / klustering | — | 4.3BSD 特有 K 拼写（原书 5.11 节 “No more than 16 klusters”），保留原文并加译注 |
| command interpreter | 命令解释器 | |
| compiler | 编译器 | |
| congestion | 拥塞 | |
| congestion control | 拥塞控制 | |
| connection | 连接 | |
| console | 控制台 | |
| context | 上下文 | |
| context switching | 上下文切换 | |
| control block | 控制块 | |
| core dump | 核心转储 | |
| core map | 核心映射表 | cmap；待视觉转录词汇表后复核 |
| CPU | CPU | |
| crash | 崩溃 | |
| cylinder | 柱面 | |
| cylinder group | 柱面组 | FFS |
| daemon | 守护进程 | |
| data structure | 数据结构 | |
| datagram | 数据报 | |
| debugging | 调试 | |
| demand paging | 请求调页 | 教材通行译法 |
| descriptor | 描述符 | |
| descriptor table | 描述符表 | |
| device | 设备 | |
| device driver | 设备驱动（程序） | |
| direct memory access（DMA） | 直接存储器访问（DMA） | |
| directory | 目录 | |
| disk | 磁盘 | |
| disk quota | 磁盘配额 | |
| distributed system | 分布式系统 | |
| domain（通信） | 通信域 | socket domain |
| double (doubly) linked list | 双向链表 | |
| effective user/group ID | 有效用户/组 ID | |
| environment | 环境 | |
| Ethernet | 以太网 | |
| fault | 故障 | page fault 译“缺页” |
| field | 字段 | |
| FIFO | 命名管道（FIFO） | |
| file | 文件 | |
| file descriptor | 文件描述符 | |
| file offset | 文件偏移量 | |
| filesystem | 文件系统 | |
| fill-on-demand | 按需填充 | |
| flags | 标志 | |
| flush | 刷新 | |
| foreground | 前台 | |
| fork | — | 系统调用名保留 |
| fragment | 片 | FFS 块内分段 |
| free list | 空闲表 | |
| gateway | 网关 | 原书时代的 router 多称 gateway，照原书用词 |
| global CLOCK algorithm | 全局 CLOCK 算法 | |
| hash | 哈希 | |
| host | 主机 | |
| host identifier | 主机标识符 | |
| inode（index node） | 索引节点 | |
| initialization | 初始化 | |
| interface | 接口 | |
| Internet（DARPA Internet） | Internet | 专名保留；泛指互联网时译“互联网” |
| internetwork | 网际互联网 | 视上下文 |
| interrupt | 中断 | |
| interrupt handler | 中断处理程序 | |
| interrupt priority level（IPL） | 中断优先级（IPL） | |
| interprocess communication（IPC） | 进程间通信（IPC） | |
| ioctl | — | 系统调用名保留 |
| job control | 作业控制 | |
| kernel | 内核 | |
| kernel mode | 内核态 | |
| kernel organization | 内核结构 | 4.4BSD 官方中译本第 2 章译法 |
| kill | — | 命令/信号名保留 |
| line discipline | 行规程 | Linux 内核文档中文社区与 dog250 经典文章通行 |
| link | 链接 | |
| linked list | 链表 | |
| locality | 局部性 | |
| lock | 锁 | |
| logical block | 逻辑块 | |
| login | 登录 | /bin/login 保留路径 |
| machine-dependent | 与机器相关的 | |
| machine-independent | 与机器无关的 | |
| main memory | 主存 | |
| mapping | 映射 | |
| memory | 存储器／内存 | 按语境：主存实体用“内存”，抽象层次用“存储器” |
| memory management | 存储管理 | 4.4BSD 官方中译本第 5 章标题 |
| message | 消息 | |
| mbuf | — | 内存缓冲区，保留 mbuf |
| modem | 调制解调器 | |
| mode | 模式 | |
| mount / unmount | 挂载／卸载 | 社区通行；旧教材“安装/拆卸”不采用 |
| multiplexing | 多路复用 | |
| multiprogramming | 多道程序设计 | |
| network | 网络 | |
| network interface | 网络接口 | |
| nice | — | nice 值保留 |
| out-of-band data | 带外数据 | |
| open file table | 打开文件表 | |
| operating system | 操作系统 | |
| overlay | 覆盖 | |
| owner | 属主 | |
| page | 页 | |
| page fault | 缺页 | |
| page frame | 页框 | |
| pagein | 页面换入 | 5.11 节 Pagein of Swapped Pages |
| page replacement | 页面置换 | |
| page table | 页表 | |
| page-table entry（PTE） | 页表项（PTE） | |
| paging | 调页 | |
| paging daemon（pagedaemon） | 调页守护进程 | |
| pathname | 路径名 | |
| permission | 权限 | |
| physical address | 物理地址 | |
| pipe | 管道 | |
| pointer | 指针 | |
| port（网络） | 端口 | |
| port / porting（移植） | 移植 | 与“端口”按义项区分 |
| preemption | 抢占 | |
| priority | 优先级 | |
| privileged instruction | 特权指令 | |
| proc structure | proc 结构 | 结构体名保留 |
| process | 进程 | |
| process group | 进程组 | |
| process ID（PID） | 进程 ID（PID） | |
| profiling | 剖析 | 计时剖析 |
| protocol | 协议 | |
| protocol control block（PCB） | 协议控制块 | 与进程控制块按语境区分 |
| pseudo-device | 伪设备 | |
| queue | 队列 | |
| queue limiting | 队列限长 | 11.6 节 |
| quota | 配额 | |
| raw device | 裸设备 | |
| raw I/O | 裸 I/O | |
| raw socket | 原始套接字 | |
| reentrant | 可重入 | |
| relative pathname | 相对路径名 | |
| replacement algorithm | 置换算法 | |
| resident | 驻留 | |
| resource | 资源 | |
| resource limit | 资源限制 | |
| retransmission | 重传 | |
| round-robin | 轮转 | |
| round-trip time（RTT） | 往返时间（RTT） | |
| route / routing | 路由 | |
| routing redirect | 路由重定向 | |
| routing table | 路由表 | |
| run queue | 运行队列 | |
| swapping process（swapper） | 交换进程 | 0 号进程 |
| scatter/gather I/O | 分散/聚集 I/O | 百度百科词条“分散/聚集方式 I/O”、微软文档 |
| scheduling | 调度 | |
| secondary storage | 辅存 | 亦可“二级存储器” |
| sector | 扇区 | |
| seek | 寻道 | |
| select | — | 系统调用名保留 |
| semaphore | 信号量 | |
| shared text | 共享正文段 | text structure |
| shell | — | 不译 |
| signal | 信号 | |
| signal delivery | 信号递送 | |
| signal posting | 信号发送 | |
| silly window syndrome（SWS） | 糊涂窗口综合症 | 中文维基百科、百度百科通行译法 |
| single-user mode | 单用户模式 | |
| slow start | 慢启动 | |
| socket | 套接字 | 教材通行译法 |
| socket address | 套接字地址 | |
| software interrupt | 软件中断 | |
| special file | 特殊文件 | |
| stack | 栈 | |
| standard input/output/error | 标准输入/输出/错误 | |
| state | 状态 | |
| sticky bit | 粘滞位 | |
| storage | 存储 | |
| structure | 结构体 | C 语境 |
| superblock | 超级块 | |
| superuser | 超级用户 | |
| swap | 交换 | |
| swap space | 交换空间 | FreeBSD 中文使用手册译法 |
| swapin / swapout | 换入／换出 | |
| swapping | 交换 | 教材另有“对换”，本表统一“交换” |
| synchronization | 同步 | |
| system call | 系统调用 | |
| tape | 磁带 | |
| terminal | 终端 | |
| text segment | 正文段 | |
| thrashing | 抖动 | |
| timeout | 超时 | |
| timer | 计时器 | |
| timesharing | 分时 | |
| top half / bottom half | 上半部／下半部 | 终端驱动与中断处理语境 |
| trailer protocol | 尾部协议 | |
| trap | 陷阱 | |
| tty | — | 保留 tty |
| UDP（User Datagram Protocol） | 用户数据报协议（UDP） | |
| UID / GID | 用户标识符／组标识符 | |
| UNIBUS / MASSBUS | — | VAX 总线名保留 |
| user mode | 用户态 | |
| user structure（u.） | user 结构（u.） | |
| utility | 实用程序 | |
| VAX | — | 机型名保留 |
| virtual address | 虚拟地址 | |
| virtual address space | 虚拟地址空间 | |
| virtual memory | 虚拟存储 | 4.4BSD 中译本语系 |
| window | 窗口 | TCP 语境 |
| working set | 工作集 | |
| workstation | 工作站 | |
| 4.2BSD fast filesystem | 快速文件系统 | FFS |

## 人名表（一律不音译，首次出现以同位语补充身份）

| 英文 | 身份备注 |
| ---- | ---- |
| Samuel J. Leffler（Sam Leffler） | 本书第一作者，时供职硅图公司（Silicon Graphics） |
| Marshall Kirk McKusick | 本书作者，加州大学伯克利分校，BSD 核心开发者 |
| Michael J. Karels | 本书作者，加州大学伯克利分校，4.3BSD 主要开发者 |
| John S. Quarterman | 本书作者，德克萨斯互联网咨询公司 |
| Ken Thompson | UNIX 创始人之一，贝尔实验室 |
| Dennis Ritchie | C 语言与 UNIX 创始人之一，贝尔实验室 |
| Bill Joy | BSD 主要开发者，vi 作者，Sun 公司联合创始人 |
| Keith Bostic | BSD 开发者 |
| Özalp Babaoğlu | 按需填充成组读取（fill-on-demand klustering）论文作者之一 |
| Rob Pike、Brian Kernighan 等 | 后续章节出现时补录 |

## 公司/机构表

| 英文 | 中文 | 备注 |
| ---- | ---- | ---- |
| University of California at Berkeley | 加州大学伯克利分校 | |
| Bell Laboratories / Bell Labs | 贝尔实验室 | |
| Western Electric | 西方电气公司 | |
| AT&T | — | 保留 |
| IBM | — | 保留 |
| DEC（Digital Equipment Corporation） | — | 保留 DEC；需要全称时译“数字设备公司” |
| Sun Microsystems | — | 保留 Sun |
| Xerox | 施乐 | Xerox PARC 施乐帕洛阿尔托研究中心 |
| Hewlett-Packard | 惠普 | |
| Massachusetts Institute of Technology（MIT） | 麻省理工学院 | |
| DARPA | 美国国防高级研究计划局 | 正文中 DARPA Internet 保留专名 |
| Silicon Graphics | 硅图公司 | |
| Addison-Wesley | 艾迪生-韦斯利 | 出版社 |
| McGraw-Hill | 麦格劳-希尔 | 出版社 |

## 书名/文献表

| 原名 | 译名 | 备注 |
| ---- | ---- | ---- |
| The Design and Implementation of the 4.3BSD UNIX Operating System | 《4.3BSD UNIX 操作系统的设计与实现》 | 本书，用户 2026-10-24 裁定 |
| The Design and Implementation of the 4.4BSD Operating System | 《4.4BSD 操作系统的设计与实现》 | 官方中译本，术语参照系① |
| The C Programming Language（Kernighan & Ritchie） | 《C 程序设计语言》 | 有中文译本 |
| The UNIX Programming Environment（Kernighan & Pike） | 《UNIX 编程环境》 | 有中文译本 |
| The Design of the UNIX Operating System（Bach） | 《UNIX 操作系统设计》 | 有中文译本 |
| Operating System Concepts（Peterson & Silberschatz） | 《操作系统概念》 | 有中文译本 |
| Life with UNIX（Libes & Ressler, 1988） | 《UNIX 生活：写给每个人的指南》 | FreeBSD 中文社区姊妹译作 |
| The Multics System（Organick, 1975） | — | 无中文译本，保留英文 |

## 查证来源（高风险术语，2026-10-24 联网核查）

* memory management→存储管理、virtual memory→虚拟存储、kernel organization→内核结构：[4.4BSD操作系统设计与实现·目录（百度百科）](https://baike.baidu.com/item/4.4BSD%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E8%AE%BE%E8%AE%A1%E4%B8%8E%E5%AE%9E%E7%8E%B0/675953)、[Flier Lu 读书笔记](https://www.cnblogs.com/flier/archive/2004/07/08/22296.html)
* silly window syndrome→糊涂窗口综合症：[糊涂窗口综合症·中文维基百科](https://zh.wikipedia.org/zh-hans/%E7%B3%8A%E6%B6%82%E7%AA%97%E5%8F%A3%E7%BB%BC%E5%90%88%E7%97%87)
* kluster 的 K 拼写为 4.3BSD 原书特有：[原书影印（vdoc.pub）](https://vdoc.pub/documents/the-design-and-implementation-of-the-43bsd-unix-operating-system-318lt657atsg)（“No more than 16 klusters (32 pages on a VAX)”）；4.4BSD 起改回 cluster
* line discipline→行规程：[Linux 内核文档 TTY Line Discipline](https://docs.kernel.org/driver-api/tty/tty_ldisc.html) 及中文社区通行译法
* scatter/gather I/O→分散/聚集 I/O：[分散/聚集方式 I/O（百度百科）](https://baike.baidu.com/item/%E5%88%86%E6%95%A3/%E8%81%9A%E9%9B%86%E6%96%B9%E5%BC%8FIO/10059756)
* swap space→交换空间：[FreeBSD 中文使用手册](https://docs-archive.freebsd.org/doc/7.2-RELEASE/usr/share/doc/zh_CN/books/handbook/book.html)
* bootstrap→自举：[自举引导（百度百科）](https://baike.baidu.com/item/%E8%87%AA%E4%B8%BE%E5%BC%95%E5%AF%BC/3067459)
* socket→套接字、datagram→数据报：谢希仁《计算机网络》通行译法

## 维护规则

* 翻译推进中新术语随时补录（先录后用）；词汇表（Glossary，印刷 413–450）视觉转录完成后，须以其词条为准对本表做一轮全面校准。
* 同一英文术语同一义项最多一个译名；改译名须全书同步替换并在 `CHANGELOG.md` 记录。
* 多义词按义项分行登记（block、port、memory 等）。

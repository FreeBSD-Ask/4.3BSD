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
（2026-10-24 已按原书词汇表（印刷 413–450）全量校准：词汇表 482 个词条全部登记，并保留正文补充词条与专名表；core map 等待复核条目已按词汇表定义定稿。）

| 英文 | 中文 | 备注 |
| ---- | ---- | ---- |
| 2MSL timer | 2MSL 计时器 | TCP TIME_WAIT 状态 |
| 4.2BSD fast filesystem | 快速文件系统 | FFS |
| absolute pathname | 绝对路径名 | 见 pathname（路径名） |
| access method | 访问方法 | |
| access rights | 访问权限 | 4.3BSD IPC 支持随报文传递访问权 |
| accounting | 记账 | 系统记账（system accounting） |
| adb | — | 调试器名保留 |
| address family | 地址族 | |
| address format | 地址格式 | |
| Address Resolution Protocol (ARP) | 地址解析协议（ARP） | 网络地址间的动态映射，如 DARPA Internet 地址映射为以太网地址 |
| address space | 地址空间 | |
| address translation | 地址转换 | 多由硬件实现 |
| address-translation cache | 地址转换高速缓存 | |
| advisory lock | 劝告锁 | 仅显式请求才强制，与强制锁相对 |
| AGE buffer list | AGE 缓冲区链表 | 存放内容尚未证明有用的缓冲区（如预读块） |
| ARP | 地址解析协议（ARP） | 见 Address Resolution Protocol |
| ARPANET | — | 专名保留 |
| ARPANET Host Access Protocol | ARPANET 主机访问协议 | 主机与 ARPANET PSN 间通信所用协议 |
| assembler | 汇编器 | |
| association | 关联 | 12.1 节，端口与地址的关联 |
| Association for Computing Machinery (ACM) | （美国）计算机协会（ACM） | 图灵奖颁发机构 |
| AST | 异步系统陷阱（AST） | |
| asynchronous | 异步 | |
| asynchronous system trap (AST) | 异步系统陷阱（AST） | |
| attach routine | 附接例程 | 设备自动配置阶段 |
| autoconfiguration | 自动配置 | |
| autoconfiguration phase | 自动配置阶段 | |
| background process | 后台进程 | |
| backing storage | 后备存储 | 即 backing store；调页与交换时存放被换出对象，见 secondary storage |
| backward compatibility | 向后兼容 | |
| bad sector | 坏扇区 | |
| bad-sector forwarding | 坏扇区转发 | |
| bad-sector table | 坏扇区表 | |
| basename | 基名 | basename.extension 文件名惯例 |
| baud rate | 波特率 | |
| Berkeley Software Distribution (BSD) | 伯克利软件发行版（BSD） | BSD 之名由此来 |
| Berknet | — | Berkeley 早期网络软件名保留 |
| beta test | beta 测试 | |
| block（存储） | 块 | 磁盘/文件系统块 |
| block（等待） | 阻塞 | 进程状态；按义项区分 |
| block device | 块设备 | |
| block-device interface | 块设备接口 | |
| block-device table | 块设备表 | |
| block I/O | 块 I/O | 对块设备的 I/O |
| block size | 块大小 | |
| block special file | 块特殊文件 | |
| bootdevice register | 引导设备寄存器 | |
| boothowto register | 引导方式寄存器 | |
| bootstrap | 自举 | 百度百科“自举引导”；FreeBSD 手册亦用“引导”，两词同义时统一“自举” |
| bootstrapping | 自举 | |
| bottom half | 下半部 | 因中断而调用的内核例程集合，不能睡眠；与上半部相对 |
| breakpoint fault | 断点故障 | |
| broadcast | 广播 | |
| bss segment | bss 段 | 未初始化数据段 |
| buffer | 缓冲区 | |
| buffer cache | 缓冲区高速缓存 | |
| buffered | 缓冲的 | |
| buffered data path | 缓冲数据通路 | |
| bus | 总线 | |
| bus adapter | 总线适配器 | |
| byte | 字节 | |
| cache | 高速缓存 | |
| canonical mode | 规范模式 | 终端行规程模式 |
| capability | 权能 | 呈现给系统以获取对象访问权的数据 |
| carrier | 载波 | modem 控制语境 |
| catenet | — | 异构网络经网关互连的形态；DARPA Internet 即一例，保留 |
| cathode ray tube | 阴极射线管 | |
| caught signal | 已捕获信号 | |
| C-block | C 块 | C-list 的组成单元 |
| cbreak mode | cbreak 模式 | 介于规范模式与原始模式之间 |
| central processing unit | 中央处理器 | |
| character | 字符 | |
| character device | 字符设备 | |
| character-device interface | 字符设备接口 | |
| character-device table | 字符设备表 | |
| checksum | 校验和 | |
| child process | 子进程 | |
| client | 客户端 | 客户-服务器模型；client process 译客户进程 |
| client process | 客户进程 | 客户-服务器模型中请求服务的一方 |
| C-list | C 链表（C-list） | 终端字符链表，正文可保留 C-list |
| CLOCK algorithm | CLOCK 算法 | 见 global CLOCK algorithm |
| clock hand | 时钟指针 | CLOCK 置换算法的扫描指针 |
| clock interrupt | 时钟中断 | |
| cluster（存储管理） | 簇 | 相邻物理页成组，用于模拟大于硬件页面的页 |
| cold start | 冷启动 | |
| command interpreter | 命令解释器 | |
| communication domain | 通信域 | 即 domain（通信域） |
| communication protocol | 通信协议 | |
| compiler | 编译器 | |
| Computer Systems Research Group (CSRG) | 计算机系统研究组（CSRG） | 伯克利 BSD 开发团队 |
| configuration file | 配置文件 | |
| configuration procedure | 配置过程 | |
| congestion | 拥塞 | |
| congestion control | 拥塞控制 | |
| connection | 连接 | |
| connect request | 连接请求 | |
| console | 控制台 | |
| console monitor | 控制台终端 | 连接在控制台终端接口上的终端 |
| console processor | 控制台处理机 | VAX 控制台 LSI-11 |
| context | 上下文 | |
| context switching | 上下文切换 | |
| continue signal | 继续信号 | |
| control block | 控制块 | |
| controlling terminal | 控制终端 | |
| control request | 控制请求 | |
| cooked mode | 规范模式（cooked） | 终端默认模式：整行处理后才交付输入，与原始模式、cbreak 模式并列；即 canonical mode |
| copy-on-write | 写时复制 | |
| core dump | 核心转储 | 见 core file、crash dump |
| core file | core 文件 | 进程收到特定信号时系统生成的状态记录文件，名为 core |
| core map | 核心映射表 | 核心映射表（cmap）；词汇表定义：内核管理主存的数据结构，主存每簇一项 |
| coroutine | 协程 | |
| CPU | 中央处理器（CPU） | 见 central processing unit |
| crash | 崩溃 | 系统意外失效 |
| crash dump | 崩溃转储 | 崩溃时刻机器状态的记录 |
| critical section | 临界区 | |
| CRT | 阴极射线管（CRT） | |
| current working directory | 当前工作目录 | |
| cylinder | 柱面 | |
| cylinder group | 柱面组 | FFS |
| daemon | 守护进程 | 有内核态（如 pagedaemon）与用户态（如 routed）之分 |
| datagram | 数据报 | |
| datagram socket | 数据报套接字 | |
| data path | 数据通路 | |
| data segment | 数据段 | 进程中存放程序初始化与未初始化数据的部分 |
| data structure | 数据结构 | |
| dbx | — | 调试器名保留 |
| debugging | 调试 | |
| decapsulation | 解封装 | |
| demand paging | 请求调页 | 教材通行译法 |
| demultiplex / demultiplexing | 解复用 | 与多路复用相对 |
| deprecated | 已弃用 | |
| descriptor | 描述符 | open 或 socket、pipe 等创建时系统返回的整数 |
| descriptor table | 描述符表 | 每进程一张；又称进程打开文件表 |
| device | 设备 | |
| device driver | 设备驱动（程序） | |
| device flags | 设备标志 | 配置文件中指定并传给设备驱动的数据 |
| device number | 设备号 | 主/次设备号合成的编码 |
| device special file | 设备特殊文件 | 进程借此访问硬件设备 |
| directed broadcast | 定向广播 | |
| direct memory access (DMA) | 直接存储器访问（DMA） | 外设不经 CPU 直接访问主存 |
| directory | 目录 | |
| directory entry | 目录项 | 变长记录，含文件名与 inode 号 |
| dirty | 脏 | 页内容已修改待写回 |
| disk | 磁盘 | |
| disk partition | 磁盘分区 | |
| disk quota | 磁盘配额 | |
| distributed program | 分布式程序 | |
| distributed system | 分布式系统 | |
| DMA | 直接存储器访问（DMA） | 见 direct memory access |
| domain（通信） | 通信域 | socket domain |
| double (doubly) linked list | 双向链表 | |
| double indirect block | 二级间接块 | |
| Draft International Standard | 国际标准草案 | ISO DIS |
| ECC correction | ECC 纠错 | |
| effective GID | 有效组标识符 | 见 effective group identifier |
| effective group identifier (effective GID) | 有效组标识符 | 执行 setgid 程序时设置；用于文件系统组权限检查 |
| effective UID | 有效用户标识符 | 见 effective user identifier |
| effective user identifier (effective UID) | 有效用户标识符 | 执行 setuid 程序时设置；用于多数用户权限检查 |
| elevator sorting algorithm | 电梯排序算法 | disksort 使用的磁盘调度 |
| emulate | 仿真 | |
| encapsulation | 封装 | |
| environment | 环境 | |
| erase character | 擦除字符 | 行规程的行内删除键 |
| errno | — | 错误码变量名保留 |
| error-message buffer | 消息缓冲区 | 见 message buffer；内核消息环形缓冲区 |
| Ethernet | 以太网 | |
| fan-in / fan-out | 扇入／扇出 | |
| fault | 故障 | page fault 译“缺页” |
| fault rate | 缺页率 | |
| Federal Information Processing Standard (FIPS) | 联邦信息处理标准（FIPS） | NBS 发布 |
| fetch policy | 取页策略 | 何时取页调入内存 |
| ffs | 快速文件系统（FFS） | |
| field | 字段 | |
| FIFO | 命名管道（FIFO） | 先进先出的进程间通信文件 |
| file | 文件 | |
| file descriptor | 文件描述符 | 即 descriptor（描述符） |
| filename | 文件名 | |
| file offset | 文件偏移量 | |
| file structure | file 结构 | 内核中记录打开文件描述符信息的结构体 |
| filesystem | 文件系统 | |
| fill-on-demand | 按需填充 | |
| fill-on-demand klustering | 按需填充成组 | 缺页时连同相邻页一并调入的预调页手段 |
| fill-on-demand page fault | 按需填充缺页 | 某页的首次缺页，须读文件系统或分配零页解决 |
| fill-on-demand page-table entry | 按需填充页表项 | 引用即产生按需填充缺页的 PTE |
| finite-state machine | 有限状态机 | |
| first-level bootstrap | 第一级自举 | |
| flags | 标志 | |
| flush | 刷新 | |
| foreground | 前台 | |
| foreground process | 前台进程 | |
| fork | — | 系统调用名保留 |
| fragment | 片 | FFS 块内分段 |
| fragment-descriptor table | 片描述符表 | FFS 片分配 |
| free list | 空闲表 | 存储管理中可用物理内存簇的列表（memory free list） |
| free-space reserve | 空闲空间保留 | FFS minfree，缺省 10% |
| garbage collection | 垃圾收集 | |
| gateway | 网关 | 原书时代的 router 多称 gateway，照原书用词 |
| GID | 组标识符（GID） | 见 group identifier |
| global CLOCK algorithm | 全局 CLOCK 算法 | 4.3BSD 采用前后双指针（clock hand）变体 |
| go routine | go 例程 | UNIBUS 驱动中启动 I/O 的例程 |
| group identifier (GID) | 组标识符（GID） | 16 位整数，唯一标识一组用户 |
| half-open | 半打开 | 仅一端认为连接仍打开 |
| handler | 处理例程 | 响应事件（如信号）的过程；按语境亦可作处理程序 |
| hard limit | 硬限制 | 不可超越；与软限制相对 |
| hard link | 硬链接 | |
| hard lock | 强制锁 | |
| Harvard University | 哈佛大学 | |
| hash | 哈希 | |
| heap | 堆 | |
| high watermark | 高水位线 | |
| hole | 空洞 | 文件内无数据块的区间，读出为零 |
| home directory | 主目录 | |
| host | 主机 | |
| Host Dead message | 主机失效报文 | ARPANET/ICMP 报文 |
| host identifier | 主机标识符 | sethostid 设置的 32 位值，用于构造全网唯一标识 |
| Host Unreachable message | 主机不可达报文 | |
| ICMP | 网际控制报文协议（ICMP） | |
| IDP | 网际数据报协议（IDP） | XNS |
| IMP | 接口报文处理机（IMP） | ARPANET 交换机 |
| indirect block | 间接块 | |
| init | — | 1 号进程/命令名保留 |
| initialization | 初始化 | |
| initial sequence number | 初始序号 | TCP ISN |
| inode | 索引节点 | 文件系统描述文件的数据结构；inode 本身无名字，由目录项关联名字 |
| inode table | 索引节点表 | 存放活动 inode，常驻内存，按 LRU 复用 |
| Input/Output (I/O) | 输入/输出（I/O） | |
| intelligent gateway | 智能网关 | |
| interactive program | 交互式程序 | |
| interface | 接口 | |
| Interface Message Processor (IMP) | 接口报文处理机（IMP） | |
| International Organization for Standardization (ISO) | 国际标准化组织（ISO） | |
| Internet（DARPA Internet） | Internet | 专名保留；泛指互联网时译“互联网” |
| Internet Control Message Protocol (ICMP) | 网际控制报文协议（ICMP） | |
| internet domain | 网际域 | 支持 DARPA Internet 体系结构的通信域 |
| internet host address | 网际主机地址 | 32 位，同时标识网络与主机 |
| Internet Protocol (IP) | 网际协议（IP） | |
| internetwork | 互连网 | 视上下文；谢希仁《计算机网络》译法，与 Internet 专名区分 |
| Internetwork Datagram Protocol (IDP) | 网际数据报协议（IDP） | XNS |
| interprocess communication (IPC) | 进程间通信（IPC） | 4.3BSD 中通信在套接字之间而非进程之间进行 |
| interrupt | 中断 | |
| interrupt handler | 中断处理程序 | |
| interrupt priority level | 中断优先级（IPL） | 由设备控制器上的开关或跳线设定 |
| interrupt stack | 中断栈 | 系统级运行时栈，独立于各进程的内核栈 |
| interrupt vector | 中断向量 | |
| interrupt-vector table | 中断向量表 | |
| I/O | 输入/输出（I/O） | 见 Input/Output |
| ioctl | — | 系统调用名保留 |
| I/O page | I/O 页 | 地址空间中可访问 I/O 设备控制寄存器的区段；VAX 上为每个 UNIBUS 适配器地址空间的末 8 KB |
| I/O redirection | I/O 重定向 | |
| I/O stream | I/O 流 | |
| iovec | — | 结构体名保留 |
| I/O vector | I/O 向量 | |
| IP | 网际协议（IP） | |
| IPC | 进程间通信（IPC） | 见 interprocess communication |
| job | 作业 | 同一进程组标识符的全部进程；作业控制的基本对象 |
| job control | 作业控制 | |
| keepalive packet | 保活报文 | |
| keepalive timer | 保活计时器 | |
| kernel | 内核 | |
| kernel map | 内核映射表 | 分配映射用户进程地址空间的 PTE 所用的资源映射 |
| kernel mode | 内核态 | 最特权的处理机访问模式 |
| kernel organization | 内核结构 | 4.4BSD 官方中译本第 2 章译法 |
| kernel process | 内核进程 | 处理机处于内核态执行的进程，如 pagedaemon、swapper |
| kernel state | 内核状态 | 含程序计数器、通用寄存器与运行时栈，每次上下文切换须保存恢复 |
| kill | — | 命令/信号名保留 |
| kill character | kill 字符 | 规范模式下删除本行自上一行结束符以来全部输入的字符 |
| kluster / klustering | — | 4.3BSD 特有 K 拼写（原书 5.11 节 “No more than 16 klusters”），保留原文并加译注；词汇表定义：按局部性相关的页组，拼作 K 以与页成簇（cluster）区分 |
| ldpctx | — | VAX 指令：装载进程上下文，保留 |
| least recently used (LRU) | 最近最久未使用（LRU） | |
| line discipline | 行规程 | Linux 内核文档中文社区与 dog250 经典文章通行 |
| line mode | 行模式 | 见 cooked mode（规范模式） |
| link | 链接 | |
| linked list | 链表 | |
| link layer | 链路层 | |
| listen request | 监听请求 | |
| load average | 平均负载 | 就绪与等待磁盘 I/O 进程数的 1 分钟均值 |
| locality | 局部性 | |
| locality of reference | 引用局部性 | |
| local network | 本地网络 | |
| lock | 锁 | |
| logical block | 逻辑块 | 文件线性长度按文件系统块大小划分得到的块 |
| logical drive partitions | 逻辑驱动器分区 | |
| logical unit | 逻辑单元 | 自动配置发现的逻辑部件号 |
| login | 登录 | /bin/login 保留路径 |
| login shell | 登录 shell | |
| long-haul network | 远程网络 | |
| long-term–scheduling algorithm | 长期调度算法 | |
| loop | 页环 | 存储管理中由全局 CLOCK 算法管理的常驻页集合 |
| lossy | 易丢包的 | |
| low watermark | 低水位线 | |
| machine check | 机器检查 | VAX 硬件错误；与 checksum（校验和）区分 |
| machine-dependent | 与机器相关的 | |
| machine-independent | 与机器无关的 | |
| magic number | 魔数 | |
| mailing list | 邮件列表 | |
| main memory | 主存 | |
| major-device number | 主设备号 | |
| mapped | 已映射的 | |
| mapping | 映射 | |
| mark and sweep algorithm | 标记-清除算法 | 垃圾收集通行译法 |
| masked | 屏蔽的 | 信号屏蔽 |
| MASSBUS adapter | MASSBUS 适配器 | |
| MASSBUS-adapter support routines | MASSBUS 适配器支持例程 | |
| MASSBUS unit number | MASSBUS 部件号 | |
| master copy | 主副本 | |
| master device | 主设备 | |
| maximum segment lifetime (MSL) | 最长报文段生存期（MSL） | |
| mbuf | — | 内存缓冲区，保留 mbuf |
| memory | 存储器／内存 | 按语境：主存实体用“内存”，抽象层次用“存储器” |
| memory address | 内存地址 | 分物理地址与虚拟地址两类 |
| memory allocator | 内存分配器 | |
| memory free list | 空闲表 | 见 free list |
| memory management | 存储管理 | 4.4BSD 官方中译本第 5 章标题 |
| memory-management system | 存储管理系统 | |
| memory-management unit | 存储管理单元 | MMU |
| memory-mapped I/O architecture | 存储映射 I/O 体系结构 | |
| message | 消息 | |
| message buffer | 消息缓冲区 | 记录全部内核消息的环形缓冲区，可经 /dev/klog 读取 |
| minor-device number | 次设备号 | |
| mode | 模式 | |
| modem | 调制解调器 | |
| modem control | 调制解调器控制 | RS-232 异步串行线路上可靠建立与拆除连接的信号支持 |
| moderated newsgroup | 仲裁新闻组 | |
| mount / unmount | 挂载／卸载 | 社区通行；旧教材“安装/拆卸”不采用 |
| MSL | 最长报文段生存期（MSL） | |
| multilevel feedback queue | 多级反馈队列 | 4.3BSD 调度算法 |
| multiplexed file | 多路复用文件 | 第七版 UNIX 的 IPC 文件类型 |
| multiplexing | 多路复用 | |
| multiprogramming | 多道程序设计 | |
| National Bureau of Standards (NBS) | 美国国家标准局（NBS） | 后更名 NIST |
| network | 网络 | |
| network address | 网络地址 | |
| network architecture | 网络体系结构 | |
| network byte order | 网络字节序 | |
| network interface | 网络接口 | |
| network-interface layer | 网络接口层 | |
| network layer | 网络层 | |
| network mask | 网络掩码 | |
| network virtual terminal | 网络虚拟终端 | 跨网络连接收发数据的终端设备 |
| new terminal driver | 新终端驱动 | 4.3BSD termios 驱动 |
| nexus | — | VAX 主系统总线的物理连接点，保留 |
| nice | — | nice 值保留 |
| nonblocking I/O | 非阻塞 I/O | |
| nonlocal goto | 非局部跳转 | |
| nonresident | 非驻留 | |
| octet | 八位组 | |
| old terminal driver | 旧终端驱动 | V7 风格 tty 驱动 |
| open file table | 打开文件表 | |
| operating system | 操作系统 | |
| Optimal Replacement Policy | 最优置换算法 | OPT，理论基准 |
| out-of-band data | 带外数据 | |
| overlay | 覆盖 | |
| owner | 属主 | |
| P0 base register (P0BR) | P0 基址寄存器（P0BR） | VAX |
| P0BR | P0 基址寄存器（P0BR） | |
| P0 length register (P0LR) | P0 长度寄存器（P0LR） | |
| P0LR | P0 长度寄存器（P0LR） | |
| P1 base register (P1BR) | P1 基址寄存器（P1BR） | |
| P1BR | P1 基址寄存器（P1BR） | |
| P1 length register (P1LR) | P1 长度寄存器（P1LR） | |
| P1LR | P1 长度寄存器（P1LR） | |
| Packet Exchange (PEX) | 分组交换协议（PEX） | XNS |
| Packet Switch Node (PSN) | 分组交换节点（PSN） | ARPANET |
| page | 页 | 划分物理或虚拟地址空间的定长单位 |
| pagedaemon | 调页守护进程 | 4.3BSD 中负责将进程地址空间写往辅存以支持调页的进程 |
| page fault | 缺页 | |
| page frame | 页框 | |
| pagein | 页面换入 | 5.11 节 Pagein of Swapped Pages |
| pageout | 页面换出 | |
| pageout in progress | 页面换出进行中 | |
| page push | 页面推出 | 脏页的页面换出 |
| page reclaim | 页面回收 | 缺页时所需页尚在内存（如空闲表） |
| page replacement | 页面置换 | |
| page table | 页表 | |
| page-table entry (PTE) | 页表项（PTE） | 标识虚拟地址空间中一页的位置与状态 |
| paging | 调页 | 页被引用时调入，被置换时移出 |
| panic | 恐慌 | 内核检测到的不可恢复故障，4.3BSD 自动重启恢复 |
| parent process | 父进程 | |
| parity checking | 奇偶校验 | |
| partition | 分区 | |
| pathname | 路径名 | 以斜杠分隔的字符串；行首斜杠为绝对路径名，否则为相对路径名 |
| PCB | 进程控制块（PCB） | 见 process control block（进程控制块）；与协议控制块按语境区分 |
| PCBB | 进程控制块基址（PCBB） | VAX |
| permission | 权限 | |
| persist timer | 持续计时器 | TCP 零窗口探测 |
| PEX | 分组交换协议（PEX） | |
| physical address | 物理地址 | |
| physical block | 物理块 | 逻辑块映射到的一个或多个连续磁盘扇区 |
| physical unit number | 物理部件号 | |
| PID | 进程标识符（PID） | 见 process identifier |
| pipe | 管道 | 相关进程间的单向数据流 |
| pipeline | 管道线 | 以管道连接的进程链：一进程的标准输出接下一进程的标准输入 |
| placement policy | 放置策略 | 调入的页放到何处 |
| pointer | 指针 | |
| port（网络） | 端口 | |
| port / porting（移植） | 移植 | 与“端口”按义项区分 |
| POSIX | 可移植操作系统接口（POSIX） | |
| post a signal | 发送信号 | |
| preemption | 抢占 | |
| prefetching | 预取 | |
| prepaging | 预调页 | |
| priority | 优先级 | |
| privileged instruction | 特权指令 | |
| probe routine | 探测例程 | 自动配置阶段检测设备存在 |
| probing | 探测 | |
| process | 进程 | |
| Process Control Block Base (PCBB) | 进程控制块基址（PCBB） | |
| process control block (PCB) | 进程控制块 | VAX 上含硬件 PCB 与紧随其后的软件 PCB；与协议控制块按语境区分 |
| process group | 进程组 | |
| process-group identifier | 进程组标识符 | |
| process-group leader | 进程组长 | |
| process identifier (PID) | 进程标识符（PID） | 非负整数，唯一标识活动进程；亦作 process ID |
| process open file table | 进程打开文件表 | 见 descriptor table（描述符表） |
| processor priority level | 处理机优先级 | |
| Processor Status Longword (PSL) | 处理机状态长字（PSL） | VAX |
| process priority | 进程优先级 | |
| process table | 进程表 | 描述全部活动进程的 proc 结构集合，常驻内存 |
| /proc filesystem | /proc 文件系统 | 以文件系统接口访问活动进程，用于构造进程调试设施；第八版 UNIX 引入 |
| proc structure | proc 结构 | 结构体名保留 |
| profiling | 剖析 | 计时剖析 |
| protocol | 协议 | |
| protocol control block（PCB） | 协议控制块 | 与进程控制块按语境区分 |
| protocol family | 协议族 | |
| protocol switch structure | 协议开关结构 | `protosw` |
| pseudo-device | 伪设备 | |
| pseudo-DMA | 伪 DMA | 主处理机代行 DMA 传输 |
| PSL | 处理机状态长字（PSL） | |
| PSN | 分组交换节点（PSN） | |
| PTE | 页表项（PTE） | 见 page-table entry |
| Purdue University | 普渡大学 | |
| pure demand paging | 纯请求调页 | |
| queue | 队列 | |
| queue limiting | 队列限长 | 11.6 节 |
| quota | 配额 | |
| Rand Corporation | 兰德公司 | |
| raster plotter | 光栅绘图仪 | |
| raw device | 裸设备 | |
| raw-device interface | 裸设备接口 | |
| raw I/O | 裸 I/O | |
| raw mode | 原始模式 | 输入即收、不加解释的终端模式 |
| raw socket | 原始套接字 | 直接访问低层通信协议的套接字 |
| raw-socket interface | 裸套接字接口 | |
| Ready for Next Message (RFNM) | 就绪接收下一报文（RFNM） | ARPANET 流控 |
| real GID | 实际组标识符 | |
| real group identifier (real GID) | 实际组标识符 | |
| real UID | 实际用户标识符 | |
| real user identifier (real UID) | 实际用户标识符 | |
| receive window | 接收窗口 | |
| reclaim | 回收 | |
| reclaim from free | 从空闲表回收 | |
| red zone | 红区 | 内核栈末页下方的只读警戒区，越界即触发故障 |
| reentrant | 可重入 | |
| reference bit | 引用位 | PTE 中的访问位 |
| referenced | 已引用的 | |
| reference string | 引用串 | |
| register save mask | 寄存器保存掩码 | VAX 调用约定 |
| relative pathname | 相对路径名 | 见 pathname |
| release engineering | 发布工程 | |
| reliably delivered message socket | 可靠投递报文套接字 | SOCK_SEQPACKET 之前身 |
| relocation | 重定位 | |
| replacement algorithm | 置换算法 | |
| replacement policy | 置换策略 | |
| resident | 驻留 | |
| resource | 资源 | |
| resource limit | 资源限制 | |
| resource map | 资源映射表 | 管理可用线性区间描述的资源分配 |
| retransmission | 重传 | |
| retransmit timer | 重传计时器 | |
| RFNM | 就绪接收下一报文（RFNM） | |
| root directory | 根目录 | |
| root filesystem | 根文件系统 | |
| rotational-layout table | 旋转布局表 | FFS 磁盘布局参数 |
| round robin | 轮转 | |
| round-trip time（RTT） | 往返时间（RTT） | |
| route | 路由 | 到某目的地须经哪些主机转发 |
| routing | 路由 | route 的动名词义项 |
| routing daemon | 路由守护进程 | 即 routed；维护动态更新的路由信息分布式数据库 |
| routing redirect message | 路由重定向报文 | 网关发现更直接路径时发出的报文；亦作 routing redirect |
| routing table | 路由表 | |
| run queue | 运行队列 | |
| SBR | 系统基址寄存器（SBR） | |
| scatter/gather I/O | 分散/聚集 I/O | 正文补充词条（词汇表无此条目），通行译法 |
| scatter loading | 分散装载 | |
| scheduling | 调度 | |
| scheduling priority | 调度优先级 | 进程在用户态执行时，内核按进程优先级与 nice 值周期性重算 |
| secondary storage | 辅存 | 亦可“二级存储器” |
| sector | 扇区 | |
| seek | 寻道 | |
| segment | 段 | 存储管理中指连续地址区间；TCP 中指连续序号区间及其关联数据 |
| select | — | 系统调用名保留 |
| semaphore | 信号量 | |
| send window | 发送窗口 | |
| sense request | 状态请求 | 进程在套接字上执行 stat 系统调用后传入用户请求例程的请求 |
| Sequenced Packet Protocol (SPP) | 顺序分组协议（SPP） | XNS |
| sequenced packet socket | 顺序分组套接字 | |
| sequence space | 序号空间 | TCP |
| Serial Line IP (SLIP) | 串行线路 IP（SLIP） | |
| server process | 服务器进程 | |
| session | 会话 | 作业控制中单次登录启动的全部进程 |
| set-group-identifier program | 设置组标识符程序 | setgid 程序 |
| set-priority-level | 设置优先级 | 经 `spl` 前缀例程（如 `spltty()`）设置处理机优先级 |
| set-user-identifier program | 设置用户标识符程序 | setuid 程序 |
| shadow swap map | 影子交换映射 | 位于每个进程 user 结构中，在进程持有既有交换空间期间临时记录新分配的交换空间 |
| shared text | 共享正文段 | 即 shared text segment 的行文用词 |
| shared text segment | 共享正文段 | 多个进程共享的正文段，由魔数识别 |
| shell | — | 不译 |
| short-term–scheduling algorithm | 短期调度算法 | |
| signal | 信号 | 软件事件，4.3BSD 中仿照硬件中断建模 |
| signal delivery | 信号递送 | |
| signal-driven I/O | 信号驱动 I/O | |
| signal handler | 信号处理程序 | 响应信号的过程，经 sigvec 安装 |
| signal posting | 信号发送 | |
| signal-trampoline code | 信号蹦床代码 | `sigtramp` |
| silly-window syndrome | 糊涂窗口综合症 | |
| silly window syndrome（SWS） | 糊涂窗口综合症 | 中文维基百科、百度百科通行译法 |
| single indirect block | 一级间接块 | |
| single-user mode | 单用户模式 | |
| slave device | 从设备 | |
| slave routine | 从例程 | |
| sleep queue | 睡眠队列 | |
| sliding-window scheme | 滑动窗口机制 | |
| SLIP | 串行线路 IP（SLIP） | |
| slip sector | 滑移扇区 | 用于替换同一磁道上坏扇区的扇区 |
| slip-sector forwarding | 滑移扇区转发 | |
| slow start | 慢启动 | |
| SLR | 系统长度寄存器（SLR） | |
| small-packet avoidance | 小报文避免 | TCP 避免发送过小报文段 |
| socket | 套接字 | 教材通行译法 |
| socket address | 套接字地址 | |
| soft limit | 软限制 | 可临时超越；与硬限制相对 |
| soft link | 符号链接 | 即 symbolic link |
| software interrupt | 软件中断 | VAX 支持 15 级，经 SIRR 寄存器请求 |
| software-interrupt process | 软件中断进程 | |
| source-code control | 源码控制 | |
| sparse address space | 稀疏地址空间 | |
| special file | 特殊文件 | 见 device special file（设备特殊文件） |
| spin loop | 自旋循环 | |
| SPP | 顺序分组协议（SPP） | |
| stack | 栈 | 后进先出的暂存区；VAX 上由高地址向低地址生长 |
| stack segment | 栈段 | |
| stale translation | 失效转换 | TLB 中过期的地址转换项 |
| standalone | 独立运行 | 脱离操作系统直接运行 |
| standalone device driver | 独立设备驱动 | 自举环境用 |
| standalone I/O library | 独立 I/O 库 | 自举环境用 |
| standard error | 标准错误 | |
| standard input | 标准输入 | |
| standard output | 标准输出 | |
| start routine | 启动例程 | |
| start-up script | 启动脚本 | |
| state | 状态 | |
| steering committee | 指导委员会 | |
| sticky bit | 粘滞位 | inode 中指示正文段按粘滞正文处理的位 |
| sticky text | 粘滞正文 | 保存在交换区以便复用的正文段 |
| storage | 存储 | |
| stream I/O system | 流 I/O 系统 | |
| stream socket | 流套接字 | SOCK_STREAM |
| structure | 结构体 | C 语境 |
| structured device | 有结构设备 | 即块设备；与无结构设备相对 |
| stub | 桩 | 汇编语言桩 |
| subnetwork | 子网 | |
| superblock | 超级块 | |
| superuser | 超级用户 | UID 为 0 的用户，登录名通常为 `root` |
| svpctx | — | VAX 指令：保存进程上下文，保留 |
| swap | 交换 | |
| swap area | 交换区 | |
| swap device | 交换设备 | 交换区所在的设备 |
| swapin / swapout | 换入／换出 | |
| swap map | 交换映射表 | 描述交换区可用空间的数据结构 |
| swapping | 交换 | 教材另有“对换”，本表统一“交换” |
| swapping process（swapper） | 交换进程 | 0 号进程 |
| swap space | 交换空间 | 词汇表作 swap area（交换区）的同义词；FreeBSD 中文使用手册译法 |
| symbolic link | 符号链接 | |
| synchronization | 同步 | |
| synchronous | 同步 | |
| system activity | 系统活动 | |
| system base register (SBR) | 系统基址寄存器（SBR） | |
| system bus | 系统总线 | |
| system call | 系统调用 | |
| system clock | 系统时钟 | 周期性中断 CPU 的间隔计时器，维护时间并执行周期性功能 |
| system identification register | 系统标识寄存器 | VAX SID |
| system length register (SLR) | 系统长度寄存器（SLR） | |
| system mode | 系统态 | 见 kernel mode（内核态） |
| system page table | 系统页表 | 映射内核虚拟地址空间的页表 |
| system region | 系统区 | VAX 系统地址空间区域 |
| tape | 磁带 | |
| TCP | 传输控制协议（TCP） | |
| terminal | 终端 | |
| terminal multiplexer | 终端多路复用器 | DZ-11 等 |
| text segment | 正文段 | 存放机器指令的段，通常只读且可共享 |
| text structure | 正文结构 | 内核管理共享正文段的数据结构 |
| thrashing | 抖动 | 内存需求远超可用内存，系统忙于系统任务而无暇执行应用代码 |
| tick | 时钟节拍 | |
| tightly coupled system | 紧耦合系统 | |
| timeout | 超时 | |
| time quantum | 时间量 | 即时间片 |
| timer | 计时器 | |
| timer backoff | 计时器退避 | TCP 重传超时倍增 |
| timesharing | 分时 | |
| time slice | 时间片 | |
| TLB | 转换检测缓冲区（TLB） | |
| token ring | 令牌环 | |
| top half | 上半部 | 因系统调用或陷阱同步调用的内核例程集合，可以睡眠；与下半部相对 |
| trace trap | 跟踪陷阱 | ptrace 断点 |
| track | 磁道 | |
| trailer protocol | 尾部协议 | 控制信息置于数据之后的协议，Ethernet 上用于页对齐接收 |
| translation lookaside buffer | 转换检测缓冲区（TLB） | |
| translation-not-valid fault | 转换无效故障 | |
| Transmission Control Protocol | 传输控制协议（TCP） | |
| transport layer | 传输层 | |
| trap | 陷阱 | |
| triple indirect block | 三级间接块 | |
| tty | — | 保留 tty |
| tty driver | tty 驱动 | 实现终端设备语义的软件模块，由若干行规程构成 |
| Turing Award | 图灵奖 | ACM |
| type-ahead | 预键入 | 终端输入的提前缓冲 |
| u-dot | u. 结构 | 即 user 结构 |
| UDP | 用户数据报协议（UDP） | 见 User Datagram Protocol |
| UID | 用户标识符（UID） | 见 user identifier |
| uio | — | 描述 I/O 操作的结构体名保留 |
| unbuffered data path | 非缓冲数据通路 | |
| UNIBUS adapter | UNIBUS 适配器 | |
| UNIBUS / MASSBUS | — | VAX 总线名保留；UNIBUS 用于中低速外设，MASSBUS 用于高速大容量存储外设 |
| unit start routine | 部件启动例程 | |
| University of Illinois | 伊利诺伊大学 | |
| UNIX domain | UNIX 域 | 本地通信协议族 |
| UNIX Support Group (USG) | UNIX 支持组（USG） | AT&T 内部 |
| unstructured device | 无结构设备 | 即字符设备 |
| urgent data | 紧急数据 | TCP 紧急指针/带外数据 |
| user area | 用户区 | 即 user 结构 |
| User Datagram Protocol (UDP) | 用户数据报协议（UDP） | DARPA Internet 的简单不可靠数据报协议 |
| user identifier (UID) | 用户标识符（UID） | 16 位非负整数，唯一标识用户 |
| user mode | 用户态 | 特权最低的处理机访问模式 |
| user page table | 用户页表 | 映射进程虚拟地址空间；位于内核虚拟地址空间中 |
| user-request routine | 用户请求例程 | `protosw` 的 `pr_usrreq` |
| user structure | user 结构 | 每活动进程一份；进程换出时移往辅存；又称 u. 区、user 区 |
| utility | 实用程序 | |
| VAX | — | 机型名保留 |
| VAX architecture | VAX 体系结构 | |
| VAX system | VAX 系统 | VAX 体系结构的一种具体实现 |
| vectored interrupt | 向量中断 | |
| virtual address | 虚拟地址 | |
| virtual address space | 虚拟地址空间 | |
| virtual machine | 虚拟机 | |
| virtual memory | 虚拟存储 | 4.4BSD 中译本语系 |
| wait | — | 系统调用名保留 |
| wait channel | 等待通道 | 标识进程所等事件的值（常为相关结构地址） |
| wildcard route | 通配路由 | |
| window | 窗口 | TCP 语境 |
| window probe | 窗口探测报文 | TCP 零窗口探测 |
| word-erase character | 字擦除字符 | 行规程的词删除键 |
| working directory | 工作目录 | 见 current working directory（当前工作目录） |
| working set | 工作集 | 一段时间内被引用过的页的集合 |
| workstation | 工作站 | |
| XNS domain | XNS 域 | 施乐网络系统通信域 |
| X/OPEN Portability Guide | 《X/OPEN 可移植性指南》 | |
| zombie process | 僵尸进程 | |

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
| Özalp Babaoğlu | 按需填充成组（fill-on-demand klustering）论文作者之一 |
| Rob Pike、Brian Kernighan 等 | 后续章节出现时补录 |

## 公司/机构表

| 英文 | 中文 | 备注 |
| ---- | ---- | ---- |
| Addison-Wesley | 艾迪生-韦斯利 | 出版社 |
| AT&T | — | 保留 |
| Bell Laboratories / Bell Labs | 贝尔实验室 | |
| Carnegie-Mellon University | 卡内基-梅隆大学 | |
| DARPA | 美国国防高级研究计划局 | 正文中 DARPA Internet 保留专名 |
| DEC（Digital Equipment Corporation） | — | 保留 DEC；需要全称时译“数字设备公司” |
| Hewlett-Packard | 惠普 | |
| IBM | — | 保留 |
| International Computer Science Institute (ICSI) | 国际计算机科学研究所（ICSI） | |
| Massachusetts Institute of Technology（MIT） | 麻省理工学院 | |
| McGraw-Hill | 麦格劳-希尔 | 出版社 |
| Silicon Graphics | 硅图公司 | |
| Sun Microsystems | — | 保留 Sun |
| University of Arizona | 亚利桑那大学 | |
| University of California at Berkeley | 加州大学伯克利分校 | |
| University of Colorado | 科罗拉多大学 | |
| University of Kent | 肯特大学 | |
| University of Maryland | 马里兰大学 | |
| University of Melbourne | 墨尔本大学 | |
| University of Rochester | 罗切斯特大学 | |
| University of Utah | 犹他大学 | |
| Usenix Association | Usenix 协会 | 保留 Usenix |
| Western Electric | 西方电气公司 | |
| Xerox | 施乐 | Xerox PARC 施乐帕洛阿尔托研究中心 |

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

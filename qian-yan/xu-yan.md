# 前言

本书是对加州大学伯克利分校所开发研究版 UNIX 系统的设计与实现的第一部权威而完整的描述，着墨最多的是 4.3BSD——它汇聚了此前伯克利各版本的改进。

**UNIX 系统**

UNIX 系统的运行范围上至最大的巨型机，下至个人家庭系统。它是多数多处理器系统、图形系统和向量处理系统的首选操作系统，也因其初衷——分时——而得到广泛使用。它是迄今开发出的可移植性最强的操作系统。这种可移植性部分归功于其实现语言 C [Kernighan & Ritchie, 1978]（C 本身也是移植得最广的语言之一），部分归功于系统优雅的设计。它的许多特性为其他系统所模仿 [O'Dell, 1987]。

自 1969 年问世 [Ritchie & Thompson, 1978] 以来，UNIX 系统沿若干条分而复合的支流演进。最初的开发者继续在 AT&T 贝尔实验室内部以其第九版 UNIX 推动技术前沿；与此同时，AT&T 把 UNIX System V 当作产品来授权。这两个系统都深受加州大学伯克利分校计算机系统研究组（CSRG）发布的伯克利软件发行版的影响。

**伯克利软件发行版**

这些伯克利系统为 UNIX 社区引入了许多有用的程序和设施：2BSD（伯克利 PDP-11 系统）中的文本编辑器 `vi`，3BSD（第一个伯克利 VAX 系统）中的请求调页虚拟存储支持，4.0BSD 的性能改进，4.1BSD 的作业控制、自动配置和长 C 标识符，以及 4.2BSD 和 4.3BSD 的可靠信号、改进的联网、完善的进程间通信（IPC）原语、快速文件系统和更多的性能改进。4.2BSD 与 4.3BSD 是许多厂商 UNIX 系统的基础，也被许多其他厂商的开发组内部使用。这些发展中的一部分已被 System V 吸收，或被产品本以 System V 为基础的厂商添加。

4.2BSD 与 4.3BSD 中 TCP/IP 网络协议套件的实现，加上这两个系统的可得性，解释了 TCP/IP 为何在全世界得到如此广泛的实现。众多厂商改用了伯克利的联网实现，无论其基础系统是 4.2BSD、4.3BSD、System V，还是甚至 VMS。

4BSD 还对 POSIX（IEEE Std 1003.1）操作系统接口标准及相关标准影响甚巨。若干特性——如可靠信号、作业控制、每进程多重访问组、目录操作例程——就是从 4.3BSD 纳入 POSIX 的。

**本书内容**

除开篇的历史材料外，本书中的“UNIX”一词均指 4.3BSD。凡涉及具体硬件之处，均以数字设备公司（DEC）的 VAX 为准。尽管许多厂商销售源自 4.2BSD 或 4.3BSD、运行于众多处理器和计算机系统（如 Motorola 68020、National Semiconductor 32032 或 Intel 80386）之上的系统，4BSD 最初是在 VAX 上开发出来的。这台机器也是当前伯克利软件发行版运行的机器之一，因而仍是一个便利的参照点。

本书讲的是 4.3BSD 的 **内部** 结构 [Quarterman et al., 1985]，是实现 4.3BSD 系统设施所用概念、数据结构和算法的深入阐述。其详尽程度与 Bach 论 System V UNIX 的著作 [Bach, 1986] 相仿；不过，本书聚焦于 UNIX 操作系统伯克利变体所用的设施、数据结构和算法。全书从系统调用一级向下覆盖——从内核接口直到硬件本身。内核包括进程管理、存储管理、I/O 系统、文件系统、`socket` 进程间通信机制以及网络协议实现等系统设施。系统调用一级以上的材料——库、shell、命令、编程语言及其他用户接口——不在本书范围内，只有少量与终端接口和系统启动有关的内容例外。与 Organick 论 Multics 的著作 [Organick, 1975] 一样，本书是对一个当代操作系统的深入研究。

能从本书受益的读者包括操作系统实现者、系统程序员、UNIX 应用开发者、管理员和好奇的用户。本书可以伴着系统源码阅读，其详略介于手册 [CSRG, 1986] 与代码之间。但本书既不是 UNIX 编程手册，也不是用户教程（教程可参阅 [Libes & Ressler, 1988]）。熟悉某种版本 UNIX 系统的使用（例如参见 [Kernighan & Pike, 1984]）以及 C 程序设计语言（例如参见 [Kernighan & Ritchie, 1988]），会极有帮助。

**在操作系统课程中的使用**

本书适合作为参考书，为操作系统二级课程的主教材提供背景。它不是供入门教学使用的教材；读者应当已经接触过存储管理、进程调度和 I/O 系统一类术语 [Peterson & Silberschatz, 1985]。熟悉网络协议的概念，对后面几章会很有帮助 [Tanenbaum, 1988; Stallings, 1985; Schwartz, 1987]。

每章末尾附有习题。习题分为三级，分别以无星、一星或两星标示。无星习题的答案可在正文中找到；一星习题需要在正文给出的概念之外加一步推理或直觉；两星习题则是大型设计项目或开放的研究问题。

**结构**

本书既讨论理念与设计问题，也讨论具体实现的细节。论述常常从系统调用一级入手，层层深入内核。书中用表格和插图阐明数据结构与控制流，用类 C 语言的伪代码展示算法。粗体用于标识程序名和文件系统路径名。斜体用于引入词汇表中出现的术语，并用于标识系统调用、变量、例程和结构的名字。例程名（系统调用除外）后面再跟一对圆括号以示区分（例如 *malloc()* 是例程名，而 *argv* 是变量名）。

全书分为五个部分：

* **第一部分 概览** 三章引论为整个操作系统、也为其余各章提供背景。第 1 章《历史和目标》勾勒系统的历史发展，着重其研究取向。第 2 章《4.3BSD 设计综述》描述系统所提供服务的性质，概述内核的内部组织，并讨论系统开发过程中做出的设计决策。第 3 章《内核服务》解释系统调用如何执行，并详细描述内核的一些基本服务。

* **第二部分 进程** 这一部分的第一章——第 4 章《进程管理》——描述进程的结构、调度进程执行的算法，以及系统为保证对内核驻留数据结构的一致访问所用的同步机制，为后续各章打下基础。第 5 章《存储管理》详细讨论虚拟存储管理系统。

* **第三部分 I/O 系统** 首先由第 6 章《I/O 系统概述》解释系统的 I/O 接口，并描述支持这一接口的设施的结构。引论之后的三章描述 I/O 系统三个主要组成部分的细节。第 7 章《文件系统》描述实现文件系统的数据结构和算法。第 8 章《设备驱动》讲解块设备与字符设备驱动，包括系统用来确定接有哪些物理设备的自动配置方法，并给出磁盘设备驱动的详细实例。第 9 章《终端处理》描述对字符终端的支持，并给出一个面向字符的设备驱动的描述。

* **第四部分 进程间通信** 第 10 章《进程间通信》描述为相关或无关进程间提供通信的机制。第 11 章《网络通信》与第 12 章《网络协议》密切相关：前者描述的设施很大程度上要靠后者所述的具体协议（如 TCP/IP 协议套件）来实现。

* **第五部分 系统运行** 第 13 章《系统启动》讨论系统的启动、停机与配置，并解释进程一级的系统初始化——从内核初始化一直到用户登录。

本书宜按章节顺序阅读，但除第一部分外，各部分相对独立，可以单独阅读。第 13 章应在读完全书其余部分之后再读，不过有基础的读者单独阅读它也会有所收获。

书末附有词汇表（给出主要术语的简要定义）和索引。每章有一个参考文献小节，列出相关材料的出处。

**致谢**

我们感谢以下各位，他们都阅读并评论了本书的初稿：Wayne Hathaway（Ultra Network Technologies）、Maurice Herlihy（卡内基-梅隆大学）、Thomas LeBlanc（罗切斯特大学）、Larry Peterson（亚利桑那大学）、Robert Elz（墨尔本大学）、Peter Collinson（肯特大学）、Dennis Ritchie（AT&T 贝尔实验室）、Matt Koehler（Sun Microsystems）、Eric Allman（国际计算机科学研究所）、Mike Hibler（犹他大学）、Robert Gingell（Sun Microsystems）、Joseph Moran（Legato Systems）、Christopher Torek（马里兰大学）、Kevin Fall（加州大学伯克利分校）、Peter Salus（Usenix 协会）、Evi Nemeth（科罗拉多大学）、Jim Lawson（Pixar）、Mike Paquette（Pixar）、Mike Russell（Pixar）、Donn Seeley（犹他大学）、Jay Lepreau（犹他大学）、Bill Shannon（Sun Microsystems）、Donald Coleman（Unisoft Corporation）、Michael O'Dell（Prisma, Incorporated）、Michel Gien 及其同事（Chorus Systèmes）。

本书使用 `pic`、`tbl`、`eqn` 和 `ditroff` 制作。索引由从 Jon Bentley 和 Brian Kernighan 所写索引程序衍生而来的 `awk` 脚本生成 [Bentley & Kernighan, 1986]。大部分插图先用 `cip` 生成 `pic` 输入，再经手工修整，清理毛糙的线条和未居中的文字。插图摆放和寡行消除由 `ditroff` 宏完成，孤行消除和偶数页底部对齐则只能手工处理。到头来我们的结论是：一定有更好的办法！

作者欢迎读者把改进建议，或对本书排印错误及其他错误的意见，用电子邮件发往 **bsdbook-bugs@berkeley.edu**。

## 参考文献

Bach, 1986.
M. J. Bach, *The Design of the UNIX Operating System*, Prentice-Hall, Englewood Cliffs, NJ (1986).

Bentley & Kernighan, 1986.
J. Bentley & B. Kernighan, “Tools for Printing Indexes,” Computing Science Technical Report 128, AT&T Bell Laboratories, Murray Hill, NJ (1986).

CSRG, 1986.
CSRG, “UNIX Programmer's Manual, 4.3 Berkeley Software Distribution, Virtual VAX-11 Version,” Six Volumes and an Index Volume, University of California Computer Systems Research Group, Berkeley, CA (April 1986).

Kernighan & Ritchie, 1978.
B. W. Kernighan & D. M. Ritchie, *The C Programming Language*, Prentice-Hall, Englewood Cliffs, NJ (1978).

Kernighan & Pike, 1984.
B. W. Kernighan & R. Pike, *The UNIX Programming Environment*, Prentice-Hall, Englewood Cliffs, NJ (1984).

Kernighan & Ritchie, 1988.
B. W. Kernighan & D. M. Ritchie, *The C Programming Language*, 2nd ed, Prentice-Hall, Englewood Cliffs, NJ (1988).

Libes & Ressler, 1988.
D. Libes & S. Ressler, *Life with UNIX*, Prentice-Hall, Englewood Cliffs, NJ (1988).

O'Dell, 1987.
M. O'Dell, “UNIX: The World View,” *Proceedings of the 1987 Winter USENIX Conference*, pp. 35–45 (January 1987).

Organick, 1975.
E. I. Organick, *The Multics System: An Examination of Its Structure*, MIT Press, Cambridge, MA (1975).

Peterson & Silberschatz, 1985.
J. Peterson & A. Silberschatz, *Operating System Concepts*, Addison-Wesley, Reading, MA (1985).

Quarterman et al., 1985.
J. S. Quarterman, A. Silberschatz, & J. L. Peterson, “4.2BSD and 4.3BSD as Examples of the UNIX System,” *ACM Computing Surveys* **17**(4), pp. 379–418 (December 1985).

Ritchie & Thompson, 1978.
D. M. Ritchie & K. Thompson, “The UNIX Time-Sharing System,” *Bell System Technical Journal* **57**(6 Part 2), pp. 1905–1929 (July-August 1978). The original version [*Comm. ACM* **7**(7), pp. 365–375 (July 1974)] described the 6th edition; this citation describes the 7th edition.

Schwartz, 1987.
M. Schwartz, *Telecommunication Networks*, Addison-Wesley, Reading, MA (1987).

Stallings, 1985.
R. Stallings, *Data and Computer Communications*, Macmillan, New York, NY (1985).

Tanenbaum, 1988.
A. S. Tanenbaum, *Computer Networks*, 2nd ed, Prentice-Hall, Englewood Cliffs, NJ (1988).

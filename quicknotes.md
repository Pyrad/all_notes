# Quick Notes

## yyc's GitHub:

[https://github.com/yungyuc](https://github.com/yungyuc)

## Install sphinx (related)

```shell
# 安装sphinx
pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com sphinx
# 安装sphinx_rtd_theme
pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com sphinx_rtd_theme
# 安装markdown支持工具
pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com recommonmark
pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com sphinx_markdown_tables
# 或者只安装Read The Docs网站上推荐的：myst_parser
pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com myst_parser
```

## **labuladong** 算法小抄

[https://labuladong.gitee.io/algo/](https://labuladong.gitee.io/algo/)

# Git for Windows downloads：

官网：https://github.com/git-for-windows/git/releases/
淘宝网镜像：http://npm.taobao.org/mirrors/git-for-windows/

## Github国内镜像

解决Github访问的神器
https://github.com.cnpmjs.org/
https://hub.fastgit.org/
https://github.wuyanzheshui.workers.dev/

# kernel.org国内镜像

北京交通大学：https://mirror.bjtu.edu.cn/kernel/linux/kernel/
清华大学：https://mirror.tuna.tsinghua.edu.cn/kernel/
南京大学：https://mirrors.nju.edu.cn/

# vscode

官网：https://code.visualstudio.com/#alt-downloads
官网下载速度有时候快有时候慢。
首先在官网找到需要下载的文件，点击下载。
复制载地址，然后将域名的部分更换为如下内容：
vscode.cdn.azure.cn <--------就是左边这个
例如更新后的地址为：https://vscode.cdn.azure.cn/stable/ea3859d4ba2f3e577a159bc91e3074c5d85c0523/code_1.52.1-1608136922_amd64.deb
这个就是国内的镜像了点开后你会发现速度直接起飞。

# mingw

用过mingw在线安装的看到这个估计会很开心吧
软件仓库：http://files.1f0.de/mingw/

# gvim

官网：https://www.vim.org/download.php

# msys2

https://github.com/msys2/msys2-installer/releases
https://mirrors.tuna.tsinghua.edu.cn/help/msys2/
MSYS2使用教程
https://blog.csdn.net/Dreamhai/article/details/109842184

# How-to ReadTheDoc articles

https://www.jianshu.com/p/058440ed14df

https://zhuanlan.zhihu.com/p/380889131

# Gitee笔记首页示例

http://hollischuang.gitee.io/tobetopjavaer/#/basics/object-oriented/object-oriented-vs-procedure-oriented

# Ubuntu 安装tofrodos（类似dos2unix)

ubuntu下面没有dos2unix，需要安装`tofrodos`来使用`todos`和`fromdos`这两个命令

```sh
# install tofrodos
apt-get install tofrodos

# Use todos (change a file from unix style to window style)
todos <FILE>

# Use fromdos (change a file from window style to unix style)
fromdos <FILE>
```

# Sphnix + reStructuredText + ReadTheDocs Tutorial

- [Series From youtube](https://www.youtube.com/watch?v=pzzjW0Xv_gk&list=PLPDCBPbzk1AYghqYazE7Cxt3p7edml8I7&index=1)

# MathJax

[MathJax Documentation](https://docs.mathjax.org/en/latest/index.html)

[How-to-add-MathJax in Sphinx](https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax)

# Vim frequently used commands

[link](http://blog.chinaunix.net/uid-20769502-id-112737.html)

[link2](https://www.zhihu.com/question/27478597/answer/36837839)

# 欧路词典词库

[https://mdx.mdict.org/](https://mdx.mdict.org/)

# Linux Powerline for Shell

How to install & use powerline in shell

- http://www.2daygeek.com/powerline-adds-powerful-statusline-to-vim-bash-tumx-in-ubuntu-fedora-debian-arch-linux-mint/

- https://linux.cn/article-8651-1.html (translated to Chinese)

# Git-bash powerline

[为 Git Bash 设置 PowerLine](https://zhuanlan.zhihu.com/p/402739037)

[使用nerd-font/font-patcher为字体添加字体图标](https://zhuanlan.zhihu.com/p/150097941)

# Shell - parameter substitution

[https://tldp.org/LDP/abs/html/parameter-substitution.html](https://tldp.org/LDP/abs/html/parameter-substitution.html)

# MSYS2 on Windows - Backspace works abnormally

Each hit of `backspace` produces a space and make the cursor move right, which is really a dealbreaker.

Possible solutions in this discussion: [Arrow keys and backspace not working in bash after recent update](https://github.com/msys2/MSYS2-packages/issues/1124)



# CMake Workshop

[Detecting your environment](https://enccs.github.io/cmake-workshop/environment/)

# Github 加速

[github访问加速](https://zhuanlan.zhihu.com/p/75994966?utm_source=wechat_session)

# How to write a coc.nvim extension

[Sam's world](https://samroeca.com/)

https://samroeca.com/coc-plugin.html#coc-plugin

# GitHub Speedup (diff ways)

[Github加速的10种方式](https://www.cnblogs.com/shuangxinyuan/p/15506449.html)

# Compiler Explorer

[gcc.godbolt.org](https://gcc.godbolt.org)

# Checking the code generated implicitly by the C++ compiler

https://stackoverflow.com/questions/24858014/checking-the-code-generated-implicitly-by-the-c-compiler

# How can I see parse tree, intermediate code, optimization code and assembly code during COMPILATION?

https://stackoverflow.com/questions/1496497/how-can-i-see-parse-tree-intermediate-code-optimization-code-and-assembly-code

# How to make vim for win32 - Yongwei

https://github.com/adah1972/vim/wiki

# Pass clangd args to YouCompleteMe

```vim
let g:ycm_clangd_args = ['--query-driver=' .. '/depot/gcc-7.3.0/bin/g++']
```

# Building with CMake, Ninja and Clang on Windows

https://newbedev.com/building-with-cmake-ninja-and-clang-on-windows

# Use GDB in Geany

[The Geany](https://www.geany.org/)

https://www.zhihu.com/question/65306462/answer/2603110780

# 瑞泽家园样板间地址

用友软件园西区1C#楼2段北

# 百度网盘搜索 - 知乎文章

[15个好用的百度网盘搜索引擎 - crystal的文章 - 知乎](https://zhuanlan.zhihu.com/p/60840594)

# Use homebrew mirror URLs from Tsinghua university

[Homebrew / Linuxbrew 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/)

[Homebrew 国内使用加速](https://www.cnblogs.com/cocowool/p/speedup-homebrew.html)

# Computational Geometry

https://en.wikipedia.org/wiki/Computational_geometry

[NanoVG](https://github.com/memononen/nanovg)

[你工作中最推荐的 C/C++ 程序库有哪些，为什么？ - chunquedong的回答 - 知乎](https://www.zhihu.com/question/51134387/answer/2664748363)

[你工作中最推荐的 C/C++ 程序库有哪些，为什么？ - 知乎](https://www.zhihu.com/question/51134387)

# Doxygen - How to create a doxygen doc for C++ STL?

https://www.doxygen.nl/manual/external.html

https://en.cppreference.com/w/Cppreference:Archives

https://flcwiki.desy.de/How%20to%20document%20your%20code%20using%20doxygen

# English word check

[linggle](https://linggle.com/)

# Z-library how-to-find

[Pirate Library Mirror](http://pilimi.org/)

[Zlibrary 最新入口](https://find.looks.wang/)

[易书论坛 Zlibrary](https://bbs.yibook.org/)

[Zlibrary Pro Helper](https://zlib.pro/)

https://nav.yibook.org/

https://www.pdfdrive.com/

https://xmsoushu.com/#/



# Word

Floor is yours, it means: You have the right to speak now! Say what you want!

# Latex Math Symbols

[List of LaTeX mathematical symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)

# Latex Use backslash itself

A example using backslash in a matrix (latex syntax)

$$
\begin{matrix}
\alpha & \backslash{alpha} & \beta & \backslash{beta} &
\gamma & \backslash{gamma} & \delta & \backslash{delta} \\
\end{matrix}
$$

# Add icon for html files generated by sphinx

> Thanks to @StevePiercy I found this documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_favicon
> 
> conf.py
> 
> `html_favicon = 'favicon.ico'`
> 
> I put favicon.ico in my source folder, next to my .rst-files and it is working as expected: https://global-coffee-data-standard.readthedocs.io/en/latest/index.html

# CMake 正确链接动态库

[CMake如何做到正确链接动态库so？ - Lion Long的回答 - 知乎](https://www.zhihu.com/question/489682173/answer/2873091122)

# Bentley-Ottmann Sweep line algorithm

[Bentley-Ottmann Sweep line algorithm](https://github.com/ideasman42/isect_segments-bentley_ottmann)

# Bash multiple conditions and `[[` and `((` in if-condition

[Bash Multiple Conditions](https://stackoverflow.com/a/20263097)


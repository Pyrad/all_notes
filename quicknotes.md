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




# To disable cursor blinking in Windows Terminal

For bash/zsh

Putting the following at the end of your .bashrc/.zshrc file

```bash
echo -e -n "\e[2 q"
```


For PowerShell

```powershell
Write-Host -NoNewLine "`e[2 q"
```







# MSYS2 on Windows - Backspace works abnormally

Each hit of `backspace` produces a space and make the cursor move right, which is really a dealbreaker.

Possible solutions in this discussion: [Arrow keys and backspace not working in bash after recent update](https://github.com/msys2/MSYS2-packages/issues/1124)




# Check fonts in Linux

字体列表

```bash
fc-list
```

中文字体

```bash
fc-list :lang=zh
```

查看字体详情

```bash
fc-match -v "FontName"
```

# MSYS2 CMake path prefix is in Windows format (C:/) but needs MSYS2/\*nix style (/c/) to link

[MSYS2 CMake path prefix is in Windows format (C:/) but needs MSYS2/*nix style (/c/) to link](https://stackoverflow.com/questions/54767375/msys2-cmake-path-prefix-is-in-windows-format-c-but-needs-msys2-nix-style)

```cmake
    cmake_minimum_required(VERSION 3.12)

    project(sample CXX)

    # Find GTK+ headers/libs with PkgConfig
    find_package(PkgConfig REQUIRED)
    pkg_check_modules(GTK3 REQUIRED gtk+-3.0)

    # Generated paths starting with "C:" need to be converted to /c/ to work with MSYS2
    # TODO remove this or do it some way better at some point in the future
    if(MSYS OR MINGW)
        string(REGEX REPLACE "C:" "/c/" GTK3_INCLUDE_DIRS "${GTK3_INCLUDE_DIRS}")
    endif(MSYS OR MINGW)

    include_directories(${GTK3_INCLUDE_DIRS})
    link_directories(${GTK3_LIBRARY_DIRS})

    add_definitions(${GTK3_CFLAGS_OTHER})

    set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib/natives)
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib/natives)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

    add_executable(sample src/main.cpp)

    target_link_libraries(sample ${GTK3_LIBRARIES})
```

# Turn on `-DBoost_DEBUG=ON` for cmake to print out more information about errors
[cmake v3.15.3 cannot find boost v1.71.0](https://stackoverflow.com/questions/57870032/cmake-v3-15-3-cannot-find-boost-v1-71-0)






# CMake Workshop

[Detecting your environment](https://enccs.github.io/cmake-workshop/environment/)







# Github 加速

[github访问加速](https://zhuanlan.zhihu.com/p/75994966?utm_source=wechat_session)





# How to write a coc.nvim extension

[Sam's world](https://samroeca.com/)

https://samroeca.com/coc-plugin.html#coc-plugin



# GitHub Speedup (diff ways)

[Github加速的10种方式](https://www.cnblogs.com/shuangxinyuan/p/15506449.html)





# VIM设置python3支持和检测python version

注意vim的版本（64or32）必须和python3的版本一致

python3的版本必须和vim中+python3/dyn所指明的python3版本一致，否则`echo has("python3")`只会返回`0`

https://www.jianshu.com/p/18f06d12348c

https://blog.zengrong.net/post/pyton_support_on_vim/



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


# Tcl tutorial

https://wiki.tcl-lang.org/page/Tcl+Tutorial+Index

# Tcl man page

https://www.tcl.tk/man/tcl/contents.html



# Vim to check if a plugin is loaded

https://vi.stackexchange.com/questions/10939/how-to-see-if-a-plugin-is-active

```vim
" Method 1
g:loaded_<plugin_name>

" Method 2
if exists("loaded_<plugin_name>")
" ...
endif
```






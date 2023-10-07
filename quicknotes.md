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

# GDB Python Support

[GDB Python Support](https://devguide.python.org/advanced-tools/gdb/index.html)

# GDB Pretty Printer

https://stackoverflow.com/questions/12574253/c-gdb-python-pretty-printing-tutorial

https://www.kurokatta.org/grumble/2018/05/gdb-pretty

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

# Does C++ lambda have any runtime cost?

Short answer: no.

detail: [https://stackoverflow.com/questions/50346822/does-lambda-object-construction-cost-a-lot]()

> here, lambda is just an instance of an anonymous type. The type itself is processed at compile-time, so no worries.
> What happens at run-time though is the capture of variables (here var). When a capture is done by value, the value itself is copied into the lambda instance.
> This is what costs. When a capture is done by reference, the reference is copied into the lambda, which is cheap.

# C++ Macro Expansion

Use `-E` option of `gcc/g++`.

```shell
g++ -E source_file.cpp > source_file_preprocess_out.cpp
```

# Word

Floor is yours, it means: You have the right to speak now! Say what you want!

# Latex Math Symbols

[List of LaTeX mathematical symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)

# GDB tutorial

[RMS's gdb Debugger Tutorial](http://www.unknownroad.com/rtfm/gdbtut/)

# Git repo control line ending styles

[Git End-of-Line Issues](https://learn.openwaterfoundation.org/owf-learn-git/eol/)

# Latex Use backslash itself

A example using backslash in a matrx (latex syntax)

$$
\begin{matrix}
\alpha & \backslash{alpha} & \beta & \backslash{beta} &
\gamma & \backslash{gamma} & \delta & \backslash{delta} \\
\end{matrix}
$$

# Greek Alphabet in Latex

$$
\begin{matrix}
A\alpha & A, \backslash{alpha} &
B\beta & B, \backslash{beta} \\
\Gamma\gamma & \backslash{Gamma}, \backslash{gamma} &
\Delta\delta & \backslash{Delta}, \backslash{delta} \\
E\epsilon & E, \backslash{epsilon} &
Z\zeta& Z, \backslash{zeta} \\
H\eta & H, \backslash{eta} &
\Theta\theta & \backslash{Theta}, \backslash{theta} \\
I\iota & I, \backslash{iota} &
K\kappa & K,\backslash{kappa}\\
\Lambda\lambda & \backslash{Lambda}, \backslash{lambda} &
M\mu & M, \backslash{mu} \\
N\nu & N, \backslash{nu} &
\Xi\xi & \backslash{Xi}, \backslash{xi} \\
O\omicron & O, \backslash{omicron} &
\Pi\pi&  \backslash{Pi}, \backslash{pi} \\
P\rho & P, \backslash{rho} &
\Sigma\sigma &  \backslash{Sigma}, \backslash{sigma} \\
T\tau & T, \backslash{tau} &
\Upsilon\upsilon &  \backslash{Upsilon}, \backslash{upsilon } \\
\Phi\phi & \backslash{Phi}, \backslash{phi} &
X\chi &  X, \backslash{chi } \\
\Psi\psi & \backslash{Psi}, \backslash{psi} &
\Omega\omega &   \backslash{Omega}, \backslash{omega}
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

# Initialize a std::unique_ptr with `nullptr`

See [Why does my unique_ptr think is has a null function pointer deleter](https://stackoverflow.com/questions/22915631/why-does-my-unique-ptr-think-is-has-a-null-function-pointer-deleter)

```cpp
class FooObj {
  FooObj() {}
  ~FooObj() { std::cout << "dtor!\n"; }
};

void freeFooObj(FooObj *obj) {
  if (obj) {
    std::cout << "Free func for FooObj\n";
    delete obj;
  }
}

class Foo {
  // Use nullptr and a free func to initialize it
  Foo::Foo() :  m_val(nullptr, freeFooObj) { }

  std::unique_ptr<FooObj, decltype(freeFooObj)> m_val;
};
```

# CMake 正确链接动态库

[CMake如何做到正确链接动态库so？ - Lion Long的回答 - 知乎](https://www.zhihu.com/question/489682173/answer/2873091122)

# GDB uses a file as interactive input

If a program asks for user's input after launched, the user's input can be written into a file, and let `gdb` read that file as user's input, thus interactive input in `gdb` can be avoided.

For example, when running `corexec`, it might ask for user's confirmation and then continue,

```shell
If you wish to ignore this warning, type Y.
Typing anything else will terminate.
> 
```

In this circumstances, you can type `Y`, and then hit `Enter` key to let it continue.

```shell
If you wish to ignore this warning, type Y.
Typing anything else will terminate.
> Y
```

But if the binary is attached into `gdb`, and then it asks for user's input. But there's no way to type that as `gdb` session doesn't know how to read it from `stdin`.

So write `Y` to a file (for example, `gdbStdin.in`), and start `gdb` as below,

```shell
corexec simp1_PBCSIMPLE_NDF.pjx 331 331 -color 1 -no_output < ./gdbStdin.in
```

# Linux rename multiple files

Use command `rename`

For example, if there a few files below,

```shell
myDbgFile_a.txt
myDbgFile_b.txt
myDbgFile_c.txt
```

If I'd like to change the name from "my" to "myTest" in each file name, I can use the following

```shell
rename my myTest *.txt
```

Here the 1st option `my` is the pattern I'd like to replace, and the 2nd option `myTest` is the string after replacement.

The 3rd option specifies the files waiting for replacement.

So after replacement, file names are,

```shell
myTestDbgFile_a.txt
myTestDbgFile_b.txt
myTestDbgFile_c.txt
```



# Permenantly delete commits after a commit number

[Answer in Stack Overflow](https://stackoverflow.com/questions/4114095/how-do-i-revert-a-git-repository-to-a-previous-commit)

This will destroy any local modifications after 0d1d7fc32 (0d1d7fc32 is not destroyed)

Don't do it if you have uncommitted work you want to keep.

```shell
git reset --hard 0d1d7fc32
```

Alternatively, if there's work to keep

```shell
git stash
git reset --hard 0d1d7fc32
git stash pop
```

This saves the modifications, then reapplies that patch after resetting.

You could get merge conflicts, if you've modified things which were changed since the commit you reset to.

# Git cheat-sheet from GitLab

[git-cheat-sheet.pdf](https://about.gitlab.com/images/press/git-cheat-sheet.pdf)

# Bentley-Ottmann Sweep line algorithm

[Bentley-Ottmann Sweep line algorithm](https://github.com/ideasman42/isect_segments-bentley_ottmann)



# Start X-services from cygwin on Windows

When to start a GUI program in a Cygwin shell on Windows, `gitg` for instance, it will raise the following error,

```shell
Unable to init server: Could not connect to 127.0.0.1: Connection refused

(gedit:8196): Gtk-WARNING **: cannot open display:
```

To fix this,

1. [install Cygwin/X](http://x.cygwin.com/docs/ug/setup.html#setup-cygwin-x-installing)

2. open cygwin and start x11 server by typing
   
   ```shell
   startxwin >/dev/null 2>&1 &
   ```

3. set `DISPLAY` environment variable as explained [here](http://x.cygwin.com/docs/ug/using-local-apps.html) by typing
   
   ```shell
   export DISPLAY=:0.0
   ```

Start gitg normally

The steps here come from this [answer](https://stackoverflow.com/questions/36209671/im-trying-to-run-gedit-in-cygwin-but-receiving-error)



# What's Vim paste mode?

[https://techexplorations.com/blog/kicad/blog-how-to-copy-text-into-vim/](https://techexplorations.com/blog/kicad/blog-how-to-copy-text-into-vim/)

If you are copying text for which the formatting should not change, beware that the above process can introduce changes to the formatting.
For example, if you are copying Python code into a file using Vim, be prepared for the indentation to be altered, and therefore your program to not work as expected.
In Python, code blocks like loops are denoted using text indentation.

To avoid this from happening, you can use Vim’s paste mode. When you enable paste mode, Vim will not auto-indent any text that you paste.
To enable paste mode, follow this process:

In Vim, ensure you are command mode by hitting the Esc key.
- Type `:set paste` to enter command mode.
- Type `i` to enter paste mode. Notice the `– INSERT (paste) –` at the bottom of the Vim window.
- Paste your Python code into Vim. Indentation should be as in the original
- To exit paste mode, type `:set nopaste`. Notice the `– INSERT –` at the bottom of the Vim window. This means you are back to normal insert mode.


# Vim remove color codes from terminal

[Removing ANSI Color Codes from a text file in VI](https://superuser.com/questions/1445805/removing-ansi-color-codes-from-a-text-file-in-vi)

# Vim Reload current file

Just use `:e`

# Bash multiple conditions and `[[` and `((` in if-condition

[Bash Multiple Conditions](https://stackoverflow.com/a/20263097)


# Vim get current file name and path

Symbol `%` is a register in Vim, which stores the current file name

In normal mode, use `"%p` to paste the current file name to current cursor's position (or use `"%P` to paste before the cursor)

[Get the name of the current file](https://vim.fandom.com/wiki/Get_the_name_of_the_current_file#:~:text=In%20insert%20mode%2C%20type%20Ctrl,to%20create%20a%20similar%20name.)




# Use a stash for temp backup

[A practical guide to using the git stash command | Opensource.com](https://opensource.com/article/21/4/git-stash)

If you have some files modified in current branch, but suddenly you want to switch to other branches with a clean directory (no modified file), then you can use `git stash`.



Save your current modified files to a stash

```shell
git stash
```

or,

```shell
git stash save "My temp modified files"
```



To check how many stashes you have,

```shell
git stash list
```

This might show something like this,

```shell
stash@{0}: WIP on dev: 40d943c63b Fix a bug
stash@{1}: WIP on dev: f0000c6066 Update code format
```



To show a diff summary of a specific stash, for example, to check `stash@{0}`

```shell
git stash show stash@{0}
```

This will show something like this,

```shell
 src/array.cpp          |  2 +-
 src/geom.cpp           | 37 +++++++++++++--------------
 2 files changed, 19 insertions(+), 20 deletions(-)
```



To bring up your code from a specific stash, for example, retrieve code from `stash@{0}`

```shell
git stash apply stash@{0}
```

The above command will not remove the stash. If you want to remove it from the stash list, use `pop` instead as the following,

```shell
git stash pop stash@{0}
```



To show detailed diff, use `--patch` or `-p` flag together with `show` option.

```shell
git stash show stash@{0}
git stash show stash@{0} --patch
```



# Resolve conflicts when merging from another branch

once conflict occurs after `git merge $branch_name`, it will show what file has conflicts, and it needs to be resolved before merged.

Just open that file using `vi` or other text editor, and find conflict marker `<<<<<<<<`. Then fix the conflicts.

After conflicts are resolved, just add that file(s) by using

```shell
git add .
```

Then commit it by using

```shell
git commit
```

Now it seems like below,

```shell
 1 Merge branch 'master' into dev
 2                                                                                 
 3 # Conflicts:                                                                    
 4 #       src/array.cpp
 5 #                                                                               
 6 # It looks like you may be committing a merge.                                  
 7 # If this is not correct, please remove the file                                
 8 #       .git/MERGE_HEAD                                                         
 9 # and try again.                                                                
10                                                                                 
11                                                                                 
12 # Please enter the commit message for your changes. Lines starting              
13 # with '#' will be ignored, and an empty message aborts the commit.             
14 #                                                                               
15 # On branch allangle                                                            
16 # All conflicts fixed but you are still merging.                                
17 #                                                                               
18 # Changes to be committed:                                                      
19 #       modified:   src/array.hpp
```

It reminds you that current you are committing a merge.

Save and commit, then it's done.


# The simplest way to list conflicted files in Git

[What's the simplest way to list conflicted files in Git?](https://stackoverflow.com/questions/3065650/whats-the-simplest-way-to-list-conflicted-files-in-git)

```shell
git diff --name-only --diff-filter=U --relative
```



# Vim Repeat finding next character in this line

Use `f` + `<char>` to move the the 1st occurrence of this line, then press `;` (semicolon) to jump to the 2nd occurrence, again for the next until none.

# Use vimgrep and quickfix window

```vim
:vimgrep /keyword_pattern/g % | cw
```

Here `keyword_pattern` is the word to search, and `%` is current file name, `cw` is used to open the quickfix windows


# Python create list and generator

```python
a_list = [i for i in range(10)]
a_itr = (i for i in range(10))
next_element_0 = next(a_itr, None)
next_element_1 = next(a_itr, None)
```

Here `next_element_0` is `0` and `next_element_1` is `1`.


# Change weird username on Windows 11

1. Open Run Command by `Win + R`, type `netplwiz` and hit `Enter`.
2. In the User Accounts window, select the user account for which the username needs to be changed.
3. Click on Properties.
4. In the General tab, you'll see your existing username. Rename it to your liking after removing it.
5. Once the new username has been added, click the Apply button and OK.
6. Then, log out of your account, and you'll be greeted with your new username on the sign-in screen when you sign in.



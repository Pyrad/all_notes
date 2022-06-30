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


# 打印一个函数里面的static variable
(gdb) p 'longc_perf_test::longc_perf_cnt_7()::cnt'
这里longc_perf_test是namespace，longc_perf_cnt_7()是函数，cnt是函数longc_perf_cnt_7()中的static变量，注意单引号必须加上

# 查看一个变量的类型: 
https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_109.html

whatis variable_name

ptype variable_name

# 查看gdb是否在编译时期设置了python support
gdb --configuration

# 命令教程- 如何加载core dump文件
http://www.yolinux.com/TUTORIALS/GDB-Commands.html#STLDEREF

# Gdbinit file example
https://gist.github.com/CocoaBeans/1879270





# Git-bash powerline

[为 Git Bash 设置 PowerLine](https://zhuanlan.zhihu.com/p/402739037)

[使用nerd-font/font-patcher为字体添加字体图标](https://zhuanlan.zhihu.com/p/150097941)



# GDB - Attached process to read stdin

[https://github.com/cgdb/cgdb/issues/36](https://github.com/cgdb/cgdb/issues/36)

Example,

Write the desired input to a file "input.txt", then redirect in gdb

```shell
(gdb) r program-arg-list < input.txt
```


# Shell - parameter substitution

[https://tldp.org/LDP/abs/html/parameter-substitution.html](https://tldp.org/LDP/abs/html/parameter-substitution.html)

# GDB - show program arguments

```gdb
(gdb) show args
```



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



# GDB check vtable from a pointer/reference to base class object

```gdb
(gdb) run
Starting program: /home/bazis/test

Program received signal SIGTRAP, Trace/breakpoint trap.
main (argc=1, argv=0xbffff064) at test.cpp:23
23 delete pObject;
(gdb) print pObject
$1 = (BaseClass *) 0x804b008
(gdb) info vtbl pObject
vtable for 'BaseClass' @ 0x80486c8 (subobject @ 0x804b008):
[0]: 0x80485f4 <ChildClass::Test()>
(gdb) info symbol 0x80486c8
vtable for ChildClass + 8 in section .rodata of /home/bazis/test
```


# Bash colors

```bash
cReset='\033[0m'
cPrefix='\033['

code_style_normal="0"
code_style_bold="1"
code_style_faint="2"
code_style_italics="3"
code_style_underline="4"

code_foreground="3"
code_light_foreground="9"
code_background="4"
code_light_background="10"

color_black="0m"
color_red="1m"
color_green="2m"
color_orange="3m"
color_blue="4m"
color_purple="5m"
color_cyan="6m"
color_gray="7m"
```

```bash
### Show different kinds of colors

cReset='\033[0m'
cPrefix='\033['

code_style_normal="0"
code_style_bold="1"
code_style_faint="2"
code_style_italics="3"
code_style_underline="4"
slist=($code_style_normal $code_style_bold $code_style_faint \
         $code_style_italics $code_style_underline)
slist_str=("normal" "bold" "faint" "italics" "underline")
snum=${#slist[@]}


code_foreground="3"
code_light_foreground="9"
code_background="4"
code_light_background="10"
glist=($code_foreground $code_light_foreground $code_background $code_light_background)
glist_str=("fore" "light_fore" "back" "light_back")
gnum=${#glist[@]}

color_black="0m"
color_red="1m"
color_green="2m"
color_orange="3m"
color_blue="4m"
color_purple="5m"
color_cyan="6m"
color_gray="7m"
clist=($color_black $color_red $color_green $color_orange $color_blue \
         $color_purple $color_cyan $color_gray)
clist_str=("black" "red" "green" "orange" "blue" "purple" "cyan" "gray")
cnum=${#clist[@]}

for (( s = 0; s < snum; s++ )) do
   for (( g = 0; g < gnum; g++ )) do
      for (( c = 0; c < cnum; c++ )) do
         sstr="${slist_str[$s]}"
         gstr="${glist_str[$g]}"
         cstr="${clist_str[$c]}"

         scode="${slist[$s]}"
         gcode="${glist[$g]}"
         ccode="${clist[$c]}"

         msg="${sstr} + ${gstr} + ${cstr}"
         ccode="${cPrefix}${scode};${gcode}${ccode}"
         echo -e "$s-$g-$c ${ccode}${msg} ${cReset}"
      done
   done
done

```




# How to insert special code (unicode) in Vim

- `i` go to insert mode

- `Ctrl + v` go into ins-special-keys mode

- `u2713` insert the Unicode character CHECK MARK (U+2713). Here first char `u` tells it the following 4 chars are unicode

Some powerline special glyphs


`e0a0` stream

`e0a1` Line number

`e0a2` Lock

`e0a3` (Not sure)

`e0b0`, `e0b1`, `e0b2`, `e0b3`, `e0b4`, `e0b5`, `e0b6`, `e0b7`, `e0b8`, `e0b9`, `e0ba`

`e0bb`, `e0bc`, `e0be`, `e0bf`, `e0c0`, `e0c1`, `e0c2`, `e0c3`, `e0c4`, `e0c5`, `e0c6`

`e0c7`, `e0c8`, `e0ca`, `e0cc`, `e0cd`, `e0ce`, `e0ce`, `e0cf`, `e0d0`, `e0d1`, `e0d2`, `e0d4`

```bash



        # original
        'patched': {
                'lock': u'\uE0A2',
                'network': u'\uE0A2',
                'separator': u'\uE0B0',
                'separator_thin': u'\uE0B1'
        },
        # angly 1
        'patched': {
                'lock': u'\uE0A2',
                'network': u'\uE0A2',
                'separator': u'\uE0B8',
                'separator_thin': u'\uE0B9'
        },
        # angly 2
        'patched': {
        	'lock': u'\uE0A2',
        	'network': u'\uE0A2',
        	'separator': u'\uE0BC',
        	'separator_thin': u'\uE0BD'
        },
        # curvy
        'patched': {
        	'lock': u'\uE0A2',
        	'network': u'\uE0A2',
        	'separator': u'\uE0B4',
        	'separator_thin': u'\uE0B5'
        },
        # flames (flamey)
        'patched': {
        	'lock': u'\uE0A2',
        	'network': u'\uE0A2',
        	'separator': u'\uE0C0',
        	'separator_thin': u'\uE0C1'
        },
        # lego (blocky)
        'patched': {
        	'lock': u'\uE0A2',
        	'network': u'\uE0A2',
        	'separator': u'\uE0CE',
        	'separator_thin': u'\uE0CF'
        },
        # pixelated blocks 2 (large) random fade (pixey)
        'patched': {
        	'lock': u'\uE0A2',
        	'network': u'\uE0A2',
        	'separator': u'\uE0C6',
        	'separator_thin': u'\uE0C6'
        }
```


### MSYS2 on Windows - Backspace works abnormally

Each hit of `backspace` produces a space and make the cursor move right, which is really a dealbreaker.

Possible solutions in this discussion: [Arrow keys and backspace not working in bash after recent update](https://github.com/msys2/MSYS2-packages/issues/1124)




### Bash array

```bash
# Syntax		Result
arr=()		Create an empty array
arr=(1 2 3)	Initialize array
${arr[2]}	Retrieve third element
${arr[@]}	Retrieve all elements
${!arr[@]}	Retrieve array indices
${#arr[@]}	Calculate array size
arr[0]=3	         Overwrite 1st element
arr+=(4)	         Append value(s)
str=$(ls)	Save ls output as a string
arr=( $(ls) )	Save ls output as an array of files
${arr[@]:s:n}	Retrieve n elements starting at index s
```


### Function shell variables

All function parameters or arguments can be accessed via `$1, $2, $3,..., $N`.

`$0` always point to the shell script name.

`$*` or `$@` holds all parameters or arguments passed to the function.

`$#` holds the number of positional parameters passed to the function.


## Check fonts in Linux
fc-list   #字体列表
fc-list :lang=zh  #中文字体
fc-match -v "字体名" # 查看字体详情

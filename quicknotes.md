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

# Vim

### Vim diff
1. 启动
vimdiff FILE_LEFT FILE_RIGHT
或者
vim -d FILE_LEFT FILE_RIGHT
2. 启动之后，两侧的文件滚动式同步的。
跳转到下一个差异点命令  ]c
跳转到上一个差异点命令  [c

3. 文件合并命令
（注意，当前光标所在的文件是当前文件）
如果希望把一个差异点中当前文件的内容复制到另一个文件里，可以使用命令→ dp，这个命令的含义是diff put
如果希望把一个差异点中另一个文件的内容复制到当前文件里，可以使用命令→ do，这个命令的含义是diff get，因为dg这个命令已经被占用，所以用了do.
4. 打开折叠的文本行用命令→ zo，意思是folding open，用字母z是因为它像被折叠的样子。。。
重新折叠的文本行用命令→ zc，意思是folding close


### Vim colors
How to tell vim how many colors your terminal could be capable of?
t_Co=256 tells Vim that your terminal is capable of using 256 colors (whether that is correct or not). termguicolors is a relative recent addition in Vim 8 and tells Vim that your terminal is capable of handling rgb colors (e.g. 16 Million colors, whether that is correct or not)
	
From <https://github.com/vim-airline/vim-airline/issues/26>

### Execute Vim script
In non-interactive mode: `vim -s <cmds.file.vim> -es <file.to.modify>`


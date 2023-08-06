# Felia

## 关于

felia是一个执行终端命令的工具，搭配Pycharm Python console使用，利用其强大的智能补全特性，提高命令输入效率。

## 安装

```text
pip install felia
```

## 快速上手

打开Pycharm的Python控制台 <kbd>工具</kbd> -> <kbd>Python或调试控制台</kbd>

执行代码

```ipython
>>> from felia.pip import *
>>> pip_list()
INFO $ pip list
Package                Version             
---------------------- --------------------
.......                ........ 
```

## 已实现的命令行工具

* cobra
* docker
* go
* pip
* protoc
* sphinx
* ssh
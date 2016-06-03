# encoding: utf8

print '''
定义文件编码
Python 默认使用 ASCII 编码
设定编码的注释只能写在第一行或者第二行，因为第一行有时候会被用来指定Python的执行路径
这行注释需要匹配如下正则表达式 "^[ \t\v]*#.*?coding[:=][ \t]*([-_.a-zA-Z0-9]+)"

常见的文件第一二行的写法
# coding=<encoding name>

# coding:<encoding name>

linux 系统下通常这样写
#!/usr/bin/python
# -*- coding: <encoding name> -*-

#!/usr/bin/python
# vim: set fileencoding=<encoding name> :
'''

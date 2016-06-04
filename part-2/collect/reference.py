#! /usr/bin/python
# encoding: utf-8

print '''
is 如果两个变量指向同一个 object, 返回 True
== 如果两个变量的值相同，返回 True
'''
a = b = 1
print 'a = b = 1; a == b', a == b
print 'a is b', a is b

a = b = [1]
print 'a = b =[1], a == b', a == b
print 'a is b', a is b
c = [1]
print 'c = [1]; c == b', c == b
print 'c is b', c is b


print '''
number, string, tuple 不可变数据属于值传递
dict, list, set 等可变对象类型 引用传递
'''

list_a = [0,1,3,4,5]
list_b = list_a
print 'list_a =', list_a
print 'list_b =', list_b
list_b.reverse()
print 'list_b.reverse()'
print 'list_a =', list_a
print 'list_b =', list_b
list_c = list(reversed(list_b))
print 'list_c = list(reversed(list_b))'
print 'list_a =', list_a
print 'list_b =', list_b
print 'list_c =', list_c

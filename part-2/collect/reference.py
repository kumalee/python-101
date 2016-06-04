#! /usr/bin/python
# encoding: utf-8

print '''
number, string, tuple 不可变数据属于值传递
dict, list, set 等可变对象类型 引用传递
'''

'''
is 如果两个变量指向同一个 object, 返回 True
== 如果两个变量的值相同，返回 True
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

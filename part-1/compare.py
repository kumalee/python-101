# coding: utf8

print '''
CPython implementation detail: Objects of different types except numbers are ordered by their type names; objects of the same types that don’t support proper comparison are ordered by their address.

>>> 5 < 'foo'   # <type 'int'> < <type 'str'>
True
>>> 5 < (1, 2)  
True
>>> 5 < {}     
True
>>> 5 < [1, 2] 
True


>>> [1, 2] > 'foo'   # 'list' < 'str' 
False
>>> (1, 2) > 'foo'   # 'tuple' > 'str'
True

'''


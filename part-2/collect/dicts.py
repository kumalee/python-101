#! /usr/bin/python
# encoding: utf-8

d1 = dict(a=1, b=[1,2,3], c=tuple([1,2,3]))
d2 = {'a':1, 'b':[1,2,3], 'c':tuple([1,2,3])}
print d1, '\n', d2
print d1 == d2
print d1 is d2
d3 = d2
print d2 is d3

t1 = tuple([1,2,3])
t2 = tuple([1,2,3])
t3 = t2
print '\n'
print t1==t2
print t3==t2
print t1 is t2
print t3 is t2

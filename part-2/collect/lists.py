#! /usr/bin/python
# encoding: utf-8

list_a = [1,2,3]
print dir(list_a)
print '\n','list_a =', list_a, '\n'

print list_a.append.__doc__, '\n'
print '1 in list_a'
print 1 in list_a, '\n'

print '4 in list_a'
print 4 in list_a

list_a.append(4)
print 'list_a.append(4)'
print 'list_a =', list_a
print '4 in list_a'
print 4 in list_a

for a in list_a:
    print a

print 'list[start_index:end_index]'
print 'list_a[0] =', list_a[0]
print 'list_a[-1] =', list_a[-1]
print 'list_a[0:2] =', list_a[0:2]
print 'list_a[2:] =', list_a[2:]
print 'list_a[1:-1] =', list_a[1:-1]
print 'list_a[-1:1] =', list_a[-1:1]
print 'list_a[:] =', list_a[:]

print '\n', list_a.extend.__doc__, '\n'
list_a.extend([5])
print 'list_a.extend([5])'
print 'list_a =', list_a

print '\n', list_a.count.__doc__, '\n'
print 'list_a.count(0) =', list_a.count(0)
print 'list_a.count(1) =', list_a.count(1)

print '\n', list_a.index.__doc__, '\n'
print 'list_a.index(1) =', list_a.index(1)
print 'list_a.index(2) =', list_a.index(2)
print 'list_a.index(5) =', list_a.index(5)

print '\n', list_a.insert.__doc__, '\n'
list_a.insert(0,0)
print 'list_a.insert(0,0) =', list_a
list_a.insert(1,0)
print 'list_a.insert(1,0) =', list_a
list_a.insert(-1,0)
print 'list_a.insert(-1,0) =', list_a

print '\n', list_a.pop.__doc__, '\n'
print 'list_a.pop(0) =', list_a.pop(0), list_a
print 'list_a.pop(2) =', list_a.pop(2), list_a

print '\n', list_a.remove.__doc__, '\n'
list_a.remove(0)
print 'list_a.remove(0) =', list_a

print '\n', list_a.reverse.__doc__, '\n'
list_a.reverse()
print 'list_a.reverse() =', list_a

print '\n', list_a.sort.__doc__, '\n'
list_a.sort()
print 'list_a.sort() =', list_a

print '\n', '引用类型和值类型的区别'
list_b = list_a
print 'list_a =', list_a
print 'list_b =', list_b
list_b.reverse()
print 'list_b.reverse()'
print 'list_a =', list_a
print 'list_b =', list_b

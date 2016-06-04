#! /usr/bin/python
# encoding: utf-8

class Parallelogram(object): pass

class Rectangle(Parallelogram): pass

class Sqaure(Parallelogram): pass

po = Parallelogram()
ro = Rectangle()
so = Sqaure()

print '\nSqaure is instance of Parallelogram: ', isinstance(so,Parallelogram)
print '\nRectangle is instance of Parallelogram: ', isinstance(ro,Parallelogram)
print '\nSqaure is instance of Rectangle: ', isinstance(so,Rectangle)
print '\n'

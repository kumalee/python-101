#! /usr/bin/python
# encoding: utf-8

class Shape(object):
    def __init__(self, width, height):
        self.length = width, height

    def setLength(self, width, height):
        self.length = width, height

    def getLength(self):
        return self.length

    def getName(self): pass

class Parallelogram(Shape):
    def __init__(self, width, height, deg):
        Shape.__init__(self, width, height)
        self.deg = deg

    def setDeg(self, deg):
        self.deg = deg

    def getDeg(self):
        return self.deg

    def getName(self):
        return 'Parallelogram'

class Rectangle(Shape):
    def getDeg(self):
        return 90

    def getName(self):
        return 'Rectangle'

class Sqaure(Shape):
    def __init__(self, width):
        self.length = width

    def setLength(self, width):
        self.length = width

    def getDeg(self):
        return 90

    def getName(self):
        return 'Sqaure'

po = Parallelogram(10, 20, 15)
ro = Rectangle(30, 40)
so = Sqaure(50)

print '\nParallelogram\'s length =', po.getLength(), ' deg =', po.getDeg()
print '\nRectangle\'s length =', ro.getLength(), ' deg =', ro.getDeg()
print '\nSqaure\'s length =', so.getLength(), ' deg =', so.getDeg()

po.setDeg(90)
print '\nParallelogram\'s deg =', po.getDeg()

print '\n'

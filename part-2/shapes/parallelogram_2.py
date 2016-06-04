#! /usr/bin/python
# encoding: utf-8

class Parallelogram(object):
    def __init__(self, width, height, deg):
        self.length = width, height
        self.deg = deg

    def setDeg(self, deg):
        self.deg = deg

    def getDeg(self):
        return self.deg

    def setLength(self, width, height):
        self.length = width, height

    def getLength(self):
        return self.length

    def getName(self):
        return 'Parallelogram'

class Rectangle(Parallelogram):
    def getName(self):
        return 'Rectangle'

class Sqaure(Parallelogram):
    def __init__(self, width, deg):
        self.length = width
        self.deg = deg

    def setLength(self, width):
        self.length = width

    def getName(self):
        return 'Sqaure'

po = Parallelogram(10, 20, 15)
ro = Rectangle(30, 40, 90)
so = Sqaure(50, 90)

print '\nParallelogram\'s length =', po.getLength(), ' deg =', po.getDeg()
print '\nRectangle\'s length =', ro.getLength(), ' deg =', ro.getDeg()
print '\nSqaure\'s length =', so.getLength(), ' deg =', so.getDeg()
print '\n'

# ro.setDeg(100)
# so.setDeg(100)
#
# print '\nRectangle\'s deg =', ro.deg
# print '\nSqaure\'s deg =', so.deg

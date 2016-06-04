#! /usr/bin/python
# encoding: utf-8

import math

class Shape(object):
    def __init__(self, width, height):
        self.length = width, height

    def setLength(self, width, height):
        self.length = width, height

    def getLength(self):
        return self.length

    def getName(self): pass

    def getDeg(self):
        return 0

    def getArea(self):
        return self.length[0] * self.length[1] * math.sin(math.radians(self.getDeg()))

    def isSame(self, shape2):
        return self.getLength() == shape2.getLength() and \
            self.getDeg() == shape2.getDeg() and \
            self.getName() == shape2.getName() and \
            self.getArea() == shape2.getArea()

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
        self.length = width, width

    def setLength(self, width):
        self.length = width

    def getDeg(self):
        return 90

    def getName(self):
        return 'Sqaure'

po = Parallelogram(10, 20, 15)
ro = Rectangle(50, 50)
so = Sqaure(50)
so2 = Sqaure(50)

print so.isSame(ro)
print so.isSame(po)
print so.isSame(so2)

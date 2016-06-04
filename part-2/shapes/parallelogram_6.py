#! /usr/bin/python
# encoding: utf-8

import math

class Parallelogram(object):
    def __init__(self, width, height, deg):
        self.length = width, height
        self.deg = deg

    def setLength(self, width, height):
        self.length = width, height

    def getLength(self):
        return self.length

    def setDeg(self, deg):
        self.deg = deg

    def getDeg(self):
        return self.deg

    def getArea(self):
        return self.length[0] * self.length[1] * math.sin(math.radians(self.deg))

    def getName(self):
        if self.length[0] == self.length[1] and self.deg == 90:
            return 'Sqaure'
        elif self.length[0] != self.length[1] and self.deg == 90:
            return 'Rectangle'
        else:
            return 'Parallelogram'

po = Parallelogram(10,15,30)

print '\n po is a', po.getName(), ' with length', po.getLength(), \
    ' and deg', po.getDeg(), ' and area', po.getArea()
po.setDeg(90)
print '\n po is a', po.getName(), ' with length', po.getLength(), \
    ' and deg', po.getDeg(), ' and area', po.getArea()
po.setLength(10,10)
print '\n po is a', po.getName(), ' with length', po.getLength(), \
    ' and deg', po.getDeg(), ' and area', po.getArea()
print '\n'

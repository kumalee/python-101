#! /usr/bin/python
# encoding: utf-8

class car(object):
    '''
    This class the base of car.
    
    '''
    def __init__(self, brand, color, types):
        self.brand = brand
        self.color = color
        self.types = types
        self.speed = 0
        self.running = False

    def start(self):
        self.running = True
        self.speedup()

    def stop(self):
        self.running = False
        self.speed = 0

    def speedup(self, unit=10):
        self.speed += unit

    def status(self):
        isRun = 'running' if self.running else 'not running'
        print '请安全驾驶'
        print 'A {color} {brand} {types} is {isRun}'.format(color=self.color, brand=self.brand, types=self.types, isRun=isRun)

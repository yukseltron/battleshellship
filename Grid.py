# -*- coding: utf-8 -*-
import Point as point
from random import randint

class Grid():

    def __init__(self):
        self.d = 10
        self.matrix = [[" " for x in range(self.d)] for y in range(self.d)]

    def printGrid(self):
        print "0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9"
        print "/////////////////////////////////////////"

        for i in range(self.d):
            for j in range(self.d):
                print self.matrix[j][i], "|",
            print "/",i
            print "---------------------------------------"

    def setGrid(self, values):
        for i in values:
            self.matrix[i.getX()][i.getY()] = i.getS()

    def setPoint(self, x, y, s):
        self.matrix[x][y] = s

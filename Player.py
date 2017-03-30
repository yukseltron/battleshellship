# -*- coding: utf-8 -*-
import Grid as grid
import Point as point
from random import randint

class Player():
    def __init__(self):
        self.g1 = grid.Grid()
        self.g2 = grid.Grid()
        self.ships = []
        self.hits = []
        self.misses = []
        self.damage = []

    def randomFill(self):
        self.ships.append(self.possibleShips(5))
        self.ships.append(self.possibleShips(4))
        self.ships.append(self.possibleShips(3))
        self.ships.append(self.possibleShips(3))
        self.ships.append(self.possibleShips(2))

        for i in range(len(self.ships)):
            self.g1.setGrid(self.ships[i])

    def possibleShips(self, length):
        x = randint(0,9)
        y = randint(0,9)
        a = []
        b = []#auxiliary list for a
        for i in range(length):
            p = point.Point(x-i,y,"▄")
            if (self.isValidG1(p, self.ships) == False):
                b = []
                break
            else:
                b.append(p)

        if b:
            a.append(b)
            b = []

        for i in range(length):
            p = point.Point(x+i,y,"▄")
            if (self.isValidG1(p, self.ships) == False):
                b = []
                break
            else:
                b.append(p)

        if b:
            a.append(b)
            b = []

        for i in range(length):
            p = point.Point(x,y-i,"█")
            if (self.isValidG1(p, self.ships) == False):
                b = []
                break
            else:
                b.append(p)

        if b:
            a.append(b)
            b = []

        for i in range(length):
            p = point.Point(x,y+i,"█")
            if (self.isValidG1(p, self.ships) == False):
                b = []
                break
            else:
                b.append(p)

        if b:
            a.append(b)
            b = []

        if not a:
            return self.possibleShips(length)

        r = randint(0,len(a)-1)

        return a[r]

    def isValidG1(self, p, a):
        if (p.getX() < 0 or p.getX() > 9 or p.getY() < 0 or p.getY() > 9):
            return False
        for i in range(len(a)):
            for j in range(len(a[i])):
                if (p.getX() == a[i][j].getX() and p.getY() == a[i][j].getY()):
                    return False
        return True

    def isValidG2(self, p):
        if (p.getX() < 0 or p.getX() > 9 or p.getY() < 0 or p.getY() > 9):
            return False
        if (self.g2.matrix[p.getX()][p.getY()] != " "):
            return False
        return True

    def printGrid1(self):
        self.g1.printGrid()

p = Player()
p.randomFill()
p.printGrid1()

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
        self.damage = 0

    def randomFill(self):
        self.ships.append(self.possibleShips(5))
        self.ships.append(self.possibleShips(4))
        self.ships.append(self.possibleShips(3))
        self.ships.append(self.possibleShips(3))
        self.ships.append(self.possibleShips(2))
        self.updateGrid1(self.ships)

    #Finds all possibilites for ship placement based on length, then randomly chooses the best one.
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

    #Success of a player attack
    def attack(self,enemy,x,y):
        p = point.Point(x, y, "X")
        for i in enemy:
            for j in i:
                if (x == j.getX() and y == j.getY()):
                    self.hits.append(p)
                    self.updateGrid2(self.hits)
                    return True
        p.setS("O")
        self.misses.append(p)
        self.updateGrid2(self.misses)
        return False

    #For when player gets hit
    def getHit(self,x,y):
        self.damage += 1
        self.g1.setPoint(x,y,"X")
        
    #Checks if it is a valid point on ship graph
    def isValidG1(self, p, a):
        if (p.getX() < 0 or p.getX() > 9 or p.getY() < 0 or p.getY() > 9):
            return False
        for i in range(len(a)):
            for j in range(len(a[i])):
                if (p.getX() == a[i][j].getX() and p.getY() == a[i][j].getY()):
                    return False
        return True

    #Checks if it is a valid point on attack graph
    def isValidG2(self, p, a):
        if (p.getX() < 0 or p.getX() > 9 or p.getY() < 0 or p.getY() > 9):
            return False
        for i in range(len(a)):
            for j in range(len(a[i])):
                if (p.getX() == a[i][j].getX() and p.getY() == a[i][j].getY()):
                    return False
        return True

    #To update ship grid
    def updateGrid1(self, values):
        for i in range(len(values)):
            self.g1.setGrid(values[i])

    #To update attack grid
    def updateGrid2(self, values):
        self.g2.setGrid(values)

    def printGrid1(self):
        self.g1.printGrid()

    def printGrid2(self):
        self.g2.printGrid()

# -*- coding: utf-8 -*-
from random import randint

class Grid():
    def __init__(self):
        self.width = 10
        self.height = 10
        self.Matrix = [[" " for x in range(self.width)] for y in range(self.height)]

    def printGrid(self):
        print "0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9"
        print "/////////////////////////////////////////"
        for i in range(self.width):
            for j in range(self.height):
                print self.Matrix[i][j], "|",
            print "/",i
            print "---------------------------------------"

    def fillGrid(self, x, y):
        if (self.isValid(int(x),int(y))):
            self.Matrix[int(y)][int(x)] = "█"

    def isValid(self, x, y):
        if (x >= 0 and x < self.width and y >= 0 and y < self.width and self.Matrix[x][y] == " "):
            return True

        return False

    def notElementOf(self, valid, x, y):
        for i in range(len(valid)):
            if (x in valid[i] or y in valid[i]):
                return False

        return True

    def randomFill(self, length):
        x = randint(0,9)
        y = randint(0,9)
        validN = []
        validS = []
        validW = []
        validE = []
        valid = []

        if (self.isValid(x, y)):
            for i in range(length):
                if (self.isValid(x-i,y)):
                    validN.extend(str(x-i))
                    validN.extend(str(y))
                else:
                    validN[:] = []
                    break

            for i in range(length):
                if (self.isValid(x+i,y) and self.notElementOf([validN], x+1, y)):
                    validS.extend(str(x+i))
                    validS.extend(str(y))
                else:
                    validS[:] = []
                    break

            for i in range(length):
                if (self.isValid(x,y-i) and self.notElementOf([validN, validS], x, y-1)):
                    validW.extend(str(x))
                    validW.extend(str(y-i))
                else:
                    validW[:] = []
                    break

            for i in range(length):
                if (self.isValid(x,y+i) and self.notElementOf([validN, validS, validW], x, y+1)):
                    validE.extend(str(x))
                    validE.extend(str(y+i))
                else:
                    validE[:] = []
                    break

        valid.append(validN)
        valid.append(validS)
        valid.append(validW)
        valid.append(validE)

        r = randint(0,len(valid)-1)

        if not valid[r]:
            self.randomFill(length)
        else:
            for i in range(0,len(valid[r])-1,2):
                self.fillGrid(valid[r][i], valid[r][i+1])

    def choseRandom(self):
        self.randomFill(5)
        self.randomFill(4)
        self.randomFill(3)
        self.randomFill(3)
        self.randomFill(2)

g = Grid()
g.choseRandom()
g.printGrid()

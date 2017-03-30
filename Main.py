class Main():
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

    def fillGrid(self, x, y):
        if (isValid(x,y)):
            self.Matrix[y][x] = 1

    def isValid(self, x, y):
        if (x >= 0 and x <= self.width and y >= 0 and y <= self.width and self.Matrix[x][y] == 0):
            return True

        return False

m = Main()
m.fillGrid(1,2)
m.printGrid()

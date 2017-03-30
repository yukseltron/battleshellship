class Main():
    def __init__(self):
        self.width = 10
        self.height = 10
        self.Matrix = [[0 for x in range(self.width)] for y in range(self.height)]

    def printGrid(self):
        for i in range(self.width):
            for j in range(self.height):
                print(self.Matrix[i][j], "|")
            print("__________")

    def fillGrid(self, array):
        for i in range(len(array)-1):
            self.Matrix[i][i+1] = 1

m = Main()
m.printGrid()

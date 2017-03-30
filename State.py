import Grid as grid

class State():
    def menu(self):
        print("//B A T T L S H E L L S H I P//")
        n = input("Enter number of players: ")
        if (n == 1):
            print("Player vs Robot")
        elif (n == 2):
            print("Player1 vs Player2")
        else:
            print("invalid input, please try again.")
            self.menu()

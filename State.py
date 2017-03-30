import Player as player

class State():
    p1 = player.Player()
    p1.randomFill()
    p2 = player.Player()
    p2.randomFill()

    @staticmethod
    def menu():
        print("<<< B A T T L E S H E L L S H I P >>>")
        n = input("Enter number of players:")
        if (n == 1):
            print("Single player mode coming soon!")
            State.menu()
        elif (n == 2):
            State.twoPlayerMode1()
        else:
            menu()

    #@staticmethod
    #def onePlayerMode():

    @staticmethod
    def twoPlayerMode1():
        print("PLAYER1 SHIPS")
        State.p1.printGrid1()
        print("PLAYER1 ATTACK")
        State.p1.printGrid2()
        x = input("ENTER X-TARGET: ")
        y = input("ENTER Y-TARGET: ")
        if (State.p1.attack(State.p2.ships,x,y)):
            State.p2.getHit(x,y)
        if (State.winner() == 1):
            State.gameOver(State.winner())
        State.twoPlayerMode2()

    @staticmethod
    def twoPlayerMode2():
        print("PLAYER2 SHIPS")
        State.p2.printGrid1()
        print("PLAYER2 ATTACK")
        State.p2.printGrid2()
        x = input("ENTER X-TARGET: ")
        y = input("ENTER Y-TARGET: ")
        if (State.p2.attack(State.p1.ships,x,y)):
            State.p1.getHit(x,y)
        if (State.winner() == 2):
            State.gameOver(State.winner())
        State.twoPlayerMode1()

    @staticmethod
    def winner():
        if (State.p1.damage == 17):
            return 2
        elif (State.p2.damage == 17):
            return 1
        return 0

    @staticmethod
    def gameOver(p):
        print "PLAYER",p,"wins!"
        quit()

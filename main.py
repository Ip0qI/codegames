import sys
class Game:
    def __init__(self):
        self.game_dict = {}
        file = open('dummy/gList.txt', 'r')
        content = file.read()
        file.close()
        while True:
            try:
                gamesNum,GNint = map(str, sys.stdin.readline().split(':'))
                print(gamesNum,"      ",GNint)
                GNint = int(GNint)
                self.game_dict[gamesNum] = GNint
                print(self.game_dict)
            except:
                break
'''
        gamesNum, GNint = map(str, sys.stdin.readline().split(':'))
        GNint = int(GNint)
        self.game_dict[gamesNum] = GNint
        for i in range(GNint):
            print(i)
            game,number=map(int, sys.stdin.readline().split())
            self.game_dict[game]=number
            print(self.game_dict)
'''

G=Game()
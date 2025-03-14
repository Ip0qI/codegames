class cham:
    def __init__(self, num):
        self.name = "cham"
        self.num = num

    def converter(self, inStr):
        dir={1:["up", "상", "위", "위쪽"], 2:["down", "아래", "아래쪽", "하"], 3:["left", "좌", "좌측", "왼쪽"], 4:["right", "우", "우측", "오른쪽"]}
        keywords = {dir, "/help", "reset", "leave"}
        if inStr == int:
            if inStr == 1:
                return "up"
            elif inStr == 2:
                return "down"
            elif inStr == 3:
                return "left"
            elif inStr == 4:
                return "right"
        elif inStr == str:
            if inStr in dir[1]:
                return 1
            elif inStr in dir[2]:
                return 2
            elif inStr in dir[3]:
                return 3
            elif inStr in dir[4]:
                return 4
            else:
                return 0
        self.info = print(f"keyword\ndirecion: {self.converter.dir[1]}, {self.converter.dir[2]}, {self.converter.dir[3]}, {self.converter.dir[4]}\ncommand\n/help, reset, leave")
        self.infoDetail = print("command\n/help:popup comment about avaliable keywords\nreset: start this game from the firts\nleave: leave this game and go back to the main menu")
        self.infoHelp = print("help/popup comment about avaliable keywords")
        self.infoReset = print("reset/start this game from the firts")
        self.infoLeave = print("leave/leave this game and go back to the main menu")

    def preparance(self, numStr: str):
        print(f"welcome to our {numStr} game, \"참참참\"")
        self.start()

    def turn(self, turn):
        if turn == 1:
            self.turn = "user"
        elif turn == 2:
            self.turn = "bot"
        return self.turn

    def start(self):
        from random import randint as rd
        print("let's start the game!")
        startTurn = rd(1, 2)
        print(startTurn)
        print(self.turn(startTurn))
        print(f"the first turn is {self.turn(startTurn)}")
        self.game()

    def game(self):
        from random import randint as rd
        from time import sleep as slp
        #턴 선택 방식 개발 필요
        self.userPoint = 0
        self.botPoint = 0
        while True:
            print("attack: {self.turn}")
            botDirection = rd(1, 4)
            while True:
                #입력 받고 변환
                userInput = input('please enter the direction\nup, down, left, right : ')
                if userInput in self.converter.keywords:
                    if userInput in self.converter.dir:
                        userDirection = self.converter(userInput)
                        break
                    elif userInput == "/help":
                        self.converter.info
                        pass
                    elif userInput == "reset":
                        self.start()
                        pass
                    else:
                        print("please enter the correct direction\nfor more information, please enter /help")
                        pass
                break
            
            #승자확인, 점수 계산
            if userDirection != botDirection:
                if self.turn(self.turnNum) == "user":
                    self.turnNum = 2
                elif self.turn(self.turnNum) == "bot":
                    self.turnNum = 1
            else:
                if self.turn(self.turnNum) == "user":
                    self.userPoint += 1
                elif self.turn(self.turnNum) == "bot":
                    self.botPoint += 1
            
            #게임진행, 정보 표시시
            print("cham!")
            slp(1)
            print("cham!")
            slp(1)
            print("cham!")
            print(f"user: {self.userDirection}\nbot: {self.botDirection}\nwinner: {self.turn(self.turnNum)}")

            print(f"current point\nuser: {self.userPoint}\nbot: {self.botPoint}")

            #변수명 이용한 승자 확인 개발 요망

Cham=cham(1)
Cham.preparance("first")
#왜 ㅆ발 함수 타입 에러가 뜨냐고 썅

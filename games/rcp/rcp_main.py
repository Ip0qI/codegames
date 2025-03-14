rcpc=['rock','scissors','paper']
rpc={1:'rock',2:'scissors',3:'paper'}
aiscore=int(0)
yourscore=int(0)
import rcppd
import time
from random import randrange
print("hi friend! let's play rock paper scissors!\nif you want to stop this game, say 'good bye'\nif you want to reset the score, say'restart'")
while True:
    while True:
        AI=randrange(4)
        if 0<AI<4:
            break
    while True:
        You=input('You:')
        if You=='restart':
            aiscore=int(0)
            yourscore=int(0)
            print("you've successfully reset the score!\nnow let's play again!")
        elif You in rcpc:
            if rcppd.pd(AI,You)=='AI':
                aiscore+=int(1)
            if rcppd.pd(AI,You)=='You':
                yourscore+=int(1)
            print('rock...')
            time.sleep(0.5)
            print('scissors...')
            time.sleep(0.75)
            print('paper!')
            time.sleep(0.08)
            print(f'AI:{rpc[AI]} vs You:{You}\n{rcppd.pd(AI,You)} win!\npoint/AI:{aiscore}    You:{yourscore}')
            break
        elif You=='good bye':
            print("good bye!\nit's now turning off...")
            time.sleep(2)
            print('wait for a minaute')
            time.sleep(7.231)
            print("tada!\nlolll\nlet's play it again next time.")
            exit()
        elif You=='?':
            print("if you want to stop playing game, please say 'good bye'\nif you want to reset the score, say'restart")
        else:
            print("that's worng answer.\nplease write in a right one")
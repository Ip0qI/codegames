usdir=['왼쪽','오른쪽','위쪽','아래쪽']
from time import sleep as s
import chmpd
from chmpd import wat as t
from sys import exit
usp=0
aip=0
print(f"끝내려면 '잘가' 입력\n점수 초기화는 '재시작' 입력\n선공은 랜덤으로!\n3!")
s(0.3)
print('2!')
s(0.3)
print("1!")
s(0.3)
w=chmpd.pd()
print(f'시작\n선공// -{w}-\n{usdir} 중에 하나를 입력.')
while True:
    AI=chmpd.rai()
    while True:
        user=input('유저:')
        user=chmpd.lst(user)
        if user in usdir:
            break
        elif user=='off':
            print('- ^ -')
            s(1.3)
            exit('good bye')
        elif user=='restart':
            aip=0
            usp=0
            print('재시작 성공')
            w=chmpd.pd()
            print(f'선공// -{w}-')
            continue
        elif user=='?':
            print(f"사용 가능한 명령어:'잘가','재시작','?'\n'잘가':게임 종료\n'재시작':점수 초기화/재시작\n'?'/'help':도움말")
        elif user=='rkdwlgnsqkqh':
            usp+=1
            continue
    a2=chmpd.wpd(AI,user)
    if a2=='성공!':
        if w=='AI':
            w='AI'
            aip+=1
        else:
            w='유저'
            usp+=1
    print('참..')
    s(0.45)
    print('참...')
    s(0.51)
    print('참!')
    s(0.013)
    a=w
    b=t(w)
    print(f'{a}(공격):{chmpd.d(user,AI,a)}   {b}(수비):{chmpd.b(user,AI,b)}\n{w} 공격 {a2}\n     -점수-\n유저:{usp}   AI:{aip}')
    if a2=='실패...':
        w=t(w)
    print(f'공격// -{w}-')
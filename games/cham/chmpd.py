from random import randint as r
ai={1:'왼쪽',2:'오른쪽',3:'위쪽',4:'아래쪽'}
usd={'좌':'왼쪽','우':'오른쪽','상':'위쪽','하':'아래쪽','up':'위쪽','down':'아래쪽','left':'왼쪽','right':'오른쪽','위':'위쪽','아래':'아래쪽','w':'위쪽','s':'아래쪽','a':'왼쪽','d':'오른쪽','help':'?'}
def pd():
    while True:
        cn=r(1,4)
        an=r(1,4)
        if an!=cn:
            break
    if an<cn:
        return('AI')
    elif an>cn:
        return('유저')
def lst(user):
    if user in usd:
        return(usd[user])
    else:
        return(user)
def rai():
    return r(1,4)
def wpd(AI,user):
    if user==ai[AI]:
        return('성공!')
    elif user!=ai[AI]:
        return('실패...')
def wat(w):
    if w=='AI':
        return('유저')
    else:
        return('AI')
def a(AI):
    return(ai[AI])
def d(user,AI,a):
    if a=='유저':
        return(user)
    else:
        return(ai[AI])
def b(user,AI,b):
    if b=='유저':
        return(user)
    else:
        return(ai[AI])
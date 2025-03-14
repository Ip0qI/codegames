rcp={'가위':2,'바위':1,'보':3}
def pd(AI,You):
    while True:
        if AI==rcp[You]:
            w=('no one')
        else:
            a=AI-rcp[You]
            if a==-1 or a==2:
                w=('AI')
            elif a==1 or a==-2:
                w=('You')
            return(w)
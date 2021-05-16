import random

pl=input('Enter your choice Rock(r) , Paper(p), Scissors(s): ')
c= random.randint(1,3)
if(c==1):
    c='Rock'
elif(c==2):
    c='Paper'
elif(c==3):
    c='Scissors'

if(pl=='r'):
    pl='Rock'
elif(pl=='p'):
    pl='Paper'
elif(pl=='s'):
    pl='Scissors'


def game(c,pl):
    if(c==pl):
        return None
    elif(c=='Rock'):
        if(pl=='Paper'):
            return True
        elif(pl=='Scissors'):
            return False
    elif(c=='Paper'):
        if(pl=='Rock'):
            return False
        elif(pl=='Scissors'):
            return True
    elif(c=='Scissors'):
        if(pl=='Paper'):
            return False
        elif(pl=='Rock'):
            return True
    
print(f'Computer chose: {c}')
print(f'You chose: {pl}')

a=game(c,pl)

if a==True:
    print('You Won')
elif a==False:
    print('You Lost')
elif a==None:
    print('It is a Tie')



    
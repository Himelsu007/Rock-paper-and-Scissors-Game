from random import randint
from time import sleep


probabilities = ('PAPER', 'STONE','SCISSOR')
pc = randint(0,2)
y = ['Yes', 'yes','yup','y','YEAH','Yeah','yeah','yessir','yEah', 'yy','ye']
n = ['No' , 'no','nah','hell nah','nope','Nope','NOPE','Not', 'NOPE','n']
name = str(input('Insert Your name: ')).upper()

print( f'''Welcome {name}, Take a look at your options...
【0】 - PAPER
【1】 - STONE
【2】 - SCISSOR''')

print('_'*34)

play = int(input('Insert a number between 0 and 2: '))

def space():
    print( 'The computer is playing... [⌛]')
    sleep(1)
    print('③')
    sleep(1)
    print('②')
    sleep(1)
    print('①')
    sleep(1)

space()

if pc == 0 and play == 0:
    print( '⚫ TIE ⚫')
elif pc == 1 and play == 1:
    print( '⚫ TIE ⚫')
elif pc == 2 and play == 2:
    print( '⚫ TIE ⚫')
elif pc == 0 and play == 1:
    print(f'Maybe next time {name} ☹')
elif pc == 0 and play == 2:
    print( f'Congratulations {name} , you won! 🎉')
elif play == 0 and pc == 1:
    print(f'Congratulations {name} , you won! 🎉')
elif play == 0 and pc == 2:
    print(f'Maybe next time {name} ☹')
elif play == 1 and pc == 2:
    print(f'Congratulations {name} , you won! 🎉')
elif play == 2 and pc == 1:
    print(f'Maybe next time {name} ☹')
elif play == 2 and pc == 0:
    print(f'Congratulations {name} , you won! 🎉')

def results ():
    print('-' * 34)
    print(f'The coputer has chosen ▶ {probabilities[pc]}')
    print('-' * 34)
    print(f'You chose ▶ {probabilities[play]}')
    print('-' * 34)

def yn ():
    print('_' * 34)
    res = str(input('Do you want to see the results and Quit? [yes/no] '))
    if res in y:
        print(results())
        print('-=' * 45)
        print('------------------------------------ Play Again!----------------------------------' )
        print('-=' * 45)
    elif res in n:
        print('Thanks for playing!')
yn()
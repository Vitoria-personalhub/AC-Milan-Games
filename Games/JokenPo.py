print(' ')

print('\033[35m JOKENPO \033[m')
print(' ')

from random import randint

items = ('\033[37mRock\033[m 🌚', '\033[34mPaper\033[m 🗒', '\033[31mScissor\033[m ✂')

print('''\033[1mPlayer Options\033[m''')
print('''
\033[37m0 - Rock\033[m 🌚
\033[34m1 - Paper\033[m 🗒
\033[31m2 - Scissor\033[m ✂
''')
print(' ')
player = int(input('Number corresponding to the move: '))

print('-=' * 15)
if player == 0:
    print('Player choose \033[37mRock\033[m 🌚')
elif player == 1:
    print('Player choose \033[34mPaper\033[m 🗒')
elif jogador == 2:
    print('Player choose \033[31mScissor\033[m ✂')

from time import sleep

print('___')
print('The computer are thinking...👾')
sleep(4)
print('___')

computer = randint(0, 2)
print('Computer choose {}'.format(items[computer]))

print('-=' * 15)

if computer == 0:  #computer choose rock
    if player == 0:  # player choose rock
        print('\033[33mDRAW\033[m')

    elif player == 1:  # player choose paper
        print('\033[32mPLAYER WINS\033[m')

    elif player == 2:  # player choose scissor
        print('\033[31mCOMPUTER WINS\033[m')

    else:
        print('\033[31mINVALID PLAY\033[m')

elif computer == 1:  #computer choose paper
    if player == 0:  # player choose rock
        print('\033[31mCOMPUTER WINS\033[m')

    elif player == 1:  #player choose paper
        print('\033[33mDRAW\033[m')

    elif jogador == 2:  #player choose scissor
        print('\033[32mPLAYER WINS\033[m')

    else:
        print('\033[31mINNVALID PLAY\033[m')

elif computador == 2:  #computer choose scissor
    if jogador == 0:  # player choose rock
        print('\033[32mPLAYER WINS\033[m')

    elif jogador == 1:  #player choose paper
        print('\033[31mCOMPUTER WINS\033[m')

    elif jogador == 2:  #player choose scissor
        print('\033[33mDRAW\033[m')

    else:
        print('\033[31mINVALID PLAY\033[m')

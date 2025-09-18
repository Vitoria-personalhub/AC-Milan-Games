print('_' * 70)
print(' ')
print('''Crie um programa que faça o computador jogar jokenpô com você.''')
print(' ')
print('_' * 70)
print(' ')

print('\033[35mPEDRA, PAPEL, TESOURA\033[m')
print(' ')

from random import randint

itens = ('\033[37mPedra\033[m 🌚', '\033[34mPapel\033[m 🗒', '\033[31mTesoura\033[m ✂')

print('''\033[1mOpções do Jogador\033[m''')
print('''
\033[37m0 - Pedra\033[m 🌚
\033[34m1 - Papel\033[m 🗒
\033[31m2 - Tesoura\033[m ✂
''')
print(' ')
jogador = int(input('Número correspondente a jogada: '))

print('-=' * 15)
if jogador == 0:
    print('O jogador escolheu \033[37mPedra\033[m 🌚')

elif jogador == 1:
    print('O jogador escolheu \033[34mPapel\033[m 🗒')
elif jogador == 2:
    print('O jogador escolheu \033[31mTesoura\033[m ✂')

from time import sleep

print('___')
print('O computador está pensando...👾')
sleep(4)
print('___')

computador = randint(0, 2)
print('O computador escolheu {}'.format(itens[computador]))

print('-=' * 15)

if computador == 0:  #computador jogou pedra
    if jogador == 0:  # jogador jogou pedra
        print('\033[33mEMPATE\033[m')

    elif jogador == 1:  #jogador jogou papel
        print('\033[32mJOGADOR VENCE\033[m')

    elif jogador == 2:  #jogador jogou tesoura
        print('\033[31mCOMPUTADOR VENCE\033[m')

    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')

elif computador == 1:  #computador jogou papel
    if jogador == 0:  # jogador jogou pedra
        print('\033[31mCOMPUTADOR VENCE\033[m')

    elif jogador == 1:  #jogador jogou papel
        print('\033[33mEMPATE\033[m')

    elif jogador == 2:  #jogador jogou tesoura
        print('\033[32mJOGADOR VENCE\033[m')

    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')

elif computador == 2:  #computador jogou tesoura
    if jogador == 0:  # jogador jogou pedra
        print('\033[32mJOGADOR VENCE\033[m')

    elif jogador == 1:  #jogador jogou papel
        print('\033[31mCOMPUTADOR VENCE\033[m')

    elif jogador == 2:  #jogador jogou tesoura
        print('\033[33mEMPATE\033[m')

    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')

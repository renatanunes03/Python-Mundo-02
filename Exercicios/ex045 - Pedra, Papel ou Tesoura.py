print('{:^40}'.format('Exercício 45'))
print('Gerenciados de Pagamentos')
print('Crie um programa que faça o computador jogar Jokenpô com você.'
'Pedra, papel e tesoura.'
'o computador escolhe uma opção e eu escolho outra.'
'E demonstro quem ganhou.')
from random import randint
from time import sleep
while True:
    try:
        itens = ('Pedra', 'Papel', 'Tesoura')
        computador = randint(0, 2)

        jogador = int(input('Escolha:\n'
                            '[0] Pedra\n'
                            '[1] Papel\n'
                            '[2] Tesoura\n'
                            'Qual sua jogada?'))
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        sleep(1)
        print('-=' * 13)
        print(f'Computador escolheu {itens[computador]}')
        print(f'Jogador escolheu {itens[jogador]}')
        print('-=' * 13)
        if itens[computador] == itens[jogador]:
            print(f'EMPATE!')
            print('-=' * 13)
        elif computador == 0: #computador opcao pedra
            if jogador == 1: #jogador opcao papel
                print('JOGADOR VENCEU!')
                print('-=' * 13)
            elif jogador == 2: #jogador tesoura
                print('COMPUTADOR VENCEU!')
                print('-=' * 13)
        elif computador == 1: #computador papel
            if jogador == 0: # jogador pedra
                print('COMPUTADOR VENCEU!')
                print('-=' * 13)
            elif jogador == 2: #jogador tesoura
                print('JOGADOR VENCEU!')
                print('-=' * 13)
        elif computador == 2: #computador tesoura
            if jogador == 0: #jogador pedra
                print('JOGADOR VENCEU!')
                print('-=' * 13)
            elif jogador == 1: #jogador papel
                print('COMPUTADOR VENCEU!')
                print('-=' * 13)
    except:
        print('Digite uma opção válida!')



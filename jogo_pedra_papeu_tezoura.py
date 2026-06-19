import random

score_maq = 0
score_jogador = 0


opcao_maq  =  ['','✂️','🪨','🧻']
escolha_maq = random.choice(opcao_maq[1:])

opcao_jogador  =  ['','1 - ✂️','2 - 🪨','3 - 🧻']
escolha_jog = int(input(f'Escolha uma {opcao_jogador[1:]}'))


if opcao_maq.index(escolha_maq) == escolha_jog:
        print('Empate...')
        print('Pontos Jogador - ', score_jogador)
        print('Pontos Máquina - ', score_maq)
        print('Maquina:', escolha_maq, 'Jogador: ', opcao_jogador[escolha_jog])

elif opcao_maq.index(escolha_maq) == 1 and escolha_jog == 3:
        print(' A MAQUINA VENCEU ... ')
        print('Pontos Jogador - ', score_jogador)
        score_maq  = score_maq  + 1
        print('Pontos Máquina - ', score_maq )
        print('Maquina:', escolha_maq, 'Jogador: ', opcao_jogador[escolha_jog])

elif opcao_maq.index(escolha_maq) == 2 and escolha_jog == 1:
    print(' A MAQUINA VENCEU ... ')
    print('Pontos Jogador - ', score_jogador)
    score_maq  = score_maq  + 1
    print('Pontos Máquina - ', score_maq )  
    print('Maquina:', escolha_maq, 'Jogador: ', opcao_jogador[escolha_jog])

elif opcao_maq.index(escolha_maq) == 3 and escolha_jog == 2:
    print(' A MAQUINA VENCEU ... ')
    print('Pontos Jogador - ', score_jogador)
    score_maq  = score_maq  + 1
    print('Pontos Máquina - ', score_maq )
    print('Maquina:', escolha_maq, 'Jogador: ', opcao_jogador[escolha_jog])

else:
    print(' VOCÊ VENCEU!!!!  ')
    score_jogador  = score_jogador  + 1
    print('Pontos Jogador - ', score_jogador)
    print('Pontos Máquina - ', score_maq )
    print('Maquina:', escolha_maq, 'Jogador: ', opcao_jogador[escolha_jog])
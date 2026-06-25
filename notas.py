# Crie um sistema de notas alunos, com as seguintes operações:
# *Utilize While ou for*

# *Sistema de notas de alunos*

# *Visão do professor*

# Acesso a conta com condicionais

# 3 chances de acessar o sistema

# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média

# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***


print('===🧾 Sistema de Media ===')

for i in range(3):
    senha = input('🔐 Senha: ')

    if senha == '123':
        print('👨🏻‍🏫Professor, Seja bem vindo!')
        n1 = float(input('1️⃣Digite a primeira nota: '))
        n2 = float(input('2️⃣Digite a segunda nota: '))
        n3 = float(input('3️⃣Digite a terceira nota: '))
        media= (n1 + n2 + n3) /3
        print('A media foi:',round(media,2))
        break #para a ação

    else:
        print('⚠️Senha bloqueada')


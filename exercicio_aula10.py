#1 - Faça um programa, utilizando while, que mostre na tela os números de 0 a 1000.

c = 0
while c <= 1000:
    print (c)
    c = c + 1

#2 - Faça um sistema, utilizando while e listas, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

nomes = []
i = 0
while i < 10:
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    nomes.append(nome)
    i += 1

print("\nLista de pessoas:")

i = 0
while i < len(nomes):
    print(nomes[i])
    i += 1

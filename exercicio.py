#Exercício 0:** Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.

#Exercício 1:** Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.

#Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.

#Exercício 3:** Adicione o número 9 à lista `numeros` e imprima a lista atualizada.

#Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.

#Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.


for numero in range(2, 21, 2):
    print(numero)
    
#Exc 1
numero = [1,2,3,4,5,6,7,8,9,10]
print(numero)

#Exc 2
print('Elemento 3:',numero[3])

#Exc 3
numero.append(9)
print('Lista Atualizada:', numero)

#Exc 4
numero.pop(5)
print(numero)

#Exc 5
carros = ["Hb20", "Argo", "Onix"]
final = numero + carros

print(final)

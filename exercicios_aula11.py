# Exercício 1:
# Peça ao usuário para inserir um número e manipule a
# exceção caso ele insira algo que não seja um número inteiro.

print('1️⃣')
try:
    idade = int(input("😊😀🙂 Digite sua idade: "))
    print(f"Sua idade é {idade} anos❗.")
except ValueError:
    print("Você não digitou um número inteiro válido!😡😤👺")


# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão.
# Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

print('2️⃣')
try:
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite o segundo número: '))

    div = numero1 / numero2

    print(f"Resultado da divisão: {div}")

except ZeroDivisionError:
    print('Erro: não é possível dividir por zero!')
except ValueError:
    print('Erro: digite apenas números inteiros!')
    

# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o 
# índice seja inválido(caso imprima um indice que não exista na lista).

print('3️⃣')
lista = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

try:
    indice = int(input("Digite um índice: "))
    print("Valor encontrado:", lista[indice])

except IndexError:
    print("Erro: índice inválido!")

except ValueError:
    print("Erro: digite um número inteiro.")

input("Digite enter para sair")


# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

print('Exercicio 1️⃣')

numero = float(input('Digite um numero: '))

if numero > 0:
    print('⛔ O numero', numero , 'é positivo!')

elif numero < 0:
    print('⛔ O numero', numero , 'é negativo!')

else:
    print('⛔ O numero', numero , 'é zero!')

# 2*
# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

print('Exercicio 2️⃣')
idade = int(input('Qual sua idade? '))

if idade >=16:
    print('UAU! voce já pode votar!')
else:
    print('Poxa, que pena! voce não pode votar')


# 3*
# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.

print('Exercicio 3️⃣')

n = float(input('Digite um numero: '))

if n % 2 == 0:
    print('Seu numero é par!')
else:
    print('Seu numero é ímpar')

# 4*
# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

print('Exercicio 4️⃣')

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

if n1 == n2 and n2 == n3:
    print('Seu triangulo é equilátero')

elif n1 == n2 or n1 == n3 or n2 == n3:
    print('Seu triangulo é isósceles')

else:
    print('Seu triangulo é escaleno')


# 5*
# Determine se um número é múltiplo de 5 e 7.

print('Exercicio 5️⃣')
nu = float(input('Digite um numero e descubra se ele é divisivel: '))

if nu % 5 == 0 and nu % 7 == 0:
    print('Seu numero é divisivel por 5 e por 7✅')

else: 
    print('Seu numero nao é divisivel nem por 5 e nem por 7❌')


# 6*
# Verifique se um número é positivo e maior que 10
print('Exercicio 6️⃣')
num = float(input('Digite um numero: '))

if num >=0 and num >10:
    print('Condição correta')

else:
    print('Condição incorret')

# 7*

# Verifique se um número é divisível por 3 ou 5.

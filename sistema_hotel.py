#   Você foi contratado(a) para desenvolver uma parte do sistema de um hotel.
#O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento 
#das diárias.

#O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.

#O sistema deve oferecer 3 tipos de quartos:
# "Simples", "Duplo" e "Luxo".

# Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.

#Cálculo da Estadia:
    # O usuário deve informar quantos dias cada cliente ficará no hotel.
    # O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***


#Regras Adicionais:
    # Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.***
    # O sistema não deve usar loops (for, while) nem funções criadas por você.**
    # O código deve considerar todos os casos possíveis de escolha dos clientes.*

print('--- Hotel landia🏨 ---')

cliente1_nome = input("Nome do cliente 1: ")
cliente1_idade = int(input("Idade do cliente 1: "))

cliente1_quarto = input("Quarto (Simples, Duplo ou Luxo): ")

if cliente1_quarto == "Simples":
    preco1 = 100
elif cliente1_quarto == "Duplo":
    preco1 = 150
else:
    preco1 = 250

cliente1_dias = int(input("Quantos dias ficará hospedado? "))
total1 = preco1 * cliente1_dias

print()

cliente2_nome = input("Nome do cliente 2: ")
cliente2_idade = int(input("Idade do cliente 2: "))

cliente2_quarto = input("Quarto (Simples, Duplo ou Luxo): ")

if cliente2_quarto == "Simples":
    preco2 = 100
elif cliente2_quarto == "Duplo":
    preco2 = 150
else:
    preco2 = 250

cliente2_dias = int(input("Quantos dias ficará hospedado? "))
total2 = preco2 * cliente2_dias

print()


cliente3_nome = input("Nome do cliente 3: ")
cliente3_idade = int(input("Idade do cliente 3: "))

cliente3_quarto = input("Quarto (Simples, Duplo ou Luxo): ")

if cliente3_quarto == "Simples":
    preco3 = 100
elif cliente3_quarto == "Duplo":
    preco3 = 150
else:
    preco3 = 250

cliente3_dias = int(input("Quantos dias ficará hospedado? "))
total3 = preco3 * cliente3_dias

print()

clientes = [cliente1_nome, cliente2_nome, cliente3_nome]
totais = [total1, total2, total3]

print("===== RESUMO DAS RESERVAS =====")

print(f"Cliente: {cliente1_nome}")
print(f"Idade: {cliente1_idade}")
print(f"Valor total: R${total1:.2f}")
print()

print(f"Cliente: {cliente2_nome}")
print(f"Idade: {cliente2_idade}")
print(f"Valor total: R${total2:.2f}")
print()

print(f"Cliente: {cliente3_nome}")
print(f"Idade: {cliente3_idade}")
print(f"Valor total: R${total3:.2f}")
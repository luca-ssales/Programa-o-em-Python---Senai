def cumprimentar():
    print('Seja bem vindo ao restaurante z...')
    print('Faça seu pedido: ')


def cadastro():
    nome  =  input('Nome: ')
    mesa = input('Mesa: ')
    return f'Cliente {nome}, Mesa {mesa}'

def pay(valor_):
    lista_pag = ['', '1 pix', '2 cc','3 cd']
    escolha = input(f'forma de pagamento: {lista_pag}')
    # posicao = lista_pag.index(escolha)
    print(f'R$ {valor_} - A forma de pagamento é ', escolha )


def restaurante():
    valor_total = 0
    cumprimentar()
    dados = []
    dados.extend([cadastro()])
    print(dados)
    ped = input('Deseja fazer o pedido? ')
    pedido = []
    valores  = []
    while ped == 'sim':
       

        menu = {

        'SALADA': 25.00,
        'MACARRONADA': 18.55,
        'SANDUICHE':32.60,
        'SORVETE':15.00

        }


        print('Menu:', menu)

        escolha  =  input(f'ecolha pelo nome:  {menu}').upper()
       

        if  escolha  in  menu.keys():
            pedido.append(escolha)
            valores.append(menu[escolha])
            print(pedido)
            print('R$', sum(valores))
            ped = input('Deseja continuar? ')
            valor_total = sum(valores)
        else:
            print('Digite algo valido...')


    else:
       
       
        pay(valor_total)
        print('Obrigada Volte sempre!')    

       
while True:
      restaurante()
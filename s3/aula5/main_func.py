from compra_enunciado import *


if __name__ == '__main__':

    lin()
    cliente1 = Cliente('224.083.250-99', 'Rafael')
    print(cliente1)

    carrinho1 = CarrinhoCompra("12", cliente1)
   # print(f'Nome:', carrinho1.get_cliente_nome())
    carrinho1.mostra_carrinho()

    produto1 = Produto('NMK444967800', 'Microfone FIFINE A8', 232.90, 1)
    #print(f'{produto1.__str__()}')
    carrinho1.insere_produto(produto1)
    print("xxxxxxxxxxxxxxxxxxxx")
    carrinho1.mostra_carrinho()





    lin()
    cliente2 = Cliente('053.678.498-68', 'Mateus')
    print(f'{cliente2.__str__()}')
    
    lin()   
    
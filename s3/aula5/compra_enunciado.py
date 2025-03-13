def lin ():  #linhas
    print('-'*50)

class Cliente(object):
    def __init__(self, cpf, nome=''):
        self.cpf = cpf
        self.nome = nome

    def get_cpf(self):
        return self.cpf
    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_nome(self):
        return self.nome

    def __str__(self):
        dados = f'-Cliente: \nCPF: {self.cpf}\nNome: {self.nome}'
        return dados

class CarrinhoCompra(object):
    def __init__(self, num_pedido, o_cliente):
        self.num_pedido = num_pedido
        self.o_cliente = o_cliente
        self.l_produto = list()

    def get_num_pedido(self):
        return self.num_pedido
    
    def get_cliente_nome(self):
        return self.o_cliente.get_nome()
    
    def insere_produto(self, o_produto):
        self.l_produto.append(o_produto)
    
    def mostra_carrinho(self):
        if len(self.l_produto) !=0:
            for o_produto in self.l_produto: 
                print("Descrição:", o_produto.get_nome())
        else:
            print("Carrinho vazio")
    

class Produto(object):
    def __init__(self, idt, nome, preco=0.0, qtd=1):
        self.idt = idt
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def get_nome(self):       
        return self.nome
    def set_nome(self, n_nome):
        self.nome = n_nome

    def __str__(self):
        dados = f'-Produto: \nIDT: {self.idt} \nNome: {self.nome} \nPreco: R${self.preco:.2f} \nQuantidade: {self.qtd}'
        return dados

        
      
import pa6

def lin(): #mostra linhas
    print(f'{pa6.c1}>{'-'*60}<{pa6.nc}')

class Funcionario():
    def __init__(self, nome, salario=0.0):
        self.nome = nome
        self.salario = salario        

    def get_nome (self):
        return self.nome
    
    def get_salario (self):
        return self.salario

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def set_nome (self, novo_nome):
        self.nome = novo_nome

    def set_salario (self, novo_salario):
        self.salario = novo_salario

    def mostra_dados(self):
        print(f'{pa6.c4}>>Mostra dados<<{pa6.nc}')
        print(f'{pa6.c3}Nome: {self.nome} \nSalário: {self.salario}{pa6.nc}')
    
#--------------------------------------------------------

class Gerente(object):
    def __init__(self, nome, salario, qtd_gerencia=1):
        self.nome = nome
        self.salario = salario
        self.qtd_gerencia = qtd_gerencia
    
    def get_nome(self):
        return self.nome
    
    def get_salario (self):
        return self.salario
    
    def get_qtd_gerencia (self):
        return self.qtd_gerencia
    
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def set_nome (self, novo_nome):
        self.nome = novo_nome

    def set_salario (self, novo_salario):
        self.salario = novo_salario

    def set_qtd_gerencia(self, nova_qtd):
        self.qtd_gerencia = nova_qtd

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def mostra_dados(self):
        print(f'{pa6.c4}>>Mostra dados<<{pa6.nc}')
        print(f'{pa6.c3}Nome: {self.nome} \nSalário: {self.salario} \nGerencia: {self.qtd_gerencia}{pa6.nc}')


    

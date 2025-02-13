import pa6

def lin ():  #linhas
    print('-'*55)


class Conta(): #Superclasse

    def __init__(self, nome, saldo=0.0):
        
        self.nome = nome
        self.saldo = saldo

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def get_nome(self):
        return self.nome
    
    def get_saldo(self):
        return self.saldo
    
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    
    def __str__(self): 
        s = f'Nome: {pa6.c3}{self.nome}{pa6.nc} \nSaldo: {pa6.c3}R${self.saldo}{pa6.nc}'
        return s
    
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self,valor):
        if valor > self.saldo:
            print(f'{pa6.c2}AÇÃO IMPOSSÍVEL, SALDO INSUFICIENTE!{pa6.nc}')

        else:
            self.saldo -= valor  
#--------------------------------------------------------


class PessoaFisica(Conta):

    def __init__(self, nome, saldo=0.0, genero='Masculino'):
        
        super().__init__(nome,saldo)
        self.genero = genero

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def get_genero(self):
        return self.genero
    
    def set_genero(self, novo_genero):
        self.genero = novo_genero

#--------------------------------------------------------


class PessoaJuridica(Conta):

    def __init__(self, nome, saldo=0.0, modalidade='MEI'):
        super().__init__(nome,saldo)
        self.modalidade = modalidade

    def get_modalidade(self):
        return self.modalidade
    
    def set_modalidade(self,nova_modalidade):
        self.modalidade = nova_modalidade
import pa6

def lin(): #mostra linhas
    print(f'{pa6.c1}>{'-'*60}<{pa6.nc}')

class Pessoa(object):
    def __init__ (self, nome, peso, altura, ano_nasc=2000):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.ano_nasc = ano_nasc

#--------------------------------------------------

    def get_nome (self):
        return self.nome
    
    def get_peso (self):
        return self.peso
    
    def get_altura (self):
        return self.altura
    
    def get_ano_nasc (self):
        return self.ano_nasc
    
#--------------------------------------------------

    def set_nome (self, novo_nome):
        self.nome = novo_nome

    def set_peso (self, novo_peso):
        self.peso = novo_peso

    def set_altura (self, nova_altura):
        self.altura = nova_altura

    def set_ano_nasc (self, novo_ano_nasc):
        if type(novo_ano_nasc) == int:
            self.ano_nasc = novo_ano_nasc

        else:
            print(f"{pa6.c2}Dados Inconsistentes!{pa6.nc}")

#--------------------------------------------------

    def imc(self):
        return self.peso/(self.altura**2)    






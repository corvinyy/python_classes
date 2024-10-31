from pa6 import*
from abc import ABC, abstractmethod

def lin ():  #linhas
    print('-'*55)

class Carro(ABC):

    preco_base = 100

    @classmethod
    def get_preco_base(cls):
        return cls.preco_base
    
    @classmethod
    def set_preco_base(cls, novo_preco):
        cls.preco_base = novo_preco

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def __init__(self,modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo
    
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    @abstractmethod
    def preco_diaria(self):
        pass

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#--------------------------------------------------------


class Economico(Carro):
    def __init__(self, modelo):
        super().__init__(modelo)

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def preco_diaria(self):
        val_diaria = Carro.get_preco_base() + (Carro.get_preco_base() * (5/100))
        return val_diaria

#--------------------------------------------------------

class Intermediario(Carro):
    def __init__(self, modelo):
        super().__init__(modelo)
        
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def preco_diaria(self):
        return Carro.get_preco_base() * 1.1
    
#--------------------------------------------------------
    
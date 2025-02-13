import pa

class Veiculo(object):
    def __init__(self, modelo, ano, preço):

        self.modelo = modelo
        self.ano = ano
        self.preço = preço

#------------------------------------------------------   

    def get_modelo (self):
        return self.modelo
    
    def get_ano (self):
        return self.ano
    
    def get_preço (self):
        return self.preço

#------------------------------------------------------ 

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def set_preço(self, novo_preço):
        if novo_preço < 0:
            print(f'{pa.yellow}\nDADOS INCONSISTENTES!{pa.nc}')
        else:
            self.preço = novo_preço

#------------------------------------------------------ 

    def mostra_dados(self):
        print(f'{pa.blue}>>Mostra dados [carro 2]<<{pa.nc}')
        print(f'Modelo: {self.modelo} \nAno: {self.ano} \nPreço: {self.preço}')

#------------------------------------------------------ 

    def aumenta_valor(self, aumenta_preço): 
        self.preço = aumenta_preço
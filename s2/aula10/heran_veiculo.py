import pa6

yc = "\33[1;49;31m" 
yc2 = "\33[1;49;34m" 
nc = "\33[m" 

def lin ():  #linhas
    print('-'*50)


class Veiculo(): #Superclasse

    def __init__(self, modelo, preco, km=0):
        
        self.modelo = modelo
        self.preco = preco
        self.km = km


    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    
    def get_modelo (self):
        return self.modelo
    
    def get_preco (self):
        return self.preco
    
    def get_km (self):
        return self.km
    
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def set_preco(self, novo_preco):
        if novo_preco < 0:
            print(f'{yc}DADOS INCONSISTENTES!{nc}')
        else:
            self.preco = novo_preco

    def set_km(self, novo_km):
        self.km = novo_km

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def atualiza_valor(self, vlr_aumento):
        if vlr_aumento < 0:
            print(f'{yc}DADOS INCONSISTENTES!{nc}')
        else:
            self.preco = self.preco + vlr_aumento

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    
    def situacao_veiculo(self):
        if self.km == 0:
            print(f'{pa6.c4}VEÍCULO NOVO!{nc}')
            
        elif self.km <= 20000:
            print(f'{pa6.c4}VEÍCULO SEMINOVO!{nc}')

        elif self.km > 20000:
            print(f'{pa6.c4}VEÍCULO USADO!{nc}')

#--------------------------------------------------------

class Carro(Veiculo):

    def __init__(self, modelo, preco, km=0, n_portas=2):
        super().__init__ (modelo, preco, km)
        self.n_portas = n_portas

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def get_n_portas(self):
        return self.n_portas
    
    def set_n_portas(self, novo_n_portas):
        self.n_portas = novo_n_portas
    
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def mostra_dados(self):
     print(f'''Modelo: {yc2}{self.modelo}{nc}
Preço: {yc2}R${self.preco}{nc}
Quilometragem: {yc2}{self.km}{nc}
Número de Portas: {yc2}{self.n_portas}{nc}''')

    def __str__(self):
        s = f'Modelo: {yc2}{self.modelo}{nc} \nPreço: {yc2}{self.preco}{nc} \nQuilometragem: {yc2}{self.km}{nc} \nNúmero de portas: {yc2}{self.n_portas}{nc}'
        return s

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    
    #--------------------------------------------------------

class Moto(Veiculo):

    def __init__(self, modelo, preco, km=0, cilindradas=100):
        super().__init__(modelo, preco, km)
        self.cilindradas = cilindradas

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def get_cilindradas(self):
        return self.cilindradas
    
    def set_cilindradas(self, nova_cilindradas):
        if nova_cilindradas < 125:
            print(f'{yc}DADOS INCONSISTENTES!{nc}')
        self.cilindradas = nova_cilindradas
    
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def mostra_dados(self):
     print(f'''Modelo: {yc2}{self.modelo}{nc}
Preço: {yc2}R${self.preco}{nc}
Quilometragem: {yc2}{self.km}{nc}
Cilindradas: {yc2}{self.cilindradas}cc{nc}''')
     


#--------------------------------------------------------



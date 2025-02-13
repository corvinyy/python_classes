import pa6

def lin(): #mostra linhas
    print(f'{pa6.c1}>{'-'*60}<{pa6.nc}')

class Produto():
    def __init__(self, nome, vlr_compra, vlr_venda, qtd_estoque=0, qtd_minima=0):
        self.nome = nome
        self.vlr_compra = vlr_compra
        self.vlr_venda = vlr_venda
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima

#--------------------------------------------------------

    def get_nome (self):
        return self.nome 
    
    def get_qtd_estoque (self):
        return self.qtd_estoque
    
#--------------------------------------------------------

    def set_nome (self, novo_nome):
        self.nome = novo_nome

    def set_qtd_estoque (self, novo_vlr):
        
        if novo_vlr < 0:
            print(f"{pa6.c2}\nDADOS INCONSISTENTES!{pa6.nc}")   
        
        else:
            self.qtd_estoque = novo_vlr

#--------------------------------------------------------

    def  __str__(self):
        s = f"Nome:{self.nome}, {self.vlr_compra}, {self.vlr_venda}, {self.qtd_estoque}, {self.qtd_minima}"
        return s
    
    
    def lucro(self):
        vlr_lucro = self.vlr_venda - self.vlr_compra
        return vlr_lucro

    def atualiza_estoque(self, qntd_vendida):
        self.qtd_estoque -= qntd_vendida

    def repor_produto(self, qtd_comprada):
        self.qtd_estoque += qtd_comprada
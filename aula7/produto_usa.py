import pa6
from produto_classe import*

if __name__ == '__main__':

    p1 = Produto("Arroz", 19.00, 27.50, 67, 20)

    lin()

    print(f'''\n{pa6.c3}[PRODUTO 1]{pa6.nc}
Nome: {p1.get_nome()} \nValor da compra: {p1.vlr_compra} \nValor da venda: {p1.vlr_venda}
Quantidade em estoque: {p1.get_qtd_estoque()} \nQantidade Mínima: {p1.qtd_minima}''')
    
    print(f'\n{pa6.c4}Lucro: {p1.lucro()}{pa6.nc}\n')
    lin()

    p1.set_qtd_estoque(int(input("\nAlterar quantidade em estoque: ")))

    print(f'''{pa6.c4}Quantidade do estoque de {pa6.c3}[{p1.get_nome()}]{pa6.c4} Alterada!{pa6.nc}
Valor da compra: {p1.vlr_compra} \nValor da venda: {p1.vlr_venda} \nQuantidade em estoque: {p1.get_qtd_estoque()} 
Qantidade Mínima: {p1.qtd_minima}\n''')
        
    lin()
    
   

   




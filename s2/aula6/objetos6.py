import pa6
from classepessoa import *

if __name__ == '__main__':

    p1 = Pessoa("Guilherme", 50, 1.72, 2004)
    p2 = Pessoa("Issssssami", 60, 1.70, 2005)
    p3 = Pessoa("Lorena", 51, 1.66)

   
    lin()
    
    print(f'''{pa6.c3}[ PESSOA 1 ]{pa6.nc}
Nome: {p1.get_nome()} \nPeso: {p1.get_peso()}Kg \nAltura = {p1.get_altura()} \nAno de Nascimento = {p1.get_ano_nasc()}
O IMC do(a) {p1.get_nome()} é {p1.imc():.2f}''')

    lin()

    print(f'''{pa6.c3}[ PESSOA 2 ]{pa6.nc}
Nome: {p2.get_nome()} \nPeso: {p2.get_peso()}Kg \nAltura = {p2.get_altura()} \nAno de Nascimento = {p2.get_ano_nasc()}
O IMC do(a) {p2.get_nome()} é {p2.imc():.2f}''')

    lin()

    print(f'''{pa6.c3}[ PESSOA 3 ]{pa6.nc}
Nome: {p3.get_nome()} \nPeso: {p3.get_peso()}Kg \nAltura = {p3.get_altura()} \nAno de Nascimento = {p3.get_ano_nasc()}
O IMC do(a) {p3.get_nome()} é {p3.imc():.2f}''')

    lin()

    p1.set_ano_nasc = 2000
    
    print(f'''{pa6.c3}[ PESSOA 1 ]{pa6.nc}
Nome: {p1.get_nome()} \nPeso: {p1.get_peso()}Kg \nAltura = {p1.get_altura()} \nAno de Nascimento = {p1.get_ano_nasc()}
O IMC do(a) {p1.get_nome()} é {p1.imc():.2f}''')

 
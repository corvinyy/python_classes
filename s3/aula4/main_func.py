from cliente_enunciado import *

if __name__ == '__main__':
    
    lin()

    cl1 = Cliente("Guilherme", 2004)
    e1 = Endereco("Brasília","DF")
    print(f'Nome: {cl1.get_nome()} \nAno Nascimento: {cl1.get_ano_nasc()} \nIdade: {cl1.calcula_idade()}')
    print(f'{e1.__str__()}')

    print(cl1.mostra_endereco2())
    
    lin()



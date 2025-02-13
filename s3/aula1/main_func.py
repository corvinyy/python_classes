from Inst_Ensino import *

lin()

if __name__ == '__main__':

    p1 = Pessoa('Alice', 0)
    print ('- Dados de Pessoa ...')
    print(f'Nome: {p1.get_nome()}')

    p1.set_nome('Bruno')
    print(f'Nome: {p1.get_nome()}')


    lin()



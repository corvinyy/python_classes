import pa6

from conta_corrente import*

if __name__ == '__main__':

    lin()

    count1 = Conta('Guilherme', 928.85)

    print(f'''{pa6.c2}CONTA 1{pa6.nc}
Nome: {pa6.c3}{count1.get_nome()}{pa6.nc}
Saldo: {pa6.c3}R${count1.get_saldo()}{pa6.nc}''')
    
    print(f'''\n{pa6.c2}CONTA 1 (__STR__){pa6.nc}''')
    print(count1.__str__())
    
    lin()
    
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    pf1 = PessoaFisica('Rafael', 50.0, 'Masculino')
    
    print(f'''{pa6.c2}PESSOA FÍSICA 1{pa6.nc}
Nome: {pa6.c3}{pf1.get_nome()}{pa6.nc}
Saldo: {pa6.c3}R${pf1.get_saldo()}{pa6.nc}
Gênero: {pa6.c3}{pf1.get_genero()}{pa6.nc}''')
    
    print(f'''\n{pa6.c2}PESSOA FÍSICA 1 (vars){pa6.nc}''')
    print(vars(pf1))

    print(f'''\n{pa6.c2}PESSOA FÍSICA 1 (__dict__){pa6.nc}''')
    print(pf1.__dict__)
    
    lin()
   
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    pf2 = PessoaFisica('Lorena', 530.70, 'Feminino')

    print(f'''{pa6.c2}PESSOA FÍSICA 2{pa6.nc}
Nome: {pa6.c3}{pf2.get_nome()}{pa6.nc}
Saldo: {pa6.c3}R${pf2.get_saldo()}{pa6.nc}
Gênero: {pa6.c3}{pf2.get_genero()}{pa6.nc}''')
    
    lin()

    pf2.deposito(200)
    print(f'''{pa6.c4}DEPOSITANDO +R$200.00{pa6.nc}''')
    print(f'SALDO: {pa6.c3}R${pf2.get_saldo()}{pa6.nc}')
    
    lin()

    print(f'''{pa6.c2}SAQUE -R$10.00{pa6.nc}''')
    pf2.saque(10)
    print(f'SALDO ATUAL: {pa6.c3}R${pf2.get_saldo()}{pa6.nc}')
    lin()

    print(f'''{pa6.c2}SAQUE -R$1000.00{pa6.nc}''')
    pf2.saque(1000)
    print(f'SALDO ATUAL: {pa6.c3}R${pf2.get_saldo()}{pa6.nc}')
    lin()

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


    
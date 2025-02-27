from conta_agregacao import*

if __name__ == '__main__':
    
    lin()

    titular1 = Titular ('371-1', 'Guilherme', 'Santiago')
    
    print(f'cpf: {titular1.get_cpf()} \n{titular1.nome_completo()}')

    lin()

    conta1 = Conta('458-1', titular1, 1200.0, 2000.00)
    print(f'numero: {conta1.get_numero()} \ntitular: {conta1.get_titular()} \nsaldo: {conta1.get_saldo()} \nlimite: {conta1.get_limite()}')
    
    print(conta1.get_titular().get_nome(), conta1.get_titular().get_sobrenome())
    
    lin()
    
    print()

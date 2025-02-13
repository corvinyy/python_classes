import pa6
from heranca_func import *

if __name__ == '__main__':

    f1 = Funcionario('Michel', 1400.00)
    f2 = Funcionario('Marcos')

    #--------------------------------------------------------

    lin()

    print(f'''{pa6.c2} --------------
| Funcionários | 
 --------------{pa6.nc}         
        ''')


    print(f'{pa6.c4}Funcionário 1\n{pa6.c3}Nome = {f1.get_nome()} / Salário: {f1.get_salario()}{pa6.nc}')
    f1.set_nome('Vinícius')
    print(f'{pa6.c4}\nAlterando nome do funcionário 1:')
    print(f'{pa6.c3}Nome = {f1.get_nome()} / Salário: {f1.get_salario()}{pa6.nc}')


    print(f'\n{pa6.c4}Funcionário 2: \n{pa6.c3}Nome = {f2.get_nome()} / Salário: {f2.get_salario()}{pa6.nc}\n')

    print(f'{pa6.c4}>>MOSTRA DADOS FUNCIONARIO 1<<{pa6.nc}')
    f1.mostra_dados()

    print(f'\n{pa6.c4}BONIFICAÇÃO FUNCIONARIO 1\n{pa6.c3}10% do Salário: {f1.bonificacao()}{pa6.nc}')
    lin()
    
    #--------------------------------------------------------

    print(f'''{pa6.c2} ---------
| Gerente | 
 ---------{pa6.c2}         
          ''')

    g1 = Gerente('Barbosa', 5400.00, 5)
    
    print(f'{pa6.c4}GERENTE:{pa6.c3}\nNome = {g1.get_nome()} \nSalário: {g1.get_salario()} \nGerencia: {g1.get_qtd_gerencia()}{pa6.nc}\n')
    
    print(f'{pa6.c4}>>MOSTRA DADOS GERENTE<<{pa6.nc}')
    g1.mostra_dados()

    lin()
    #--------------------------------------------------------




  
  

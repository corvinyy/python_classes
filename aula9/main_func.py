import pa6
from pro_func import *

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

    f1.mostra_dados()
    lin()
    #--------------------------------------------------------

    print(f'''{pa6.c2}\n ---------
| Gerente | 
 ---------{pa6.c2}         
          ''')

    g1 = Gerente('Barbosa', 5400.00, 5)
    g1.mostra_dados()



    lin()

  
  

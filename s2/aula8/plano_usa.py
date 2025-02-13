import pa6
from plano_cartesiano import *

if __name__ == '__main__':

    p1 = Point()
    p2 = Point(2, 3)
    p3 = Point(5)
    p4 = Point(y=6)
    #--------------------------------------------------------
   
    lin()

    print(f'{pa6.c3}X = {p1.get_x()}{pa6.nc}')
    print(f'{pa6.c3}Y = {p1.get_y()}{pa6.nc}')


    print(f'{pa6.c4}\nAlterando valor de [X, Y] do ponto 1:')
    
    p1.set_x(4)
    p1.set_y(6)
    print(f'PONTO 1: {pa6.c3}{p1.__str__()}')
    
    #--------------------------------------------------------

    print(f'\n{pa6.c4}Outros pontos:')

    print(f'\nPONTO 2: {pa6.c3}{p2.__str__()}')

    print(f'{pa6.c4}\nPONTO 3: {pa6.c3}{p3.__str__()}')

    print(f'{pa6.c4}\nPONTO 4: {pa6.c3}{p4.__str__()}{pa6.nc}')

    lin()



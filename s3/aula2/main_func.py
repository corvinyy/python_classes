from abstrata_formaGeo import *

if __name__ == '__main__':

    lin()

    q1 = Quadrado(5)
    print('[Quadrado 1]')
    print(f'lado = {q1.get_lado()}')
    print(f'area = {q1.area()}')
    print(f'perimetro = {q1.perimetro()}')

    lin()
   
    c1 = Circulo(5)
    print('[Circulo 1]')
    print(f'lado = {c1.get_raio():.2f}')
    print(f'area = {c1.area():.2f}')
    print(f'perimetro = {c1.perimetro():.2f}')

    lin()
    

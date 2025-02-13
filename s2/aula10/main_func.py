import pa6

from heran_veiculo import*

if __name__ == '__main__':

    car = Carro('Civic Hybrid', 265900.00, 80000, 4)
    car2 = Carro('HR-V', 162300.00, 60000, 4)
    car3 = Carro('aaa', 130000.00, 80000, 4)
    print(car, car2) #teste

    moto1 = Moto('CG 160',17440.00, 90000, 162)
    moto2 = Moto('FZ15', 19690.00, 50000, 150)
    moto3 = Moto('FZ25', 21690.00, 80000, 250)
    
    print(moto1, moto2) #teste

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    
    lin()

    print(f''' -----------
| {yc}AUTOMÓVEL{nc} | 
 -----------         
        ''')
    
    print(f'''{yc}CARRO 1{nc}
Modelo: {yc2}{car.get_modelo()} {nc}
Preço: {yc2}R${car.get_preco()}{nc}
Quilometragem: {yc2}{car.get_km()}{nc}
Número de Portas: {yc2}{car.get_n_portas()}{nc}''')
    
    print(f'\n{yc}Alternando preço do Honda Civic Hybrid{nc}')
    car.set_preco(275800.00)
    print(f'Novo preço: {yc2}R${car.get_preco()}{nc}')
    
    print(f'\n{yc}CARRO 2 (MOSTRA DADOS){nc}')
    car2.mostra_dados()

    print(f'\n{yc}CARRO 3 (__STR__){nc}')
    print(car3.__str__())

    lin()
    print(f'{yc}MOTO 1 (MOSTRA DADOS){nc}')
    moto1.mostra_dados()

    print(f'\n{yc}MOTO 2 (MOSTRA DADOS){nc}')
    moto2.mostra_dados()

    print(f'\n{yc}MOTO 3 (DICT){nc}')
    print(moto3.__dict__)

    moto3.atualiza_valor(1200)
    print(f'\n{pa6.c4}NOVO PREÇO DA FZ25: {yc2}{moto3.get_preco()}{nc}')
    moto3.mostra_dados()

    print(f'Moto3')
    moto3.situacao_veiculo()


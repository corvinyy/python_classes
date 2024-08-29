import pa

from classeveiculo import Veiculo

def lin():
    print(f'{pa.white}-{pa.nc}'*30)


if __name__ == '__main__':

    carro1 = Veiculo('HB', 2022, 80500.00)
    carro2 = Veiculo('Carola', 2024, 190000.00)

    lin()
    
    print(f'{pa.blue}>>Dados [carro 1]<<{pa.nc}') 
    print(f'Modelo: {carro1.get_modelo()} \nAno: {carro1.get_ano()} \nPreço: {carro1.get_preço()}')
    
    lin()
    
    print(f'{pa.blue}>>Dados [carro 2]<<{pa.nc}') 
    print(f'Modelo: {carro2.get_modelo()} \nAno: {carro2.get_ano()} \nPreço: {carro2.get_preço()}')
    
    lin()
    
    print(f'{pa.cyan}>>ATUALIZAÇÃO [CARRO 1]<<{pa.nc}')
    
    carro1.set_modelo('HB20')
    carro1.set_ano(2020)
    carro1.set_preço(-1)
    
    print(f'Modelo: {carro1.get_modelo()} \nAno: {carro1.get_ano()} \nPreço: {carro1.get_preço()}')
    
    lin()
    
    carro2.mostra_dados()

    lin()

    carro1.aumenta_valor()

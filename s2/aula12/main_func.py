import pa6

from class_abstrata import*

if __name__ == '__main__':

    lin()

    Carro.set_preco_base(200)
    print(f"Preço base de locação: {Carro.get_preco_base()}")

    obj = Economico('Uno')
    print(f"O carro: {obj.get_modelo()}")
    print(f"Preço basico: {Carro.get_preco_base()}")
    
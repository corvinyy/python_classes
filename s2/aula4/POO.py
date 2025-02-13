import pa 

def lin():
    print(f'{pa.white}-{pa.nc}'*30)

class Aluno:
    def __init__(self, nome, idade, mensalidade):

        self.nome = nome
        self.idade = idade
        self.mensalidade = mensalidade

    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def get_mensalidade(self):
        return self.mensalidade
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    #def mostra_dados():



if __name__ == '__main__':
    
    aluno1 = Aluno('Couto', 21, 1060.90)
    #print(aluno1)
        
    aluno2 = Aluno('Aurélio', 20, 1179.90)
    #print(aluno2)

    aluno3 = Aluno('Bagriel', 22, 3579.99)
    #print(aluno3)
    lin()

    print(f"{pa.yellow}- Aluno 1: \nNome: {pa.blue}{aluno1.get_nome()}")
    print(f"{pa.yellow}Idade: {pa.blue}{aluno1.get_idade()}")
    print(f"{pa.yellow}Mensalidade: {pa.blue}{aluno1.get_mensalidade()}")

    lin()

    print(f"{pa.yellow}- Aluno 2: \nNome: {pa.blue}{aluno2.get_nome()}")
    print(f"{pa.yellow}Idade: {pa.blue}{aluno2.get_idade()}")
    print(f"{pa.yellow}Mensalidade: {pa.blue}{aluno2.get_mensalidade()}")

    lin()

    print(f'{pa.yellow}- Aluno 3 \nNome: {pa.blue}{aluno3.get_nome()}')
    print(f'{pa.yellow}Idade: {pa.blue}{aluno3.get_idade()}')
    print(f'{pa.yellow}Mensalidade: {pa.blue}{aluno3.get_mensalidade()}')

    lin()

    aluno2.set_nome("Alice")
    print(f"{pa.green}Nome atualizado do(a) aluno(a) 2: {pa.blue}{aluno2.get_nome()}")
    print(f"{pa.yellow}- Aluno 2: \nNome: {pa.blue}{aluno2.get_nome()}{pa.nc}\n")

    



    
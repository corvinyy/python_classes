import pa6

def lin(): #mostra linhas
    print(f'{pa6.c1}>{'-'*60}<{pa6.nc}')

class Point():
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

#--------------------------------------------------------

    def get_x (self):
        return self.x 
    
    def get_y (self):
        return self.y

#--------------------------------------------------------

    def set_x (self, novo_x):
        
        if type (novo_x) in (int, float):
            self.x = novo_x  
        
        else:
            print(f"{pa6.c2}\nERRO! Precisa ser {pa6.c3}int{pa6.c2} ou {pa6.c3}float{pa6.c2}.")   


    def set_y (self, novo_y):
        self.y = novo_y

#--------------------------------------------------------

    def __str__(self):
        s = f'({self.x}, {self.y})'
        return s
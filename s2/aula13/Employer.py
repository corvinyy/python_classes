from abc import ABC, abstractmethod

def lin ():  #linhas
    print('-'*55)

class Employer(ABC):
    def __init__(self, first_name, last_names):
        self.first_name = first_name
        self.last_names = last_names

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def get_first_name(self):  #metodo concreto
        return self.first_name
    def set_first_name(self, novo_f_name):
        self.first_name = novo_f_name

    def get_last_names(self):
        return self.last_names
    def set_last_names(self, novo_l_names):
        self.last_names = novo_l_names

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    @abstractmethod   #metodo abstrato
    def compute_salary(self):
        pass

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def full_name(self):
        fn = f'{self.first_name} {self.last_names}'
        return fn

#----------------------------------------------------------

class FulltimeEmployee(Employer):
    def __init__(self, first_name, last_names, base_salary):
        super().__init__(first_name, last_names)

        self.base_salary = base_salary

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def get_base_salary(self):
        return self.base_salary
    def set_base_salary(self, novo_b_salary):
        self.base_salary = novo_b_salary

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    
    def compute_salary(self):
        salario_total = self.base_salary + 200 #REGRA DE NEGOCIO (RN 200)
        return salario_total   


#----------------------------------------------------------

class HourlyEmployee(Employer):
    def __init__(self, first_name, last_names, worked_hours, value_hour):
        super().__init__(first_name, last_names)

        self.worked_hours = worked_hours
        self.value_hour = value_hour

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def get_worked_hours(self):
        return self.worked_hours
    def set_worked_hours(self, new_whours):
        self.worked_hours = new_whours

    def get_value_hour(self):
        return self.value_hour
    def set_value_hour(self,new_vhour):
        self.value_hour = new_vhour

    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    
    def compute_salary(self):
        salario_total = self.worked_hours * self.value_hour  #RN DE WORKED HOURS * VALUE HOUR
        return salario_total


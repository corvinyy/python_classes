from Employer import *

if __name__ == '__main__':

    #obj_employee = Employer('Emily', 'Pereira')  NAO PODE HERDAR DA CLASSE ABSTRATA!
    lin()

    obj1 = FulltimeEmployee('Guilherme', 'Santiago', 2.50)
    print(f'''Fulltime Employee 1
Nome: {obj1.get_first_name()}    
Nome completo: {obj1.full_name()} 
Salário fixo: R${obj1.get_base_salary()}
Salário total: R${obj1.compute_salary()}\n''')
    
    lin()

    obj2 = HourlyEmployee('Lorena', 'Araujo', 18, 340)
    print(f'''HourlyEmployee 1
Nome: {obj2.get_first_name()}    
Nome completo: {obj2.full_name()} 
Salário total: R${obj2.compute_salary()}\n''')
    
    lin()


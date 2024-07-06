class Person:
    
    def __init__(self, name = 'Tancredo', age = 51, cpf = '123456789'):
        
        self.name  = name
        self.age   = age # +age: int | public
        self.__cpf = cpf # -cpf: string | private
        
    
    def drink(self, drink = 'juice'): # +       
         
        if drink == 'beer' or drink == 'milk':
            self.__show_cpf()
        print(f"{self.name} is drinking {drink}.")

    def __show_cpf(self): # -
        print(self.__cpf)
        
trancredo = Person()
print(trancredo.name)
print(trancredo.age)
print("---")
trancredo.drink('beer')
trancredo.drink('water')

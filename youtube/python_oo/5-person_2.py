class Person: # Substantivo
    
    def __init__(self, name:str = 'Tancredo', age:int = 51) -> None:
        self.name  = name
        self.age   = age
        
    
    def drive(self, car:str = 'fusion') -> None: # Verbo     
        print(f"{self.name} is driving his {car}.")

    def sing(self) -> None:
        print("Then we hit the road, cruisin' seaside 🎶")
        
    def show_age(self) -> int: # Verbo
        return self.age
    
    
class Calculator:
    
    def operation(self, option = '+', n1 = 3, n2 = 2):
        
        if   option == '+':
            return self.__sum(n1, n2)
        elif option == '-':
            return self.__sub(n1, n2)
        else:
            print("Invalid symbol.")
            
            
    def __sum(self, n1, n2):
        return n1 + n2
        
    def __sub(self, n1, n2):
        return n1 - n2
        

calcu = Calculator()
print(calcu.operation('-', 3, 2))

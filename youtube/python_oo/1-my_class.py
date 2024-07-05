class MyClass:
    
    def __init__(self, att_2 = '-empty-'):
  
        self.my_attribute = "Hello, World!"
        self.my_attribute_2 = att_2
        
    
    def my_method(self):   
        print("I'm in my method.")
        print(self.my_attribute)
        print(self.my_attribute_2)
        
    def my_method_2(self, num, mult):
        return num * mult
    
    
object = MyClass()
object.my_method()

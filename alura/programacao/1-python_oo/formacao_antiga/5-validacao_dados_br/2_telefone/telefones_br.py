import re

class Telefone:
    
    def __init__(self, telefone):
        
        if self.phone_validator(telefone):
            self.number = telefone
        else:
            raise ValueError('Pão')
    
    def __str__(self):
        
        return self.formatted_number()
    
    def phone_validator(self, telefone):
        
        default = '([0-9]{2,3}[ ]?)?([(]?[0-9]{2}[)]?[ ]?)([0-9]{4,5})[-]?([0-9]{4})'
        valid = re.findall(default, telefone)
        
        if valid:
            return True
        else:
            return False
    
    def formatted_number(self):
        
        default = '([0-9]{2,3}[ ]?)?([(]?[0-9]{2}[)]?[ ]?)([9][0-9]{4})[-]?([0-9]{4})'
        formatter = re.search(default, self.number)
        
        return ('+{} ({}) {}-{}'.format(
            formatter.group(1),
            formatter.group(2),
            formatter.group(3),
            formatter.group(4)
            )
        )
        
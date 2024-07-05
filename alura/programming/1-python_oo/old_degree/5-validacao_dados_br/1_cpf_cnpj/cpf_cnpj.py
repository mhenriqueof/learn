from validate_docbr import CPF, CNPJ

class Document:
    
    @staticmethod
    def create_doc(document):
        
        if len(document) == 11:
            return DocCpf(document)
        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise ValueError('Incorrect number of digits!')

class DocCpf:
    
    def __init__(self, document):
        
        if self.validate(document):
            self.cpf = document
        else:
            raise ValueError('Invalid CPF!')
    
    def __str__(self):

        return self.format()

    def validate(self, document):

        validator = CPF()
        
        return validator.validate(document)
    
    def format(self):
        
        masker = CPF()

        return masker.mask(self.cpf)

class DocCnpj:
    
    def __init__(self, document):
        
        if self.validate(document):
            self.cnpj = document
        else:
            raise ValueError('Invalid CNPJ!')

    def __str__(self):
        
        return self.format()
    
    def validate(self, document):
        
        validator = CNPJ()
        
        return validator.validate(document)
    
    def format(self):
        
        masker = CNPJ()
        
        return masker.mask(self.cnpj)
    

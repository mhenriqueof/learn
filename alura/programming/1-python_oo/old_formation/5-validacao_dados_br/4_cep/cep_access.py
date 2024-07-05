import requests

class CepAddress:

    def __init__(self, cep):
        
        cep = str(cep)
        
        if self.valid_cep(cep):
            self.cep = cep
        else:
            raise ValueError('Incorrect CEP!')
    
    def __str__(self):
        
        return self.formatted_cep()
    
    def valid_cep(self, cep):
        
        if len(cep) == 8:
            return True
        else:
            return False
    
    def formatted_cep(self):
        
        masker_1 = self.cep[0:2]
        masker_2 = self.cep[2:5]
        masker_3 = self.cep[5:]
        
        return f'{masker_1}.{masker_2}-{masker_3}'
    
    def via_cep_access(self):
        
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        r = requests.get(url)
        info = r.json()
        
        return (
            info['bairro'],
            info['localidade'],
            info['uf']
        )
        
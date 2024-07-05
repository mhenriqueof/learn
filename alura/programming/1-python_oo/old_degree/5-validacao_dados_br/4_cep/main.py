import requests
from cep_access import CepAddress

cep_1 = CepAddress('01001000')
bairro, cidade, estado = cep_1.via_cep_access()
print(bairro, cidade, estado)

# todo criar uma função que retorna todas as informacoes do cep
address = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'


import re

cep_first = "['0123456789']['0123456789']['0123456789']['0123456789']['0123456789']"
cep_second = "['0123456789']['0123456789']['0123456789']"
# default = re.compile(f'{cep_first}[-]?{cep_second}')
default = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
find = default.search(address)

if find:
    cep = find.group()
    print(cep)

import re
"""
pedrao = '[0-9][a-z][0-9]'
texto = '123 1a3 lcc aal'

resposta = re.search(pedrao, texto)
print(resposta.group())

default = '\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}'
text = 'aaabbbcc rodrigo123@gmail.com.br'

search = re.search(default, text)
print(search.group())

default_1 = '[(]?[0-9]{2}[)]?[ ]?[0-9]{4}[-]?[0-9]{4}'
 e (21) 5463-4865'

findall = re.findall(default_1, text_1)
print(findall)
"""

'''default_2 = '[(]?[0-9]{2}[)]?[ ]?[0-9]{4}[-]?[0-9]{4}'
text_2 = 'pão 552165326598 '

findall = re.search(default_2, text_2)
print(findall.group(0))'''

text_1 = 'pão 2165326598'
default = '([0-9]{2,3}[ ]?)?([(]?[0-9]{2}[)]?[ ]?)([0-9]{4})[-]?([0-9]{4})'
formater = re.search(default, text_1)
        
print('+{} ({}) {}-{}'.format(
    formater.group(1),
    formater.group(2),
    formater.group(3),
    formater.group(4)
))
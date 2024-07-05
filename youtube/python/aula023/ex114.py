# Modules
import urllib
import urllib.request
# Code
try:
    link = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'Não é possível acessar.')
else:
    print(f'É possível acessar.')
    print(link.read())
    
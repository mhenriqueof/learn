'''
Exemplos de URLs válidas:

bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio

Exemplos de URLs inválidas:

https://bytebank/cambio
https://bytebank.naoexiste/cambio
ht://bytebank.naoexiste/cambio
'''
# https://www.bytebank.com.br/cambio
import re
url = 'bytebank.com.br/cambio'
url_default = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = url_default.match(url)

if not match:
    raise ValueError("The URL is invalid.")

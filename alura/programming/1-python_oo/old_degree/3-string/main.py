# url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
url = ' '

# URL Sanitation
url = url.strip()

# URL Validation
if url == '':
    raise ValueError("URL is empty.")

# Separate base and parameters
separator_index = url.find('?')
url_base      = url[:separator_index]
url_parameter = url[separator_index + 1:]

print(url_base)
print(url_parameter, '\n')

# Find parameter value
search_parameter      = 'quantidade'
parameter_index       = url_parameter.find(search_parameter)
parameter_index_value = parameter_index + len(search_parameter) + 1
ampersand_index       = url_parameter.find('&', parameter_index_value)

if ampersand_index == -1:
    parameter_value = url_parameter[parameter_index_value:] # Origem
else:
    parameter_value = url_parameter[parameter_index_value:ampersand_index] # Destino

print(parameter_value)

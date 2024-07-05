import re

class URLextractor:
    def __init__(self, url):
        self.url = self.url_sanitation(url)
        self.url_validation()

    def url_sanitation(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    def url_validation(self):
        if not self.url:
            raise ValueError("URL is empty.")
        
        url_default = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = url_default.match(self.url)
        if not match:
           raise ValueError("The URL is invalid.")


    def get_url_base(self):
        separator_index = self.url.find('?')
        return self.url[:separator_index]
    
    def get_url_parameters(self):
        separator_index = self.url.find('?')
        return self.url[separator_index + 1:]

    def get_parameter_value(self, search_parameter):
        parameter_index       = self.get_url_parameters().find(search_parameter)
        parameter_index_value = parameter_index + len(search_parameter) + 1
        ampersand_index       = self.get_url_parameters().find('&', parameter_index_value)
        if ampersand_index == -1:
            parameter_value = self.get_url_parameters()[parameter_index_value:] # Origem
        else:
            parameter_value = self.get_url_parameters()[parameter_index_value:ampersand_index] # Destino
        return parameter_value
    
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url
    
    def __eq__(self, other):
        return self.url == other.url

url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
url_extractor = URLextractor(url)
url_extractor_2 = URLextractor(url)
print(f'O tamanho da URL é {len(url_extractor)}.')
print(url_extractor == url_extractor_2)


quantidade_value = url_extractor.get_parameter_value("quantidade")
print(quantidade_value)
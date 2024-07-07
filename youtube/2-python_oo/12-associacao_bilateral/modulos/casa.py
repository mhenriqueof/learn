class Casa:
    
    def __init__(self) -> None:
        self.__endereco = 'Rua de uma cidade'
        self.__proprietario = None
        

    def acender_luzes (self) -> None:
        print('Acendendo luzes')
        
    def get_endereco(self) -> str:
        return self.__endereco
    
    def set_proprietario(self, proprietario:any) -> None:
        self.__proprietario = proprietario
        
    def get_proprietario(self) -> any:
        return self.__proprietario
    
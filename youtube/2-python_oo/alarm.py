class Alarm:
    
    def __init__(self, status:bool = False) -> None:
        self.__status = status
        
    
    def get_status(self) -> bool:
        return self.__status
        
    def set_status(self, value:bool = False) -> None:
        if isinstance(value, bool):
            self.__status = value   
        
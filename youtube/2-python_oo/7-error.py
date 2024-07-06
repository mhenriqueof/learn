class Error:
    
    @staticmethod
    def error_500() -> None:
        print('Server error')
        
    @staticmethod
    def error_404() -> None:
        print('Not found')
        

Error.error_500()
Error.error_404()
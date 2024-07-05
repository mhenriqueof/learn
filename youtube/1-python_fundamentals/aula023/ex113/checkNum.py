def leiaInt(num):
    while True:
        try:
            checkInt = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número INTEIRO!\033[m')
        except KeyboardInterrupt:
            print('\033[33mNada digitado!\033[m')
            return 0
        else:
            return checkInt
            

def leiaFloat(num):
    while True:
        try:
            checkFloat = str(input(num)).replace(',','.')
            checkFloat = float(checkFloat)
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número REAL!\033[m')
        except KeyboardInterrupt:
            print('\033[33mNada digitado!\033[m')
            return 0
        else:
            return float(checkFloat)
            
def check(pão):
    checkNum = str(input(pão)).strip().replace(',','.')
    while checkNum.isalpha() or checkNum == '':
        print('ERRO! Digite um número!')
        checkNum = str(input(pão))
    return float(checkNum)

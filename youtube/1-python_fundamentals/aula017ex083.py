# Módulos
import emoji
# Cores
be = '\033[34m'
ue = '\033[4m'
rd = '\033[31m'
gn = '\033[32m'
bwe = '\033[7m'
cc = '\033[m'

# Variáveis
pareab = parefe = 0

# Abertura
print(emoji.emojize(f':a: :x::heavy_plus_sign: :b:  Análise de Expressões',use_aliases=True))
# Estruturas
askexp = input(f'Expressão: ')
for a in range(len(askexp)):
    if askexp[a] in '(':
        pareab += 1
        parefe += -1
    elif askexp[a] in ')':
        parefe += 1
        pareab += -1
# Encerramento
check ='(' in askexp or ')' in askexp
if check == True:
    if pareab == 0:
        print(emoji.emojize(f'A expressão {bwe} {askexp} {cc} está {gn}correta{cc} em relação aos {ue}parênteses{cc}.:wink:',use_aliases=True))
    else:
        print(emoji.emojize(f'A expressão {bwe} {askexp} {cc} está {rd}errada{cc} em relação aos {ue}parênteses{cc}.:wink:',use_aliases=True))
else:
    print(emoji.emojize(f'A expressão {bwe} {askexp} {cc} está {be}não tem{cc} {ue}parênteses{cc}.:wink:',use_aliases=True))

# Módulos
import emoji
# Cores
bwe = '\033[7m'
we = '\033[1m'
pk = '\033[1;35m'
be = '\033[1;34m'
rd = '\033[31m'
yw = '\033[33m'
gn = '\033[32m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':underage: {bwe} Idade e Sexo {cc} :transgender_symbol:',use_aliases=True))
# Variáveis
idade = idacont = homcont = mulcont = 0
# Estruturas
while True:
    # Idade
    while True:
        idade = int(input(f'{we}Idade{cc}: '))
        if idade > 0 and idade < 150:
            if idade >= 18:
                idacont += 1
            break
        else:  
            idade = 0        
    # Sexo
    while True:
        while True:
            sexo = int(input(emoji.emojize(f'{we}Sexo{cc}:\n[{pk}0{cc}] para {pk}Feminino :female_sign:{cc}\n[{be}1{cc}] para {be}Masculino :male_sign:{cc}\n',use_aliases=True)))
            if sexo == 0 or sexo == 1:
                break
        if sexo >= 0 and sexo <= 1:
            if sexo == 1:
                homcont += 1
            if sexo == 0 and idade < 20:
                mulcont += 1
            break
        else:
            sexo = 0
    # Continuar?
    while True:
        ask = int(input(f'Deseja continuar?\n[{rd}0{cc}] para {rd}NÃO{cc} ou [{gn}1{cc}] para {gn}SIM{cc}\n'))
        if ask >= 0 and ask <=1:
            break
        else:
            ask = 0
    if ask == 0:
        break
    else:
        idade = 0
# Encerramento
print(emoji.emojize(f'Número de pessoas {yw}Maiores de 18 anos{cc}: {we}{idacont}{cc}\nNúmero de {be}Homens{cc}: {we}{homcont}{cc}\nNúmero de {pk}Mulheres com Menos de 20 anos{cc}: {we}{mulcont}{cc}',use_aliases=True))

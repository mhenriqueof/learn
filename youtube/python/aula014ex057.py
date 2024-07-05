# Módulos
import emoji
# Cores
p = '\033[1;35m'
b = '\033[1;34m'
w = '\033[1;97m'
bk = '\033[1;30m'
r = '\033[1;31m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f'{p}:female_sign: ?Qual{cc} {bk}o{cc} {b}Sexo? :male_sign:{cc}'))
# Estruturas
sexo = ''
while sexo != 'f' and sexo != 'm':
    sexo = str(input(f'{w}F{cc} para {p}Feminino{cc} ou {w}M{cc} para {b}Masculino{cc}\n')).strip().lower()
    if sexo != 'f' and sexo != 'm':
        print(f'{r}Erro!{cc} Por favor, digite',end=' ')
    if sexo == 'f':
        print(emoji.emojize(f'Sexo {p}Feminino :female_sign:{cc} escolhido.', use_aliases=True),end=' ')
    elif sexo == 'm':
        print(emoji.emojize(f'Sexo {b}Masculino :male_sign:{cc} escolhido.',use_aliases=True),end=' ')
print(emoji.emojize(f'{w}Obrigada pela resposta!{cc}:wink:',use_aliases=True))

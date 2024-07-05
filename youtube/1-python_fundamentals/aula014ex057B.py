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
sexo = str(input(f'{w}F{cc} para {p}Feminino{cc} ou {w}M{cc} para {b}Masculino{cc}\n')).strip().lower()[0]
while sexo not in 'mMFf':
    sexo = str(input(f'{r}Erro!{cc} Por favor, digite {w}F{cc} para {p}Feminino{cc} ou {w}M{cc} para {b}Masculino{cc}\n')).strip().lower()[0]
print(emoji.emojize(f'Sexo {sexo} registrado. {w}Obrigada pela resposta!{cc}:wink:',use_aliases=True))

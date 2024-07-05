# Módulos
import emoji
# Cores
cc = '\033[m'
# Fachada
print(emoji.emojize(f':older_woman: \033[1;97mEsclarecedor de Peso{cc} :older_adult:',use_aliases=True))
# Perguntas
massa = float(input('Qual é o seu peso em Kg? '))
altura = float(input('Qual é a sua altura em metros? (Não precisa colocar vírgula!) '))
# Cálculos
altu = float(altura / 100)
imc = massa / (altu ** 2)
# Condições
print(f'Seu IMC é \033[1;97m{imc:.1f}{cc}. ', end='')
if imc < 18.5:
    print(f'Você está \033[1;34mAbaixo do Peso Ideal{cc}.')
elif imc >= 18.5 and imc < 25:
    print(f'Você está no \033[1;32mPeso Ideal{cc}.')
elif imc >= 25 and imc < 30:
    print(f'Você está \033[1;36mAcima do Peso Ideal{cc}.')
elif imc >= 30 and imc < 40:
    print(f'Você está na \033[1;33mObesidade{cc}.')
else:
    print(f'Você está na \033[1;31mObesidade Mórbida{cc}.')
print(emoji.emojize(f'Obrigado por utilizar o :older_woman:\033[1;97m Esclarecedor de Peso{cc} :older_adult:!', use_aliases=True))

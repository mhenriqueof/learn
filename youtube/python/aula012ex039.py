# Módulos
import emoji
from datetime import date
data = date.today().year
import time
hora = int(time.strftime('%H',time.localtime()))
# Fachada
print(emoji.emojize(':gun: Bem-vindo ao \033[42mAlistamento do Exército Brasileiro\033[m! :gun:',use_aliases=True))
# Perguntas
nome = str(input('Olá! Qual é o seu nome? \n'))
name = nome.lower().capitalize()
ano = int(input('Em qual ano você nasceu? \n'))
time.sleep(.5)
# Cálculos
idade = int(data - ano)
falta = int(18 - idade)
passou = int((idade - 18))
# Condições
if idade < 18:
    print(emoji.emojize(f'{name}, você ainda não precisa se alistar! {"Faltam" if falta > 1 else "Falta"} {falta} {"anos" if falta > 1 else "ano"} para você se alistar ({data + falta}). :wink:', use_aliases=True))
elif idade == 18:
    print(emoji.emojize(f'{name}, você já está na idade para se alistar!:see_no_evil:', use_aliases=True))
    print(emoji.emojize('Acesse o site para mais informações!:slightly_smiling_face:', use_aliases=True))
else:
    print(emoji.emojize(f'{name}, já passou da hora de você se alistar! Seu alistamento era para ser feito há {passou} anos ({ano + 18}). :raised_eyebrow:', use_aliases=True))
    print(emoji.emojize('Acesse o site para mais informações!:slightly_smiling_face:', use_aliases=True))
# Despedida
if hora >= 6 and hora < 12:
    print(emoji.emojize('Tenha um bom dia!:sunrise:', use_aliases=True))
elif hora >=12 and hora < 18:
    print(emoji.emojize('Tenha uma boa tarde!:city_sunset:', use_aliases=True))
else:
    print(emoji.emojize('Tenha uma boa noite!:night_with_stars:', use_aliases=True))

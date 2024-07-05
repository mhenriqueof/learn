# Módulos
import emoji
# Cores
bbe = '\033[44m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f'{bbe} Maior {cc} :arrow_up:   {bbe} Menor {cc} :arrow_down:   {bbe} Posição {cc} :on:',use_aliases=True))
# Estruturas
nums = []
maipos = []
contmai = 0
menpos = []
contmen = 0
for rep in range(0, 5):
    nums.append(int(input(f'Valor da posição {rep}: ')))
print(nums)
for p, n in enumerate(nums):
    print(p, n)
    if n == max(nums):
        maipos.append(p)
        contmai += 1
    if n == min(nums):
        menpos.append(p)
        contmen += 1
print(f'O maior valor é o {max(nums)} {"na posição" if contmai == 1 else "nas posições"} {maipos}.\nO menor valor é o {min(nums)} {"na posição" if contmen == 1 else "nas posições"} {menpos}.')
# Encerramento
print(emoji.emojize(f'Você descobriu os maiores e menores valores com suas respectivas posições. :wink:',use_aliases=True))

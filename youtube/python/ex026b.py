frase = str(input('Digite uma frase: ')).strip()

low = frase.lower()
re = low.replace('á','a').replace('â','a').replace('à','a').replace('ã','a')
ca = re.count('a')
fa = re.find('a') + 1
la = re.rfind('a') + 1

print(f'A letra A aparece {ca} vezes.')
print(f'A posição do primeiro A é {fa}.')
print(f'A posição do último A é {la}.')

frase = str(input('Digite uma frase: ').strip())

jfrase = frase.split()
bfrase = ''.join(jfrase)
afrase = f' {bfrase}'

print(bfrase.count('a'))
print(bfrase.find('a'))
print(frase.rfind('a'))

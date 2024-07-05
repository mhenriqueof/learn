s = 0
cont = 0
for mult in range(3 , 500, 2):
    if mult % 3 == 0:
        cont += 1
        s += mult
print(f'A soma entre os {cont} números é {s}.')

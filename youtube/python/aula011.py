print('\033[1;31;44mHello!\033[m')

a = 1
b = 2

print(f'Valores \033[32m{a}\033[m e \033[7;32m{b}\033[m!!')
print(f'Valores \033[35m2\033[m e \033[7;35m1\033[m!!')

limpa = '\033[m'

print(f'Valores \033[32m{a}{limpa} e {b}!!')
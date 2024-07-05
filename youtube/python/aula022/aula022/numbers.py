from uteis import numeros

n = int(input('Digite um valor: '))
fat = numeros.fatorial(n)
print(f'O fatorial do número {n} é {fat}.\nSeu dobro é {numeros.dobro(n)}')

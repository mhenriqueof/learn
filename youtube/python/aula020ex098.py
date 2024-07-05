    # Contador #
# Modules
from time import sleep
# Functions
def contador(a, b, c): # Escolhas
    if a > b:
        if c > 0:
            c *= -1
        elif c == 0:
            c = -1
        b -= 1
    else:
        b += 1
    if a < 0:
        c *= -1
    for x in range(a, b, c):
        print(x, end=' ', flush=True)
        sleep(.0)
    print()    
    print('-' * 30)
    
    
# Code
contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez!')
contador(a = int(input('a1: ')), 
         b = int(input('an: ')), 
         c = int(input('Razão: ')))

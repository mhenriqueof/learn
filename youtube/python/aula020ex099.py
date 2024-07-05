    # Maior dentre eles #
# Modules
from random import randint as r
# Functions
def maior(*num):
    bigger = 0
    for a in num:
        if a > bigger:
            bigger = a
    print(f'Dentre os {len(num)} valores de {num} o maior é o {bigger}.')
            

# Code
maior(r(0,100), r(0,100), r(0,100), r(0,100), r(0,100), r(0,100))
maior(r(0,100), r(0,100), r(0,100))
maior(r(0,100), r(0,100))
maior(r(0,100))
maior()

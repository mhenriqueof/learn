lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for comida in lanche:
    print(f'Eu vou comer {comida}.')
    
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)) :
    print(f'Eu vou comer {lanche[cont]}.')
    
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
    
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(f'Eu vou comer {sorted(lanche)}.')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(8))

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
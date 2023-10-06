'''Crie um programa para verificar se uma string é um palíndromo.'''

h = ''
frase = str(input('Indique uma frase para inverter: '))

frase = frase.lower()

for i in range(len(frase) - 1, -1, -1):
    h = h + frase[i]
    
print(frase)

if h == frase:
    print('Es branco.')
else:
    print('Es preto')
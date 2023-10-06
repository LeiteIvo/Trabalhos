''' Crie um programa que inverta uma string.'''

h = ''
frase = str(input('Indique uma frase para inverter: '))

for i in range(len(frase) - 1, -1, -1):
    h = h + frase[i]
    
print(h)

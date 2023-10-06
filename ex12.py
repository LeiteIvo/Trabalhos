'''12) Altere o programa para produzir o seguinte efeito:
g
ng
ing
ring
tring
string
'''


frase2 = ''
frase = str(input("Indique uma frasee: "))

for i in range(len(frase) - 1, -1, -1):
    frase2 = frase[i] + frase2
    print(frase2)
    
'''Crie um programa de modo a que uma string seja impressa do seguinte modo:
S
St
Str
Stri
Strin
string'''

frase2 = ''
frase = str(input("Indique uma frasee: "))

for i in range(0, len(frase)):
    frase2 = frase2 + frase[i]
    print(frase2)
    
'''Crie um programa que indique qual de três strings introduzidas pelo utilizador 
tem um comprimento superior.'''

x = 0
string = ""
tamanho = 0
palavra = ""
while x != 3:
    string = str(input('Indique o valor da strinng: '))
    tamanho1 = len(string) + 1
    if tamanho < tamanho1:
        tamanho = tamanho1
        palavra = string
    x += 1
    
print(palavra)
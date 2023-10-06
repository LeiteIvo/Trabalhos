'''Crie um programa que leia 10 nomes para um vector de strings e os ordene 
alfabeticamente na saída.'''

listanomes = []
alfabeto = "abcdefghijklmnopqrstuvwxyz"

tamanho = 0

str1 = str(input("Indique uma oalavra: "))

x = 0
while x != 9:
    str2 = str(input('Indique mais uma palavra: '))
    
    if len(str1) > len(str2):
        tamanho = len(str2)
    else:
        tamanho = len(str1)

    for x in range(0, tamanho):
        for i in range(0, 26):
            if alfabeto[i] == str1[x] and alfabeto[i] == str2[x]:
                print("tudo igual para já") 
            else:
                if alfabeto[i] == str1[x] :
                    print("A str ", str1, " é primeiro. ")
                    listanomes = str(str1) + listanomes
                    listanomes.add(str2)
                    break
                else:
                    if alfabeto[i] == str2[x]:
                        listanomes = str(str2) + listanomes
                        listanomes.add(str1)
                        break
            str1 = str2
            break    
"""Crie um programa que leia 2 strings do utilizador e indique qual das strings está 
primeiro na ordem alfabética."""

alfabeto = "abcdefghijklmnopqrstuvwxyz"

tamanho = 0

decidido = 0

str1 = str(input("Indique uma oalavra: "))

str2 = str(input("Indique outra palavra: "))

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
                decidido = 1
                break
            else:
                if alfabeto[i] == str2[x]:
                    print("A str ", str2, " é primeiro. ")
                    decidido = 1
                    break
    if decidido == 1:
        break    
            


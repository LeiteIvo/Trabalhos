"""Crie um programa que, numa string substitua todas as letras “v” por “b” e todas 
as ocorrências de “ão” por “om”. """

str1 = str(input("Indique uma palavra para meter a portista: "))
str2 = ""
for i in range(len(str1)):
    print(i)
    if str1[i] != 'ã':
        if str1[i] == "v" or str1[i] == "V":
            str2 = str2 + "b"
            i = i + 1
        elif str1[i - 1] == "ã" and str1[i] == "o":
            str2 = str2 + "om"
            i = i + 1
            print(i)
        else:
            str2 = str2 + str1[i]   
    
print(str2)


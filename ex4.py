"""Crie um programa que “limpe” os espaços iniciais e finais de uma string."""

str1 = str(input("Indique uma frase: "))

for i in range(0, len(str1)):
    if str1[i] == " ":
        str1.replace(str1[i], "nn")
    else:
        break
    
for i in range(len(str1) - 1, -1 ,):
    if str1[i] == " ":
        str1.replace(str1[i], "nn")
    else:
        break

    
print(str1)
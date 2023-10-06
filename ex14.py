'''Escreva um programa que indique quantas vezes surge cada vogal numa string'''

avezes = 0
evezes = 0
ivezes = 0
ovezes = 0
uvezes = 0

palavra = str(input('Indique uma palavra: '))

for i in range(0, len(palavra)):
    if palavra[i] =='a' or palavra[i] == 'A' or palavra[i] == 'á' or palavra[i] == 'à' or palavra[i] == 'ã' :
        avezes += 1
    else:    
        if palavra[i] == 'e' or palavra[i] == 'E' or palavra[i] == 'é' or palavra[i] == 'è':
            evezes += 1
        else:
            if palavra[i] == 'i' or palavra[i] == 'I' or palavra[i] == 'í' or palavra[i] == 'ì':
                ivezes += 1
            else:
                if palavra[i] == 'O' or palavra[i] == 'o' or palavra[i] == 'õ':
                    ovezes += 1
      
    if palavra[i] == 'U' or palavra[i] == 'u':
        uvezes += 1
        
    
print('Tem', avezes, " o A")
print('Tem', evezes, " o E")
print('Tem', ivezes, " o I")
print('Tem', ovezes, " o O")
print('Tem', uvezes, " o U")
    
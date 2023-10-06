'''Crie uma função que verifique se uma password (passada como string) é válida. Para isso, deverá ter no mínimo 6 caracteres, dos quais, pelo menos 4 alfabéticos e um numérico. Não deverá ter espaços. A função deverá retornar true se a password for válida e false em caso contrário. Teste a função através de um programa que peça ao utilizador para introduzir duas vezes a password e faça a respetiva validação. O programa só termina, quando o utilizador introduzir uma password válida.'''

alfabeto = 'ABCDEEFGHIKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz'
alfabeticos = 0
numeros = '1234567890'
numerico = 0

password = str(input('Indique a sua nova pass: '))

if len(password) < 5:
    password = str(input('Indique uma nova pass valida com 6 caracteres: '))
    
while True:
    for i in range(0, len(password)):
        for x in range(0, len(numeros)):
            if password[i] == numeros[x]:
                numerico += 1
                break
        for v in range(0, len(alfabeto)):
            if password[i] == alfabeto[v]:
                alfabeticos += 1
                break
    if alfabeticos < 4 or numerico < 1:
        password = str(input('Indique uma nova pass valida com 6 caracteres em que 4 são alfabeticos e 1 numerico: '))
    else:
        break
    

while True:
    tentativo = str(input('Indique novamente a sua pass: '))

    if tentativo == password:
        print('valido')
        break
    else: 
        print('Invalido')




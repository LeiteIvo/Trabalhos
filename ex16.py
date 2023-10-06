'''Crie um programa que leia nomes do utilizador e termine quando for introduzido 
um nome repetido (ignorar maiúsculas e minúsculas).
'''

nome = ''
listadenomes = ''

while True:
    nome = str(input('Indique um nome: '))
    nome = nome.lower()
    if nome in listadenomes:
        print('Já inserido:',listadenomes)
        break
    else:
        listadenomes +=' ' + nome
        

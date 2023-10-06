'''33) Crie um método que receba um vector de strings como argumento e retorne um 
valor inteiro correspondendo à soma de todos os comprimentos das strings.'''

p = []
tamanhomaximo = 0
b = ' '

for i in range(1,4):
    x = str(input('Índique uma palavra: '))
    tamanhomaximo = tamanhomaximo + len(x)
        
    p.append(x)
    

    
print(tamanhomaximo)
    
    
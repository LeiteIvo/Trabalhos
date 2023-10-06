'''Escreva uma função que receba uma string e retorne o número de ocorrências de letras duplas consecutivas. Por exemplo, a string: “Passar a ferro” deverá indicar o valor 2, pois há dois pares de letras que ocorrem sucessivamente (“ss” e “rr”). O programa não deverá contar espaços duplos ou quaisquer outros caracteres não alfabéticos. Teste a função com a introdução da string pelo utilizador.'''

def duplo(x):
    confirmado = 0
    
    for i in range(0, len(x)):
        if x[i] == x[i - 1]:
            confirmado += 1
        if x[i] == x[i - 1] and  x[i] == x[i - 2]:
            confirmado -= 1
    return confirmado


x = str(input('Indique uma palavra: '))

v = duplo(x)

print(v)


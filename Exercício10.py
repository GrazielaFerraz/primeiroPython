#10.Escreva um algoritmo que calcule a média dos números
# digitados pelo usuário,se eles forem pares.Termine
# a leitura se o usuário digitar zero(0);

def media():
    num1 = 1
    soma = 0
    qtde = 0

    while(num1 != 0):
        num1 = int(input('Digite um número'))
        if (num1 % 2 == 0): #verificando se o nº é par
            soma += num1 #somando os pares
            qtde += 1 #contando os pares
    return 'A media dos pares digitados é: {}'.format(soma/qtde)

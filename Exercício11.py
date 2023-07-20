#11.Escreva um algoritmo que leia valores inteiros
# e encontre o maior e o menor deles.
# Termine a leitura se o usuário digitar zero(0);

def maiorMenor():
    maior = 0
    menor = 0
    num = 1
    flag = False #Valor lógico, que representa um valor binário ex: ligado/desligado, falso/verdadeiro

    while (num != 0):
        num = int(input('Digite um número: '))
        if(num !=0):
            if(flag == False):
            # Na Primeira vez do codigo, eu instancio a variável
                maior = num
                menor = num
                flag = True

            #Definir o maior e menor
            if(num > maior):
                maior = num

            if (num < menor):
                menor = num

    return 'Maior: {} \n Menor: {}'.format(maior, menor)

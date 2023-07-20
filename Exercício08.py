#8.Escrever um algoritimo que leia 10
#números inteiros e, ao final, apresente a
#soma de todos os números lidos;

def somarInteiro():
    soma = 0 #instanciar a variável
    for i in range(1,11,1):
        num = int(input('{}º número:'.format (i)))
        soma += num

    return 'A soma dos digitados foi de: {}'.format(soma)


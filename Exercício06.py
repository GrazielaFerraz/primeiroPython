#6. Faça um algoritimo que escreva na tela
#os números de um número inicial a um
#numero final.Os números inicial e final
#devem ser informados pelo usuário

def inicialFinal(n1, n2):

        if(n1 > n2):
            for i in range(n1, n2 - 1,-1):
                print(i)
        else:
            for i in range (n1, n2+1):
                print(i)
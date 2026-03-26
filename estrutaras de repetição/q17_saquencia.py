def main():

    numero = int(input('Digite a quantidade números: '))

    sequencia(numero)










def sequencia(numero):

    soma = 0

    for n in range(1, numero + 1):
       
        soma += 1/n

    
    print(f'{soma}')





main()
def main():

    numero = int(input('Digite a quantidade números: '))


    soma_media(numero)










def soma_media(numero):

    soma = 0

    for i in range(numero):
        
        num = int(input('Digite o número: '))

        soma = num + soma 

    media = soma // numero

    print(f'média: {media}')
    print(f'Soma: {soma}')

        




main()
def main():

    numero_hab = int(input('Digite a quantidade de habitantes: '))

    calcular(numero_hab)









def calcular(numero):

    contador_ate1000 = 0

    n_filhos = 0

    n_salario = 0



    for i in range(numero):

        filhos = int(input('Dgite a quantidade de filhos: '))
        salario = int(input('Digite o salário: '))
        print()

        n_filhos += filhos

        n_salario += salario

        if salario <= 1000:
            contador_ate1000 += 1



    media_filhos = n_filhos / numero

    media_salario = n_salario / numero

    percengtual_1000 = (contador_ate1000 / numero) * 100


    print(f'A média de filhos: {media_filhos: .2f}')
    print(f'A média salário: {media_salario: .2f}')
    print(f'Percentual de salários até 1000: {percengtual_1000: .0f}%')













main()
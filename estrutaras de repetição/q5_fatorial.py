def main():

    numero = int(input('Digite o número: '))

    fatoral(numero)















def fatoral(n):

    multiplicacao = 1

    for i in range(1, n + 1):
        
        multiplicacao = multiplicacao * i

    print(multiplicacao)







main()
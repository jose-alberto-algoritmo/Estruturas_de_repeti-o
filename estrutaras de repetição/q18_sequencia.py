def main():

    numero = int(input('Digite o número: '))

    sequencia_(numero)














def sequencia_(n):

    for i in range(1, n +1):
     
     numerador = i

     denominador = n - i + 1
     
     s = numerador/denominador
     
     total += s
    


     print(f'{total: .2f}')















main()
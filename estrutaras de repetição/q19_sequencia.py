def main():
    
    numero = int(input('Digite a quantidades de números: '))

    calcular(numero)



    











def calcular(n):
    total = 0

    

    
    
    for i in range(1, n + 1):

        if i % 2 == 0:

            denominador = i

            numerador = n - i + 1

            soma = (numerador/ denominador) * (-1)

            total += soma 

        

        if i % 2 != 0:
            denominador = n - i + 1

            numerador = i

            soma = (numerador/ denominador)

            total += soma
    
    
    
    print(total)


        















main()
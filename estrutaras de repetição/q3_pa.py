def main():

    
    a0 = int(input('Digite o A0: '))

    razao = int(input('Digite a razão: '))

    limit = int(input('Digite o limite: '))

    limite(a0, razao, limit)














def limite(a0, razao, limite):
    
   for n in range (a0, limite + 1, razao):
       
       print(n)



































main()
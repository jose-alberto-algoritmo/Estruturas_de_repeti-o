def main(): 

    a0 = int(input('Digite o termo ínicial: '))
    razao = int(input('Dgite a razão: '))
    limite = int(input('Digite o limite: '))

    atual = a0

    
    
    for n in range(a0, limite + 1):

        atual = atual * razao 

        if atual <= limite:

            print(atual, end=' , ')
































main()
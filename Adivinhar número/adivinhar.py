import random

def main():

    print('***Número secreto***')

    numero = int(input('Digite um número de 1 a 100: '))

    numero_sorteado = random.randint(1, 100)

    contador = 1

    pontuacao = 100



    
    
    
    
    while numero != numero_sorteado and contador < 10:

        

        print('ERROU!!')

        if numero > numero_sorteado:

            print('>>>O sorteado é menor do que o número lido')

        else:
            print('>>>O número sorteado é maior do que o número lido')

        
        numero = int(input('>>Digite um novo número: '))
        
        contador = contador + 1
        
        pontuacao = pontuacao - 10 

        
        
        if numero == numero_sorteado:

            print ('>>>>>ACERTOU!!')

        if contador == 10:
            print('>>>>>PERDEU!!')

    






    print(f'>>>>>>>O número sorteado é {numero_sorteado}')

    print(f'>>>>>>>>>>>Pontuação: {pontuacao}')





        




main()
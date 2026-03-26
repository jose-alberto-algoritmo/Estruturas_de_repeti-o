def main():

    numero_fichas = int(input('Digite o número de fichas: '))

    contrle_manada(numero_fichas)















def contrle_manada(numero):

    maior_peso = 0

    menor_peso = 0


    for n in range(numero):

        nome = input('Digite o nome: ')
        num_identifacao = input('Digite o número da identificação: ')
        peso = float(input('Digite o peso do boi: '))

        if n == 0:
            nome_maior = nome 
           
            maior_peso = peso
           
            id_maior = num_identifacao


            nome_menor = nome
            
            menor_peso = peso
            
            id_menor = num_identifacao

        else:
            
            if peso > maior_peso:
                
                nome_maior = nome 
           
                maior_peso = peso
           
                id_maior = num_identifacao

        
           
            if peso < menor_peso:
                
                nome_menor = nome
            
                menor_peso = peso
            
                id_menor = num_identifacao

       

      


    print('****Ficha do maior****')
    print()
    print(f'nome: {nome_maior}')
    print(f'número de identificação: {id_maior}')
    print(f'peso kg: {maior_peso}')
    
    print()
    print()
    
    print('****Ficha do menor****')
    print()
    print(f'nome: {nome_menor}')
    print(f'número de identificação: {id_menor}')
    print(f'peso kg: {menor_peso}')








main()
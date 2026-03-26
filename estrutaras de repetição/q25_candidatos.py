def main():

    n_candidatos = int(input('Digite o número de candidatos: '))

    candidato(n_candidatos)









def candidato(numero):

    candidato_1 = 0

    candidato_2 = 0

    candidato_3 = 0

    nulo = 0 

    branco = 0

    n_candidato = 0

    for i in range(numero):

        n_candidato += 1



        print(f'Eleitor_{n_candidato}')
        print()
        voto = int(input('Digite o seu voto: '))
        print()

        if voto == 1:
            candidato_1 += 1


        if voto == 2:
            candidato_2 += 1

        if voto == 3:
            candidato_3 += 1


        if voto == 9:
            nulo += 1

        if voto == 0:

            branco += 1

    
    
    
    if candidato_1 > candidato_2 and candidato_1 > candidato_3:
        
        print(f'caditato_1 votos: {candidato_1}')
        print(f'caditato_2 votos: {candidato_2}')
        print(f'caditato_3 votos: {candidato_3}')
        print(f'Votos nulos: {nulo}')
        print(f'Votos em branco: {branco}')
        print()
        print('Vencedor da eleição: Candidato_1')


    elif candidato_2 > candidato_3 and candidato_2 > candidato_1:
        
        print(f'caditato_1 votos: {candidato_1}')
        print(f'caditato_2 votos: {candidato_2}')
        print(f'caditato_3 votos: {candidato_3}')
        print(f'Votos nulos: {nulo}')
        print(f'Votos em branco: {branco}')
        print()
        print('Vencedor da eleição: Candidato_2')

    else:
        candidato_3 > candidato_2 and candidato_3 > candidato_1
        
        print(f'caditato_1 votos: {candidato_1}')
        print(f'caditato_2 votos: {candidato_2}')
        print(f'caditato_3 votos: {candidato_3}')
        print(f'Votos nulos: {nulo}')
        print(f'Votos em branco: {branco}')
        print()
        print('Vencedor da eleição: Candidato_3')
        

        





















main()
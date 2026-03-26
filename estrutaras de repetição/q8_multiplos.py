def main():


    limt_inf = int(input('Digite o início: '))
    limt_super = int(input('Digite o limite: '))

    numero = int(input('Digite o número: '))

    multiplo(numero, limt_inf, limt_super)












def multiplo(n, limt_inf, limit_super):
    
    for i in range(limt_inf, limit_super + 1):
    
        if i % n == 0: 
            print(i)
        
       





main()
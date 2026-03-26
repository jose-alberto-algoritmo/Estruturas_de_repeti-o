def main():
    limt_inf = int(input('Digite o início: '))
    limt_super = int(input('Digite o limite: '))


    emetir_(limt_inf, limt_super)

    



def eh_primo(numero):

    for n in range (2, numero // 2 + 1):
        
        if numero % n == 0:
            
            return False
        
    return True       



def emetir_(limt_inf, limt_super):

    for n in range (limt_inf, limt_super + 1):
        
        if eh_primo(n) :
            
            print(n)

            



main()
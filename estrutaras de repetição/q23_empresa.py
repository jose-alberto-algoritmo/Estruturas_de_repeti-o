def main():

    numero = int(input('Digite a quantidade de funcionários: '))

    calculo(numero)











def calculo(numero):

    

    for n in range(numero):

        codigo = int(input('Digite o código do funcionário: '))
        
        horas = int(input('Digite a quantidade de horas trabalhadas pelo funcionário: '))
        
        dependentes = int (input('Digite a quandtidade de dependetes do funcinário: '))

        
        
        
        salario_total = ((horas * 12) + (dependentes * 40)) * 30

        desc_inss = salario_total * 0.085

        desc_ir = salario_total * 0.05

        desconto_total = desc_inss + desc_ir

        
        salario_liquido = salario_total - desconto_total


        print('**( Tabela***)')
        print()

        print(f'>>>Código funcinário: {codigo}')
        print(f'>>>Salário bruto: {salario_total: .2f}')
        print(f'>>>Desconto INSS: {desc_inss: .2f}')
        print(f'>>>Desconto IR: {desc_ir: .2f}')
        print(f'>>>Salério líquido: {salario_liquido: .2f}')
        print()
        print()










main()
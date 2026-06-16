macas = int(input('Digite a quanitade de maçãs vendidas: '))
bananas = int(input('Digite a quanitade de bananas vendidas: '))

if macas > bananas:
    print('Maças tiveram mais vendas')
elif macas < bananas:
    print('Bananas tiveram mais vendas')
else:
    print('As vendas foram iguais')        


#Calculando o tempo total de projeto    

a = int(input('Informe os dias para a atividade A: '))
b = int(input('Informe os dias para a atividade B: '))
c = int(input('Informe os dias para a atividade C: '))

if (a >=0 and b >=0  and c >=0 ):
    valor_total = a + b + c
    print(f'O tempo total do projeto é: {valor_total}')

else:
    print('Erro: Os dias não podem ser negativos')    

    

#Controlando o orçamento mensal
limite = 3000
despesas = float(input('Digite o total de despesas do mês: R$'))

if despesas > limite:
    print('Atenção, você ultrapassou o limite do orçamento')
else:
    print('Você está dentro do orçamento')

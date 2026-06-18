renda = float(input('Digite o valor da sua renda mensal: '))
parcela = float(input('Digite o valor da sua parcela desejada: '))

if renda > 2000 and parcela <= 0.3 * renda:
    print('Emprestimo aprovado')
elif renda <=2000:
    print('Valor da renda é baixo')
else:
    print('Emprestimo negado: parcela acima de 30% da renda.')    

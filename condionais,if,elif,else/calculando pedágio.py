#Calculando pedágio

distancia = float(input('Digite a distancia percorrida (em km): '))

if distancia <=100 :
    print('Valor pago R$10,00')
elif 100<= distancia <=200:
    print('Valor pago R$20,00')  
else:
    print('Pague R$30,00')      
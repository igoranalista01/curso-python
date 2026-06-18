peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura m: '))
imc = peso/(altura**2)

print(f'Seu IMC é: {imc}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')    
else:
    print('Voce está acima do peso')       

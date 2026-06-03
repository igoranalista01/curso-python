#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual

numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Soneca','Igor','Santos','Soares']
ano = [1996,2026]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

frutas = ['banana','melancia','coco','morango']

for fruta in frutas:
    print(fruta)
print()

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.    

soma_impares = 0
for i in range(1,11,2):
    soma_impares += i
print(soma_impares)
print()

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(10,0,-1):
    print(i)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.    
numero_tabuaba = int(input('Digite um número para a tabuada: '))
for i in range(1,10):
    resultado= numero_tabuaba *i
    print(f'{numero_tabuaba} x {i} = {resultado}')

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.    

lista_de_numeros = [10,10,10]
soma = 0

try:
    for numero in lista_de_numeros:
        soma += numero
        print(f'A soma dos elementos na lista é {soma}')
except Exception as e:
    print(f'Ocorreu um erro:{e}')

#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia. 

lista_valores = [15, 20, 25, 30]
soma_valores = 0   

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f'A media dos valores: {media}') 
    
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")   
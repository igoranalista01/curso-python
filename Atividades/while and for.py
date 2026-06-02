#esse é um cenário em que um loop while é mais apropriado, pois não sabemos com antecedência quantas vezes precisaremos solicitar ao usuário que insira um número, neste caso ele vai digita até acertar o que estamos pedindo, que neste caso é um numero positivo!!
numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)  

#Perceba que, para criar esse loop, precisamos definir um número arbitrário de tentativas para que o usuário inserisse esse valor. Isso acontece porque o loop for é utilizado quando se conhece previamente o número de iterações que devem ser realizadas.
numero =-1
for _ in range(3):
    numero= int(input('Digite um numero positivo: '))
    if numero > 0:
        break
    print(f'Você digitou o numero: {numero}')
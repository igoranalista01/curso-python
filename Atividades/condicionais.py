#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
numero = int(input('Digite um numero impar ou par: '))
if numero % 2 == 0:
    print('Esse numero é par\n')
else:
    print('Esse numero é impar\n')    

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:    
idade = int(input('Digite sua idade: '))
if 0< idade <=12:
    print('Você é uma criança\n') 
elif 12< idade <18 :
    print('Você é um adolescente\n')
elif idade >=18 :
    print('Você é um adulto\n')
else:
    print('é uma anomalia\n')
    
#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você. 
nome_deve_ser = 'soneca96'
senha_deve_ser = '96827496'

nome = input('Digite o nome de usuario para cadastro: ')
senha = input('Digite a senha para cadastro: ')


if nome == nome_deve_ser and senha == senha_deve_ser:
    print('Login e Senha corretos!\n')
else:
    print('Dados incorretos, digite novamente!\n')    

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:4

x = int(input('Digite o numero da cordenada x: '))
y = int(input('Digite o numero da cordenada y: '))

if x>0 and y>0:
    print('Primeiro Quadrante')
elif x<0 and y>0:
    print('Segundo Quadrante')
elif x<0 and y<0:
    print('Terceiro Quadrante')
elif x>0 and y<0:
    print('Quarto Quadrante')
else:
    print('O ponto está localizado no eixo ou origem')
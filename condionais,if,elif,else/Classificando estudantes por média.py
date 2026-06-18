#Classificando estudantes por média

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite  a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))

resultado_com_media = (primeira_nota + segunda_nota + terceira_nota)/3
print(f'Média: {resultado_com_media}')

if resultado_com_media >=7:
    print('Aprovado')
elif 5<= resultado_com_media <7:
    print('Recuperação')
else:
    print('Reprovado')        
num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))

media = (num1 + num2) / 2

if (media<6):
    print('Reprova')
else:
    print('aprovado')
print('Nota: {}'.format(media))

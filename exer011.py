quantia = float(input('Digite quanto você possui: '))
moeda = str(input('Para qual moeda irá converter? '))
cotacao = float(input('Digite a cotação da moeda que deseja converter: '))

resultado = quantia / cotacao

print('Atualmente você pode comprar {:.2f} em {} com {}'.format(resultado, moeda, quantia))
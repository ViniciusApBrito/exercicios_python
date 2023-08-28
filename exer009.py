valor = float(input('Digite uma medida em metro: '))

centimetro = (valor / 100)
milimetro = (valor / 1000)

print(' Valor em cm: {} \n Valor em mm {} \n Valor inserido {}'.format(centimetro,milimetro,valor))
preco = float(input("diga o preço do produto: "))

desconto = (preco * 0.05)
novo_preco = (preco - desconto)

print('Para o preço de {} com o desconto de 5%, custará {}'.format(preco,novo_preco))   
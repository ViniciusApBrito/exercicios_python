valor = input('Digite algo: ')

if valor.isnumeric():
    print('Você digitou um número.')
elif valor.isalpha():
    if valor.islower():
        print('Você digitou letras minúsculas.')
    elif valor.isupper():
        print('Você digitou letras maiúsculas.')
elif valor.isalnum():
    print('Você digitou uma combinação de letras e números')
elif valor.isprintable():
    print('Você digitou caracteres especiais.')
else:
    print('Não identificavel')

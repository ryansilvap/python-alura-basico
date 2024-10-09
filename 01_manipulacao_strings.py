# 1 - Imprima a frase: Python na Escola de Programação da Alura.
print('Python na escola de programação da Alura')

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
name = "Ryan"
age = 23
print(f'Meu nome é {name} e eu tenho {age} anos.\n')

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha
print('A\nL\nU\nR\nA\n')
print('A','L','U','R','A',sep='\n')

# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
pi = 3.14159
pi_arredondado = round(pi, 2)
print(f'\nO valor arredondado de pi é {pi:.2f}')
print(f'O valor arrendodado de pi é: {pi_arredondado}')
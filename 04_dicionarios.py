# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoa = {
    'nome' : 'Ryan',
    'idade' : 23,
    'cidade' : 'Pirapora'
}
print(pessoa)

# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
pessoa['cidade'] = 'Belo Horizonte' #or pessoa.update({'cidade': 'Belo Horizonte'})
print(pessoa)

# Adicione um campo de profissão para essa pessoa;
pessoa['profissao'] = 'Software Engineer' #or pessoa.update({'profissao': 'Software Engineer'})
print(pessoa)

# Remova um item do dicionário.
pessoa.pop('idade') #or del pessoa['idade']
print(pessoa)

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
numeros = [1, 2, 3, 4, 5]
quadrados = {}

for numero in numeros:
    quadrados[numero] = numero * numero
print(quadrados)

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
estudante = {
    'nome' : 'Ryan',
    'curso' : 'Sistemas de Informação',
    'coeficiente_rendimento': 83
}
print(f'A chave "nome" existe.' if estudante.get('nome') else 'A chave "nome" não existe.')

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = 'Estou aprendendo a linguagem de programação Python'
palavras = frase.split()

contador = {}

for palavra in palavras:
    contador[palavra] = contador.get(palavra, 0) + 1
print(contador)


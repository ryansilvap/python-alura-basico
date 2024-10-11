# 1 - Crie uma lista para cada informação a seguir:
#
#     Lista de números de 1 a 10;
#     Lista com quatro nomes;
#     Lista com o ano que você nasceu e o ano atual.

numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ["Kim", "Kelly", "John", "Paul"]
nascimento_ano_atual = [2001, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

for numero in numeros:
    print(numero)

for nome in nomes:
    print(nome)

for item in nascimento_ano_atual:
    print(item)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

#soma de todos os números de 1 a 10.
def soma_1_ate_10():
    soma = 0
    for i in range(1, 11):
        soma += i
    return soma
print(soma_1_ate_10())

#soma dos números ímpares de 1 a 10.
def soma_impar_1_ate_10():
    soma = 0
    for i in range(1, 11, 2):
        soma += i
    return soma
print(soma_impar_1_ate_10())

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(10, 0, -1):
    print(i)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
def tabuada(num):
    for i in range(1, 11):
        print(f'{i} * {num} = {i * num}')
tabuada(int(input("\nDigite um número: ")))

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

numeros = [1,'l',3,4,None,6,7,8,-1]

def soma_numeros(numeros):
    soma = 0
    for i in numeros:
        try:
            soma += i
        except TypeError as err:
            print(err)
    return soma

print(soma_numeros(numeros))

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

numeros = []

def media(numeros):
    soma = 0
    try:
        for i in numeros:
            soma += i
        media = soma / len(numeros)
        return media
    except ZeroDivisionError as err:
        print(err)

print(media(numeros))


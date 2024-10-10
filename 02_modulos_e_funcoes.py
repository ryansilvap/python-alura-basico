# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

def par_ou_impar (num):
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")

par_ou_impar (int(input("Digite um número: ")))

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

    # Criança: 0 a 12 anos;
    # Adolescente: 13 a 18 anos;
    # Adulto: acima de 18 anos.

def idade (idade):
    if 0 <= idade <= 12:
        print("Criança.")
    elif 13 <= idade < 18:
        print("Adolescente.")
    else:
        print("Adulto.")

idade (int(input("Digite sua idade: ")))

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

def login (user, password):
    user_padrao = "ryan"
    password_padrao = "password"
    if user == user_padrao and password_padrao == password:
        print("Login efetuado com sucesso!")
    else:
        print("Usuário ou senha incorreta.")

login (input("Login: "), input("Password: "))

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
#
#     Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#     Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#     Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#     Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#     Caso contrário: o ponto está localizado no eixo ou origem.

def coordenadas (x, y):
    if x > 0 and y > 0:
        print("Primeiro quadrante.")
    elif x < 0 < y:
        print("Segundo quadrante.")
    elif x < 0 and y < 0:
        print("Terceiro quadrante.")
    elif y < 0 < x:
        print("Quarto quadrante.")
    else:
        print("O ponto está localizado no eixo ou origem")

coordenadas(float(input("Valor de x: ")), float(input("Valor de y: ")))


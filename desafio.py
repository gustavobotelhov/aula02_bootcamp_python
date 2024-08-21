### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# e se o usuario digitar um número? explorar possibilidades de erro.

# nome_usuario = input("Digite o seu nome: ")

# if nome_usuario.isdigit():
#     print("Você digitou o seu nome errado.")
#     exit()
# elif len(nome_usuario) == 0:
#     print("Você não digitou nada.")
#     exit()
# elif nome_usuario.isspace():
#     print("Você digitou só espaço")
#     exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario_usuario = float(input("Digite o seu salario: "))

try:
    if salario_usuario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# bonus_usuario = float(input("Digite o bonus recebido: "))

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# print(f"O usuario {nome_usuario} recebeu o bonus de: {bonus_usuario}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
import math
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero_01 = int(input("Digite um numero: "))
# numero_02 = int(input("Digite outro numero: "))
# print(numero_01+numero_02)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# numero_01 = int(input("Digite um numero: "))
# resultado = numero_01 % 5
# print(resultado)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# numero_01 = int(input("Digite um numero: "))
# numero_02 = int(input("Digite outro numero: "))
# print(numero_01*numero_02)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# try:
#     numero_01 = int(input("Digite um numero: "))
#     numero_02 = int(input("Digite outro numero: "))
#     resultado = numero_01 // numero_02
#     print(resultado)
# except:
#     print("Não é possível realizar a divisão.")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# numero_do_usuario = int(input("Digite um número: "))
# resultado = numero_do_usuario ** 2
# print(resultado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# numero_01 = float(input("Digite um numero: "))
# numero_02 = float(input("Digite outro numero: "))
# print(numero_01 + numero_02)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# numero_01 = float(input("Digite um numero: "))
# numero_02 = float(input("Digite outro numero: "))
# media = (numero_01+numero_02) / 2
# print(media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# base = float(input("Digite a base: "))
# expoente = float(input("Digite o expoente: "))
# potencia = base ** expoente
# print(potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# celsius = float(input("Digite a temperatura em Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"A temperatura em fahrenheit é de: {fahrenheit}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio_do_circulo = float(input("Digite o raio:"))
# area_do_circulo = math.pi * raio_do_circulo ** 2
# area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
# area_do_circulo_formata2 = print(f"{area do circulo:.2f}") é a mesma coisa da linha de cima
# print(area_do_circulo_formatada)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# string_do_usuario = input("Digite um texto: ")
# string_maiuscula = string_do_usuario.upper()
# print(string_maiuscula)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# string_do_usuario = input("Digite um texto: ")
# string_maiuscula = string_do_usuario.lower()
# print(string_maiuscula)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input("Digite uma frase: ")
# print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data_do_usuario = input("Digite uma data no formato dd/mm/aaaa: ")
# data_separada = data_do_usuario.split("/")

# dia = data_separada[0]
# mes = data_separada[1]
# ano = data_separada[2]
# print(f"A data digita é: {dia}/{mes}/{ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# string_1 = input("Digite um texto: ")
# string_2 = input("Digite outro texto: ")

# print(string_1+" "+string_2)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# expressao_1 = input("Digite uma expressao booleana: ")
# expressao_2 = input("Digite outra expressao booleana: ")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# valor_1 = input("Digite uma valor: ")
# valor_2 = input("Digite outro valor: ")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

valor_1 = input("Digite uma valor: ")
valor_2 = input("Digite outro valor: ")

resultado = valor_1 == valor_2

if valor_1 == valor_2:
    print("Os dois números são iguais.")
else:
    print("Os dois números são diferentes.")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação

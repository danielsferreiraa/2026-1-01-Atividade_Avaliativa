num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))
num4 = float(input("Insira o quarto número: "))

prod = num1 * num2 * num3 * num4

print(f'O produto dos 4 números é: {prod}')

if prod > 0:
    print(f'O produto é positivo.')
else:
    print(f'O produto não é positivo.')

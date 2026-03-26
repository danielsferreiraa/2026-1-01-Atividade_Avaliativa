num1 = int(input("Insira o primeiro número inteiro: "))
num2 = int(input("Insira o segundo número inteiro: "))
num3 = int(input("Insira o terceiro número inteiro: "))
num4 = int(input("Insira o quarto número inteiro: "))

soma = num1 + num2 + num3 + num4

print(f'A soma dos 4 números é: {soma}')

if soma > 100:
    print(f'A soma é maior que 100.')
else:
    print(f'A soma não é maior que 100.')


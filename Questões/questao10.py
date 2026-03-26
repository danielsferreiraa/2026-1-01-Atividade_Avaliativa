num1 = int(input("Insira o primeiro número inteiro: "))
num2 = int(input("Insira o segundo número inteiro: "))
num3 = int(input("Insira o terceiro número inteiro: "))
num4 = int(input("Insira o quarto número inteiro: "))

med = (num1 + num2 + num3 + num4) / 4

print(f'A média é: {med}')

if med >= 6:
    print(f'Situação: Aprovado(a)!')
else:
    print(f'Situação: Reprovado(a)')


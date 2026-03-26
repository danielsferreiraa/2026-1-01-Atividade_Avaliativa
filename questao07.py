num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))
num4 = float(input("Insira o quarto número: "))

med = (num1 + num2 + num3 + num4) / 4

numeros = [num1, num2, num3, num4]
dif = max(numeros) - min(numeros)

print(f'A média aritmética é: {med}')
print(f'A diferença entre o maior e o menor valor é: {dif}')
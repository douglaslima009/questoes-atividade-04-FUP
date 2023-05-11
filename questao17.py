num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma_pares = 0
mult_impares = 1
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        soma_pares += i
    else:
        mult_impares *= i

print("A soma dos números pares do intervalo é:", soma_pares)
print("A multiplicação dos números ímpares do intervalo é:", mult_impares)
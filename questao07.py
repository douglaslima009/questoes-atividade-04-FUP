numeros = []
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)
print("A média dos números digitados é:", media)
num = int(input("Digite um número inteiro positivo: "))
divisores = []
for i in range(1, num+1):
    if num % i == 0:
        divisores.append(i)

print("Os divisores de", num, "são:", divisores)

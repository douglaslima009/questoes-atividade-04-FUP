soma = 0
contagem = 0
for i in range(10):
    num = int(input("Digite um número inteiro positivo: "))
    if num > 0:
        soma += num
        contagem += 1

media = soma / contagem
print("A média dos números positivos digitados é:", media)
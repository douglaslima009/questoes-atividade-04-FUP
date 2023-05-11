saque = int(input("Digite o valor do saque: "))
notas = [100, 50, 20, 10, 5, 2, 1]
quantidades = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(notas)):
    while saque >= notas[i]:
        saque -= notas[i]
        quantidades[i] += 1

print("Quantidade de notas:")
for i in range(len(notas)):
    if quantidades[i] > 0:
        print(f"{quantidades[i]} nota(s) de {notas[i]} reais")
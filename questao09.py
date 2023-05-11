numeros = []
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)
print(f"O menor número lido é {menor}")
print(f"O maior número lido é {maior}")
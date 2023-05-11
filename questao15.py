quantidade = int(input("Quantos números você quer ler? "))
num = []
maior = None
contador = 0
for i in range(quantidade):
    number = float(input(f"Digite o {i+1}º número: "))
    num.append(number)
    if maior is None or number > maior:
        maior = number
        contador = 1
    elif number == maior:
        contador += 1

print(f"O maior número digitado foi {maior} e foi lido {contador} vezes.")
number = []
while True:
    num = int(input("Digite um número inteiro (digite um número negativo para encerrar): "))
    if num < 0:
        break
    number.append(num)
    
if len(number) == 0:
    print("Nenhum número foi digitado.")
else:
    maior = max(number)
    menor = min(number)

    print(f"O maior número digitado foi {maior} e o menor número foi {menor}.")
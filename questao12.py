num = int(input("Digite um número inteiro não negativo: "))

if num < 0:
    print("Erro: o número digitado é negativo!")
elif num != int(num):
    print("Erro: o número digitado não é inteiro!")
else:
    fatorial = 1
    for i in range(1, num+1):
        fatorial *= i
    print(f"O fatorial de {num} é {fatorial}.")

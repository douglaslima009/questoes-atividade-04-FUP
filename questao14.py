num = int(input("Digite um número inteiro: "))
if num < 2:
    print("Não é um número primo.")
else:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print("É um número primo.")
    else:
        print("Não é um número primo.")
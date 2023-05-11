num = int(input("Digite um valor inteiro e positivo para N: "))
e = 1
fatorial = 1
for i in range(1, num+1):
    fatorial *= i
    e += 1/fatorial

print("O valor de E para N =", num, "é:", e)
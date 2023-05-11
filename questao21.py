n = int(input("Digite um número inteiro positivo: "))
h = 0
for i in range(1, n+1):
    h += 1/i

print("O número harmônico H({}) é {:.2f}".format(n, h))
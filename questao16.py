num = int(input("Digite um valor inteiro n: "))
if num < 1:
    print("O valor de n deve ser maior ou igual a 1.")
else:
    fib1 = 1
    fib2 = 1
    for i in range(3, num+1):
        fibn = fib1 + fib2
        fib1 = fib2
        fib2 = fibn

    print(f"O {num}-ésimo número de Fibonacci é: {fib2}")
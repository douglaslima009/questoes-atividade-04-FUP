import math
while True:
    num = float(input("Digite um valor (0 para sair): "))
    if num == 0:
        break
    quadrado = num ** 2
    cubo = num ** 3
    raiz_quadrada = math.sqrt(num)
    
    print(f"Valor: {num} | Quadrado: {quadrado} | Cubo: {cubo} | Raiz quadrada: {raiz_quadrada}")
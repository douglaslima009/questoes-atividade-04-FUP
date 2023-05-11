def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

while True:
    print("Calculadora de operações matemáticas")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = int(input("Digite sua opção (1/2/3/4/5): "))
    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", adicao(num1, num2))
    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", subtracao(num1, num2))
    elif opcao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", multiplicacao(num1, num2))
    elif opcao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", divisao(num1, num2))
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
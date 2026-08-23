# Exercício 1: Algoritmo básico
# Problema:
# Desenvolva um algoritmo que leia dois números inteiros e apresente:
# • Soma
# • Subtração
# • Multiplicação
# • Divisão
# Desafio:
# Trate a situação em que o segundo número seja zero


def readInt(msg: str = ""):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido e tente novamente.")


def main():
    a = readInt("Digite o primeiro número: ")
    b = readInt("Digite o segundo número: ")

    print("Soma:", a + b)
    print("Subtração:", a - b)
    print("Multiplicação:", a * b)
    print("Divisão:", a / b if b != 0 else "Impossível dividir por 0.")


if __name__ == "__main__":
    main()

# Exercício 3: Estruturas de repetição
# Problema:
# Crie um algoritmo que leia 10 números inteiros e informe:
# • Quantos são positivos;
# • Quantos são negativos;
# • Quantos são pares;
# • Quantos são ímpares.
# Pergunta:
# Qual estrutura de repetição seria mais adequada: for, while ou do...while?


def readInt(msg: str = ""):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido e tente novamente.")


def main():
    pos = 0
    neg = 0
    odd = 0
    even = 0

    # A estrutura 'for' é mais apropriada, pois a quantidade de iterações é conhecida em compile-time
    # e não depende de uma condição de dentro do loop
    for i in range(10):
        n = readInt(f"Digite o {i + 1}º número: ")

        if n < 0:
            neg += 1
        elif n > 0:
            pos += 1

        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Positivos:", pos)
    print("Negativos:", neg)
    print("Pares:", even)
    print("Ímpares:", odd)


if __name__ == "__main__":
    main()

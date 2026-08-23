# Exercício 4: Vetores
# Problema:
# Crie um vetor capaz de armazenar 10 números inteiros.
# O algoritmo deverá:
# 1. Ler os 10 valores;
# 2. Exibir os valores armazenados;
# 3. Calcular a soma;
# 4. Calcular a média;
# 5. Identificar o maior valor;
# 6. Identificar o menor valor.
# Desafio:
# Informar também a posição do maior elemento.


def avg(vetor: list[int]):
    return sum(vetor) / len(vetor)


def max_i(vetor: list[int]):
    return vetor.index(max(vetor))


def readInt(msg: str = ""):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido e tente novamente.")


def main():
    vetor = [readInt(f"Digite o {i + 1}º número: ") for i in range(10)]
    print("Armazenados:", vetor)
    print("Soma:", sum(vetor))
    print("Média:", avg(vetor))
    print("Menor:", min(vetor))
    print("Maior:", max(vetor))
    print("Índice do maior:", max_i(vetor))


if __name__ == "__main__":
    main()

# Exercício 5: Busca em vetor
# Problema:
# Dado um vetor com 15 números inteiros, solicite ao usuário um número para
# pesquisa.
# O algoritmo deverá informar:
# • Se o número foi encontrado;
# • Em qual posição ele está;
# • Quantas vezes aparece no vetor.
# Conceito trabalhado:
# Busca sequencial (linear).


def readInt(msg: str = ""):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido e tente novamente.")


def main():
    vetor = [91, 91, 57, 81, -85, -2, -19, -35, 39, -74]
    query = readInt("Digite um número para pesquisa: ")

    posicoes: list[int] = []
    contagem = 0

    for i, n in enumerate(vetor):
        if query == n:
            contagem += 1
            posicoes.append(i)

    if contagem > 0:
        print("Número encontrado")
        print("Quantidade:", contagem)
        print("Posições:", ", ".join(str(i) for i in posicoes))
    else:
        print("Não encontrado.")


if __name__ == "__main__":
    main()

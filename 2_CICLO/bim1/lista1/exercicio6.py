# Exercício 6: Ordenação
# Problema:
# Crie um vetor com 10 números inteiros e desenvolva um algoritmo para ordenar os
# elementos em ordem crescente.
# Desafio:
# Implemente o algoritmo utilizando o método:
# Bubble Sort
# Depois, apresente o vetor:
# • Antes da ordenação;
# • Após cada passagem;
# • Ao final da ordenação.


def main():
    vetor: list[int] = [50, 78, 35, 39, 82, 69, 32, 85, -2, 82]

    print("Antes da ordenação:", vetor)
    # Insertion sort seria bem mais eficiente e não tão dificil assim de implementar
    # Mas enunciado é enunciado.
    for i in range(len(vetor)):
        for j in range(len(vetor) - i - 1):
            if vetor[j] > vetor[j + 1]:
                (vetor[j], vetor[j + 1]) = (vetor[j + 1], vetor[j])
                # Equivalente:
                # c = vetor[j]
                # vetor[j] = vetor[j + 1]
                # vetor[j + 1] = c
        print(f"Etapa {i}:", vetor)
    print("Ao final da ordenação:", vetor)


if __name__ == "__main__":
    main()

# 1. Solicitar as 10 notas.
# 2. Armazená-las na lista.
# 3. Calcular a média.
# 4. Exibir a média.
# 5. Informar quantos alunos foram aprovados.


def readFloat(msg: str = ""):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Digite um número válido e tente novamente.")


def main():
    QTDE_NOTAS = 10

    nums: list[float] = []
    failCount: int = 0

    for i in range(QTDE_NOTAS):
        nums.append(readFloat(f"Digite a {i + 1}ª nota: "))
        if nums[i] < 6:
            failCount += 1

    media = sum(nums) / QTDE_NOTAS

    print("Média:", media)
    print("Reprovados:", failCount)
    print("Aprovados:", QTDE_NOTAS - failCount)


if __name__ == "__main__":
    main()

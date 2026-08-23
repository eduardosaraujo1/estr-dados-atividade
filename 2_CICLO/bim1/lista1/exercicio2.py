# Exercício 2: Estruturas condicionais
# Problema:
# Leia a nota de um aluno e determine sua situação:
# • Nota ≥ 7 → Aprovado
# • Nota entre 5 e 6,9 → Recuperação
# • Nota < 5 → Reprovado
# Desafio:
# Validar se a nota informada está entre 0 e 10.


def readFloat(msg: str = ""):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Digite um número válido e tente novamente.")


def lerNota():
    while True:
        n = readFloat("Digite a nota do aluno: ")
        if 0 <= n <= 10:
            return n
        else:
            print("A nota deve ser entre 0 e 10. Tente novamente.")


def main():
    nota = lerNota()

    if nota < 5:
        print("Reprovado")
    elif nota < 7:
        print("Recuperação")
    else:
        print("Aprovado")


if __name__ == "__main__":
    main()

def readInt(msg: str = ""):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido e tente novamente.")


def main():
    items = [10, 20, 30, 40, 50]

    num = readInt("Digite o número que deseja remover: ")

    if num in items:
        items.remove(num)
        print("Resultado:", items)
    else:
        print("Não encontrado.")


if __name__ == "__main__":
    main()

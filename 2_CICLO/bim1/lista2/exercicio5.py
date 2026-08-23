# Desenvolva um pequeno sistema para controlar produtos de uma loja.
# Crie: ArrayList<String> produtos
# Menu:
# ===== MENU =====
# 1 - Adicionar produto
# 2 - Listar produtos
# 3 - Pesquisar produto
# 4 - Remover produto
# 5 - Sair
#
# Requisitos:
# Opção 1: Adicionar um produto.
# Opção 2: Mostrar todos os produtos.
# Opção 3: Pesquisar um produto pelo nome.
# Opção 4: Remover um produto.
# Opção 5: Encerrar o programa.
# Desafio: Utilize um while para manter o menu funcionando até o usuário escolher Sair.
import sys


def readInt(msg: str = ""):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido e tente novamente.")


def readFloat(msg: str = ""):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Digite um número válido e tente novamente.")


def clear():
    # os.system("clear")
    _ = sys.stdout.write("\033[H\033[2J")
    _ = sys.stdout.flush()


def pause(msg: str = "[OK]"):
    _ = input(msg)


def addProduct(products: list[str]):
    products.append(input("Digite o nome do produto a adicionar: "))
    print("Produto adicionado com sucesso.")


def removeProduct(products: list[str]):
    max_index = len(products) - 1

    if max_index <= -1:
        print("Não há nenhum produto para remover.")
        return

    choice = -1
    while True:
        try:
            choice = readInt(
                "Digite o índice do produto a remover (Ctrl+C para cancelar): "
            )
            if choice < 0 or choice > max_index:
                print("Produto inexistente. Tente novamente.")
                continue
            break
        except KeyboardInterrupt:
            print("\nOperação cancelada.")
            return

    _ = products.pop(choice)
    print("Produto removido com sucesso.")


def showProducts(products: list[str]):
    if len(products) <= 0:
        print("Nenhum produto cadastrado.")
    else:
        print("Produtos:")
        print("\n".join([f"({i}) {p}" for i, p in enumerate(products)]))


def searchProduct(products: list[str]):
    key = input("Digite o nome do produto: ")
    try:
        print("Posição: ", products.index(key))
    except ValueError:
        print("Produto não cadastrado.")


def showUI() -> int:
    MIN_NUM = 1
    MAX_NUM = 5

    print(
        """# ===== MENU =====
1 - Adicionar produto
2 - Listar produtos
3 - Pesquisar produto
4 - Remover produto
5 - Sair
  > """,
        end="",
    )

    return min(MAX_NUM, max(MIN_NUM, readInt()))


def main():
    products: list[str] = []

    while True:
        clear()
        opt = showUI()

        try:
            match opt:
                case 1:
                    clear()
                    addProduct(products)
                    pause()
                case 2:
                    clear()
                    showProducts(products)
                    pause()
                case 3:
                    clear()
                    searchProduct(products)
                    pause()
                case 4:
                    clear()
                    removeProduct(products)
                    pause()
                case 5:
                    sys.exit()
                case _:
                    pass
        except KeyboardInterrupt:
            continue


if __name__ == "__main__":
    main()

# Adicionado pelo meu linter: resolve os type-hints após o processamento do código
from __future__ import annotations


class Node:
    def __init__(self, value: int, next: Node | None = None):
        self.__value: int = value
        self.__next: Node | None = next

    def value(self) -> int:
        return self.__value

    def next(self) -> Node | None:
        return self.__next

    def setNext(self, next: Node | None) -> None:
        self.__next = next


def readInt(msg: str = ""):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido e tente novamente.")


def generateLinkedList(arr: list[int]) -> Node | None:
    if len(arr) <= 0:
        return None

    head = Node(arr[0])
    tail = head

    for num in arr[1:]:
        node = Node(num)
        tail.setNext(node)
        tail = node

    return head


# Efetua busca linear na lista encadeada
# Retorna a posição do elemento encontrado (zero incluso), ou -1 se não for encontrado.
def busca(search: int, listHead: Node) -> int:
    atual: Node | None = listHead
    pos = 0

    while atual is not None:
        if atual.value() == search:
            return pos
        atual = atual.next()
        pos += 1

    return -1


def main():
    listHead = generateLinkedList([10, 25, 30, 45, 60])

    if listHead is None:
        print("Erro: lista interna está vazia. Peça ao administrador para preenche-la")
        return

    pesquisa = readInt("Digite um número para pesquisa: ")
    resultado = busca(pesquisa, listHead)

    if resultado < 0:
        print("Número não encontrado!")
    else:
        print(f"Número encontrado no índice {resultado}!")


if __name__ == "__main__":
    main()

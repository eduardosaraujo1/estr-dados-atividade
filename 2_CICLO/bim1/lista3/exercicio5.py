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


def exibirCadeia(node: Node | None):
    # exemplo de saida: 1 → 2 → 3 → NULL
    while node is not None:
        print(node.value(), "→", end=" ")
        node = node.next()
    print("NULL")


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


# Retorna a raíz da lista e se a operação encontrou um elemento para remover ou não
def remover(elemento: int, listHead: Node) -> tuple[Node | None, bool]:
    # Caso especial: primeiro elemento deve ser removido
    if listHead.value() == elemento:
        return (listHead.next(), True)

    previous: Node = listHead
    current: Node | None = listHead.next()

    while current is not None:
        # Estados possíveis: current pode ser o último elemento da lista, ou pode ser um elemento no meio
        if current.value() == elemento:
            previous.setNext(current.next())
            return (listHead, True)
        previous = current
        current = current.next()

    return (listHead, False)


def main():
    listHead = generateLinkedList([10, 20, 30, 40, 50])

    if listHead is None:
        print("Erro: lista interna está vazia. Peça ao administrador para preenche-la")
        return

    numero = readInt("Digite o número que deve ser removido: ")

    listHead, encontrado = remover(numero, listHead)
    if not encontrado:
        print("Elemento não encontrado.")
    else:
        print("Resultado:")
        exibirCadeia(listHead)


if __name__ == "__main__":
    main()

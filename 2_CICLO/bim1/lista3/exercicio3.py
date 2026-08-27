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


def getListTail(head: Node):
    atual = head
    proximo = head.next()

    while proximo is not None:
        atual = proximo
        proximo = atual.next()

    return atual


def inserirFinal(node: Node, listHead: Node) -> None:
    tail = getListTail(listHead)
    tail.setNext(node)


def main():
    N = readInt("Digite a quantidade de números a serem inseridos: ")
    root = None

    for i in range(N):
        numero = readInt(f"Digite o {i + 1}º número: ")
        if root is None:
            root = Node(numero)
        else:
            inserirFinal(Node(numero), root)

    exibirCadeia(root)


if __name__ == "__main__":
    main()

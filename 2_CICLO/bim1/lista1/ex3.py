def main():
    produtos: list[str] = [
        "Teclado",
        "Mouse",
        "Monitor",
        "Notebook",
        "Impressora"
    ]
    estoque: list[int] = [
        10,
        25,
        5,
        8,
        3
    ]

    itens = list(zip(produtos, estoque))

    print("Menor estoque:",min(itens, key=lambda i : i[1])[0])
    for p, e in itens:
        print(f"{p}: {e}x")

    print("Produtos com menos de 10 unidades:")
    for p, e in itens:
        if e < 10:
            print(f"{p}: {e}x")

if __name__ == '__main__':
    main()

import math

def readInt(msg: str = ""):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido e tente novamente.")

def main():
    nums = []
    qtdePar = 0
    qtdeImpar = 0
    maior = -math.inf
    menor = math.inf
    soma = 0
    count = 0
    for i in range(10):
        n = 0
        while True:
            n = readInt(f"Digite o {i+1}º número: ")
            if n in nums:
                print("Não é permitido números repetidos.")
                continue
            break

        count += 1
        soma += n

        if i % 2 == 0:
            qtdePar += 1
        else:
            qtdeImpar += 1

        maior = max(maior, n)
        menor = min(menor, n)

        nums.append(n)

    search = readInt("Digite o número a ser pesquisado: ")
    print(f"Quantidade par: {qtdePar}")
    print(f"Quantidade impar: {qtdeImpar}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
    print(f"Soma: {soma}")
    print(f"Média: {soma/count}")
    print(f"Posição do número pesquisado: ",end="")
    if search in nums:
        print(nums.index(search))
    else:
        print("Não encontrado")

if __name__ == '__main__':
    main()

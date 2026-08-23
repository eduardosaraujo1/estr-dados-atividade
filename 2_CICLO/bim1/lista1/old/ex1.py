def readInt(msg: str = ""):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido e tente novamente.")
def main():
    vetor = [readInt(f"Digite a {i+1}ª nota: ") for i in range(10)]
    print("Notas:\n",'\n'.join(str(n) for n in vetor))
    print("Média:",sum(vetor)/len(vetor))
    print("Maior:",max(vetor))
    print("Menor:",min(vetor))

if __name__ == '__main__':
    main()

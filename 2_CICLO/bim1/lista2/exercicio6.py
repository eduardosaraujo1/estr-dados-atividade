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


class Aluno:
    def __init__(self, nome: str, idade: int, nota: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__nota: float = nota

    def nome(self) -> str:
        return self.__nome

    def idade(self) -> int:
        return self.__idade

    def nota(self) -> float:
        return self.__nota

    def __str__(self) -> str:
        return f"Nome: {self.nome()} | Idade: {self.idade()} | Nota: {self.nota():.2f}"


def showUI():
    MIN_NUM = 1
    MAX_NUM = 7
    print(
        """Menu:
1 - Cadastrar aluno
2 - Listar alunos
3 - Pesquisar aluno
4 - Remover aluno
5 - Calcular média da turma
6 - Mostrar alunos aprovados
7 – Sair
""",
        end="",
    )

    return min(MAX_NUM, max(MIN_NUM, readInt("  >")))


def cadastrarAluno(aluno: list[Aluno]):
    nome = input("Digite o nome: ")
    idade = readInt("Digite a idade: ")
    nota = readFloat("Digite a nota: ")

    aluno.append(Aluno(nome, idade, nota))
    print("Aluno cadastrado com sucesso.")


def listarAlunos(aluno: list[Aluno]):
    if len(aluno) <= 0:
        print("Nenhum aluno cadastrado.")
        return

    print("Lista de Alunos")
    for i, a in enumerate(aluno):
        print(f"({i}) {a}")


def pesquisarAluno(aluno: list[Aluno]):
    if len(aluno) <= 0:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o inicio do nome a pesquisar: ")
    for a in aluno:
        if a.nome().startswith(nome):
            print("Encontrado:", a)


def removerAluno(aluno: list[Aluno]):
    index = -1

    if len(aluno) <= 0:
        print("Nenhum aluno cadastrado.")
        return

    while True:
        index = readInt("Digite o índice do aluno a remover (Ctrl+C para cancelar): ")
        if index < 0 or index >= len(aluno):
            print("Índice inválido. Tente novamente.")
            continue
        break

    removido = aluno.pop(index)
    print(f"Aluno '{removido.nome()}' removido com sucesso.")


def mostrarMedia(aluno: list[Aluno]):
    soma = 0

    if len(aluno) <= 0:
        print("Nenhum aluno cadastrado.")
        return

    for a in aluno:
        soma += a.nota()
    print("Média:", soma / len(aluno))


def mostrarAprovados(aluno: list[Aluno]):
    if len(aluno) <= 0:
        print("Nenhum aluno cadastrado.")
        return

    print("Aprovados:")
    for a in aluno:
        if a.nota() >= 6.0:
            print(a)


def main():
    alunos: list[Aluno] = []

    while True:
        clear()
        selection: int = showUI()

        try:
            match selection:
                case 1:
                    clear()
                    cadastrarAluno(alunos)
                    pause()
                case 2:
                    clear()
                    listarAlunos(alunos)
                    pause()
                case 3:
                    clear()
                    pesquisarAluno(alunos)
                    pause()
                case 4:
                    clear()
                    removerAluno(alunos)
                    pause()
                case 5:
                    clear()
                    mostrarMedia(alunos)
                    pause()
                case 6:
                    clear()
                    mostrarAprovados(alunos)
                    pause()
                case 7:
                    sys.exit()
                case _:
                    continue
        except KeyboardInterrupt:
            continue


if __name__ == "__main__":
    main()

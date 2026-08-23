alunos = [
    "Ana",
    "Bruno",
    "Carlos",
    "Daniel",
    "Eduardo"
];

nome = input("Digite o nome: ")
if nome in alunos:
    print(f"Aluno encontrado na posição {alunos.index(nome)}!")
else:
    print("Aluno não encontrado!")


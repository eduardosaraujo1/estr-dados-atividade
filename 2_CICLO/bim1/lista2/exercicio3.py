items = [10,20,30,40,50]

num = int(input("Digite o número que deseja remover: "))

if (num in items):
    items.remove(num)
    print("Resultado:",items)
else:
    print("Não encontrado.")


# 1. Solicitar as 10 notas.
# 2. Armazená-las na lista.
# 3. Calcular a média.
# 4. Exibir a média.
# 5. Informar quantos alunos foram aprovados.

def readFloat():
    return float(input())

nums: list(float) = []
failCount = 0

for i in range(10):
    print(f"Digite a {i+1}ª nota:", end=" ")
    nums.append(readFloat())
    if nums[i] < 6:
        failCount += 1

media = sum(nums)/len(nums)

print("Média:",media)
print("Reprovados:",failCount)
print("Aprovados:",len(nums) - failCount)

sistema = []
aluno = {}
nota = {}

for c in range(0, 1):
    aluno["nome"] = input("Nome do Alunos: ")
    nota["nota"] = float(input("Nota deste aluno: "))
    sistema.append(aluno.copy())
    sistema.append(nota.copy())  

print(f"Nome do Aluno: {aluno}")
print(f"A nota do Aluno: {nota}")

if nota["nota"] >= 7:
        print("APROVADO")
elif 4 <= nota["nota"] < 7:
        print("recuperacao")
else:
        print("reprovado")




# 1. Receber a nota do aluno.

nota = float(input())

# 2. Fazer a operação e já mostrar o resultado para o aluno.
if nota >= 7:
    print("Aprovado: ") 
elif nota >= 5 and nota < 7:
    print("Recuperação: ")
else:
    print("Reprovado: ")
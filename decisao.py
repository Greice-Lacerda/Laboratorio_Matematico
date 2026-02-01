# Decisão em Python: Fluxograma para aprovação de alunos

# 1. Entrada: O programa 'ouve' o aluno e converte o texto para número
nota = float(input("\nDigite a nota do aluno: "))

# 2. Decisão: O Python segue as setas do nosso fluxograma
if nota >= 6.0:
    print("\nResultado: Aprovado!")
elif nota >= 4.0:
    print("Resultado: Recuperação.")
else:
    print("\nResultado: Reprovado.")
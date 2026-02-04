# Programa para calcular a média das notas de uma turma e classificar cada aluno
print("\nCálculo da Média da Turma e Classificação dos Alunos\n")

# 1. Inicialização das variáveis
total_alunos = 5  # Vamos testar com 5 para ser rápido
soma = 0
notas_azuis = 0

# 2. Loop para entrada das notas e classificação
for i in range(1, total_alunos + 1):
    nota = float(input(f"Digite a nota do {i}º aluno: "))
    soma += nota # O mesmo que: soma = soma + nota
    
    # 1. Classificação individual (Lógica do nosso Fluxograma)
    if nota >= 6.0:
        print("-> Status: APROVADO ✅")
        notas_azuis += 1  # "Clica" o contador de notas azuis
    elif nota >= 4.0:
        print("-> Status: RECUPERAÇÃO ⚠️")
    else:
        print("-> Status: REPROVADO ❌")
    print("-" * 50)

# 2. Resultados Finais
media_turma = soma / total_alunos
print(f"\n--- RELATÓRIO FINAL ---")
print(f"Média Geral da Turma: {media_turma:.2f}")
print(f"Total de alunos com nota Azul (>= 6.0): {notas_azuis}")
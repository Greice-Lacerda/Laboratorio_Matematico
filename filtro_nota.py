# Programa que solicita uma nota de simulado e valida a entrada

# Solicita a nota do usuário
nota = float(input("\nDigite a nota do simulado (0 a 10): "))

# ENQUANTO a nota for inválida, o programa insiste
while nota < 0 or nota > 10:
    print("⚠️ Erro! A nota deve estar entre 0 e 10.\n")
    nota = float(input("Por favor, digite uma nota válida: "))

# Nota válida registrada
print(f"Sucesso! Nota {nota} registrada no sistema.")
# Decisão em Python: Verificação de número par e positivo

# 1. Entrada de dados
numero = int(input("\nDigite um número inteiro para análise: "))

print(f"\n--- Analisando o número {numero} ---")

# 2. Primeira Análise: Par ou Ímpar?
# Usamos o operador de resto (%) da divisão por 2
if numero % 2 == 0:
    print("- Ele é um número PAR.")
else:
    print("- Ele é um número ÍMPAR.")

# 3. Segunda Análise: Positivo, Negativo ou Zero?
if numero > 0:
    print("- Ele é POSITIVO.\n")
elif numero < 0:
    print("- Ele é NEGATIVO.\n")
else:
    print("- Ele é o elemento neutro (ZERO).\n")

# 4. Terceira Análise: Condição Composta (Uso do 'and')
if numero > 0 and numero % 2 == 0:
    print("- Curiosidade: Este é um número par e positivo!\n")
#Exemplo de código para média aritmética de 10 numeros

# 1. Definimos o total de notas e uma variável para acumular a soma
total_notas = 10
soma = 0
print("\nCálculo da Média Aritmética de 10 Notas\n")
# 2. O 'for' executa o bloco abaixo 10 vezes automaticamente
for i in range(1, total_notas + 1):
    valor = float(input(f"Digite a {i}ª nota: "))
    soma = soma + valor  # O acumulador recebe a nota atual

# 3. Cálculo da média (fora do loop, pois só precisamos calcular UMA vez)
media = soma / total_notas

print(f"\nA média aritmética das {total_notas} notas é: {media:.2f}")
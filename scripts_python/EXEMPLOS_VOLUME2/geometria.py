#Simulação para calcular o perimetro e a área de um circulo

# 1. Entrada de dados: O input recebe o texto, e o float() converte para número
raio = float(input("\nDigite o valor do raio do círculo: "))

# 2. Processamento: Aplicando as fórmulas matemáticas
pi = 3.14159
perimetro = 2 * pi * raio
area = pi * (raio ** 2)

# 3. Saída de dados: Exibindo os resultados de forma elegante
print(f"\n--- Resultados para o Raio {raio} ---")
print(f"\nO Perímetro é: {perimetro:.2f}")
print(f"\nA Área é: {area:.2f}")
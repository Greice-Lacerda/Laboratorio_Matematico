import math

# Definindo a ferramenta (Função)
def calcular_area(raio):
    area = math.pi * (raio ** 2)
    return area  # O 'return' é o resultado que a função nos devolve

# Usando a ferramenta (Chamada da Função)
raio = float(input("\nDigite o raio do círculo: "))
resultado = calcular_area(raio)
print(f"\nA área calculada é: {resultado:.2f}")
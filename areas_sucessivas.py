# Laboratório de Geometria: Cálculo de Perímetro e áreas de Círculo

import math # Importa a biblioteca matemática para usar o valor de pi

print("\n--- Bem-vindo ao Laboratório de Geometria ---\n")
print("Digite o raio para calcular o perímetro e a área. Para encerrar, digite -1.")

# Inicializamos a variável com um valor que permite entrar no loop
raio = 0
area = 0

while raio >= 0:
    raio = float(input("\nInforme o valor do raio: "))
    
    if raio >= 0:
        area = math.pi * raio ** 2
        print(f"✅ A área para o raio {raio} é: {area:.2f}")
        perimetro = 2 * math.pi * raio
        print(f"✅ O perímetro para o raio {raio} é: {perimetro:.2f}")
    else:
        print("🛑 Valor negativo detectado. Encerrando o simulador...")

print("\nPrograma finalizado. Até a próxima aula!")
# Arquivo: main.py

# Aqui você importa o SEU arquivo externo: o geometria1.py!
import geometria1

# Aqui você solicita ao usuário o valor do raio
raio_usuario = float(input("\nDigite o raio para os cálculos: "))

# Para chamar e usar as funções do arquvo geometria1, você escreve: nome_do_arquivo.nome_da_funcao
perimetro = geometria1.calcular_perimetro(raio_usuario)
area = geometria1.calcular_area(raio_usuario)
volume = geometria1.calcular_volume_esfera(raio_usuario)

# Exibindo os resultados
print(f"\nÁrea: {area:.5f}")
print(f"\nPerímetro: {perimetro:.5f}")
print(f"\nVolume da Esfera: {volume:.5f}")
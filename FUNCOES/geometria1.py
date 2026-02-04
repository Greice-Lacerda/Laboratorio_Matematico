# Arquivo: geometria1.py

# Funções para cálculos geométricos relacionados a círculos e esferas
import math

# Função para o cálculo da área do círculo
def calcular_area(raio):
    return math.pi * (raio ** 2)

# Função para o cálculo do perímetro do círculo
def calcular_perimetro(raio):
    return 2 * math.pi * raio

# FUnção para o cálculo do volume da esfera
def calcular_volume_esfera(raio):
    return (4/3) * math.pi * (raio ** 3)
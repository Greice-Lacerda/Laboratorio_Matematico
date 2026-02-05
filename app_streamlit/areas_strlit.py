import streamlit as st
import math

# Importamos suas funções do arquivo que você já criou
from funcoes_strlit import calcular_area, calcular_perimetro, calcular_volume_esfera

# --- CONFIGURAÇÃO DA PÁGINA ---
st.title("🧪 Laboratório de Geometria Espacial")

st.markdown("""
Bem-vindo ao simulador interativo! Aqui, exploramos como a variação do **raio ($r$)** impacta as propriedades de círculos e esferas.
""")

# --- ENTRADA DE DADOS ---
# No Streamlit, o componente de entrada substitui o input() do terminal.
raio = st.number_input("Informe o valor do raio (cm):", min_value=0.0, value=1.0, step=0.1)

# --- PROCESSAMENTO E VISUALIZAÇÃO ---
# Chamamos suas funções externas para processar o valor do raio
area = calcular_area(raio)
perimetro = calcular_perimetro(raio)
volume = calcular_volume_esfera(raio)

st.divider()
st.subheader("Resultados da Investigação")

# Organizando em colunas para uma leitura mais científica
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Área do Círculo", value=f"{area:.2f} cm²")

with col2:
    st.metric(label="Perímetro", value=f"{perimetro:.2f} cm")

with col3:
    st.metric(label="Volume da Esfera", value=f"{volume:.2f} cm³")

# --- FEEDBACK PEDAGÓGICO ---
st.info(f"Curiosidade: Para um raio de {raio}, o volume da esfera é aproximadamente {math.ceil(volume/area) if area > 0 else 0} vezes a área do círculo!")

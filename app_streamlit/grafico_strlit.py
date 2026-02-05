# grafico_strlit.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from funcoes_strlit import calcular_area

st.header("📈 Investigação Gráfica: O Crescimento da Área")

# 1. Entrada de dados para o limite da investigação
raio_max = st.slider("Selecione o raio máximo para o gráfico:", 1.0, 50.0, 10.0)

# 2. Criando dados para o gráfico
# Criamos uma lista de raios de 0 até o valor escolhido no slider
raios = np.linspace(0, raio_max, 100)
areas = [calcular_area(r) for r in raios]

# Criamos um DataFrame (uma tabela inteligente do Pandas)
dados = pd.DataFrame({
    "Raio (cm)": raios,
    "Área (cm²)": areas
})

# 3. Criando o gráfico interativo com Plotly
fig = px.line(dados, x="Raio (cm)", y="Área (cm²)", 
             title=f"Relação Raio x Área (Até {raio_max} cm)")

# 4. Exibindo no Streamlit
st.plotly_chart(fig, use_container_width=True)

st.info("💡 Passe o mouse sobre a linha para ver os valores exatos em cada ponto!")

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.header("🌊 Simulador de Funções Senoidais")
st.write("Ajuste os parâmetros abaixo para ver a onda se transformar em tempo real.")

# 1. Controles na Barra Lateral (Os Coeficientes)
with st.sidebar:
    st.subheader("Parâmetros da Equação")
    A = st.slider("Amplitude (A) - Altura da onda", 0.1, 5.0, 1.0)
    B = st.slider("Frequência (B) - Velocidade da oscilação", 0.1, 10.0, 1.0)
    C = st.slider("Fase (C) - Deslocamento horizontal", 0.0, 2*np.pi, 0.0)
    D = st.slider("Deslocamento Vertical (D)", -5.0, 5.0, 0.0)

# 2. Gerando os dados matemáticos
x = np.linspace(0, 10, 500)
# A equação fundamental:
y = A * np.sin(B * x + C) + D

df_onda = pd.DataFrame({'x': x, 'y': y})

# 3. Visualização Interativa
fig = px.line(df_onda, x='x', y='y', title=f"Gráfico: y = {A}.sin({B}x + {C}) + {D}")
fig.update_yaxes(range=[-10, 10]) # Fixamos o eixo Y para o aluno notar o deslocamento
st.plotly_chart(fig, use_container_width=True)

# 4. Explicação Didática Dinâmica
st.info(f"""
**Análise Matemática:**
* A onda atinge um pico de **{A+D:.2f}** e um vale de **{-A+D:.2f}**.
* O coeficiente **B** está fazendo a onda oscilar **{B}** vezes mais rápido que a função básica.
""")
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("🧊 Explorador de Sólidos Geométricos 3D")

# Barra lateral para escolha do sólido
solido = st.sidebar.selectbox(
    "Selecione o sólido para investigar:",
    ["Esfera", "Cone", "Paraboloide"]
)

# Ajuste de resolução (densidade da malha)
res = st.sidebar.slider("Resolução da malha:", 10, 50, 30)
# 1. Gerando as coordenadas matematicas
u = np.linspace(0, 2 * np.pi, res)
v = np.linspace(0, np.pi, res)

if solido == "Esfera":
    raio = st.slider("Raio (r):", 1, 10, 5)
    # Equações paramétricas da esfera
    x = raio * np.outer(np.cos(u), np.sin(v))
    y = raio * np.outer(np.sin(u), np.sin(v))
    z = raio * np.outer(np.ones(np.size(u)), np.cos(v))
    titulo = f"Esfera de Raio {raio}"

elif solido == "Cone":
    raio = st.slider("Raio da base:", 1, 10, 5)
    altura = st.slider("Altura (h):", 1, 10, 5)
    # Equações paramétricas do cone
    r_cone = np.linspace(0, raio, res)
    theta = np.linspace(0, 2 * np.pi, res)
    R, Theta = np.meshgrid(r_cone, theta)
    x = R * np.cos(Theta)
    y = R * np.sin(Theta)
    z = (altura / raio) * R
    titulo = f"Cone com Altura {altura}"

elif solido == "Paraboloide":
    a = st.slider("Abertura (a):", 1, 5, 2)
    x_range = np.linspace(-5, 5, res)
    y_range = np.linspace(-5, 5, res)
    X, Y = np.meshgrid(x_range, y_range)
    z = a * (X**2 + Y**2)
    x, y = X, Y
    titulo = f"Paraboloide de Revolução com Abertura {a}"

# 2. Criando o gráfico 3D com Plotly
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Viridis')])

fig.update_layout(
    title=titulo,
    scene=dict(
        xaxis_title='Eixo X',
        yaxis_title='Eixo Y',
        zaxis_title='Eixo Z'
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

# 3. Exibição
st.plotly_chart(fig, use_container_width=True)

st.info("🖱️ Use o mouse para girar o sólido e o scroll para dar zoom!")

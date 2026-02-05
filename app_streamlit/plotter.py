import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import math

# 1. Título e Introdução
st.title("📈 Investigador de Funções Matemáticas")
st.markdown("""
Neste módulo, você pode digitar qualquer função em termos de **x** e observar seu comportamento.
Use a sintaxe do Python:
* `x**2` para $x^2$
* `np.sin(x)` para $\text{sen}(x)$
* `np.exp(x)` para $e^x$
""")

# 2. Barra Lateral para Configurações (Organization Visual)
st.sidebar.header("Configurações do Gráfico")

# O aluno escolhe o intervalo de visualização (Eixo X)
intervalo = st.sidebar.slider(
    "Intervalo de x:",
    min_value=-100.0, max_value=100.0, value=(-10.0, 10.0)
)

# O aluno escolhe a "resolução" do gráfico
pontos = st.sidebar.select_slider(
    "Quantidade de pontos (Precisão):",
    options=[10, 50, 100, 500, 1000], value=100
)

# 3. Entrada da Função
funcao_texto = st.text_input("Digite a função f(x):", value="x**2")

# 4. Processamento Matemático (O Coração do Script)
try:
    # Criamos o array de X usando o intervalo do slider
    x = np.linspace(intervalo[0], intervalo[1], pontos)
    
    # O 'eval' interpreta o texto da função usando o X do numpy
    # Passamos o np para o eval para que o aluno possa usar np.sin, np.cos, etc.
    y = eval(funcao_texto, {"x": x, "np": np, "math": math})

    # Criamos o DataFrame para o Plotly
    df = pd.DataFrame({"x": x, "f(x)": y})

    # 5. Visualização Gráfica
    fig = px.line(df, x="x", y="f(x)", title=f"Gráfico de f(x) = {funcao_texto}")
    
    # Melhorando o visual do gráfico
    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)

    # 6. Exibição de Dados (Tabelas e Dataframes)
    if st.checkbox("Mostrar tabela de valores (X e Y)"):
        st.dataframe(df)

except Exception as e:
    st.error(f"Erro na equação: {e}")
    st.info("Dica: Certifique-se de usar `*` para multiplicação. Ex: `2*x` em vez de `2x`.")
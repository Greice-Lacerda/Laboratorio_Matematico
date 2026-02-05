import streamlit as st
import pandas as pd

st.title("📂 Importador de Planilhas Educacionais")

st.markdown("""
Suba sua planilha do Excel para gerar análises automáticas. 
*Certifique-se de que a planilha possui colunas como 'Nome', 'Nota' ou 'Frequência'.*
""")

# 1. Componente de Upload
# O 'type' restringe o usuário a selecionar apenas arquivos Excel
arquivo_excel = st.file_uploader("Selecione o arquivo Excel (.xlsx)", type=["xlsx"])

if arquivo_excel is not None:
    try:
        # 2. Lendo a planilha com Pandas
        # O Streamlit passa o arquivo diretamente para o Pandas
        df = pd.read_excel(arquivo_excel)

        # 3. Visualização Prévia
        st.subheader("Visualização dos Dados Importados")
        st.dataframe(df, use_container_width=True)

        # 4. Análise Dinâmica: O Professor escolhe a coluna de análise
        st.divider()
        colunas = df.columns.tolist()
        coluna_alvo = st.selectbox("Selecione a coluna que deseja analisar (ex: Notas):", colunas)

        if pd.api.types.is_numeric_dtype(df[coluna_alvo]):
            # Métricas automáticas baseadas no arquivo importado
            m1, m2, m3 = st.columns(3)
            m1.metric("Média", f"{df[coluna_alvo].mean():.2f}")
            m2.metric("Mediana", f"{df[coluna_alvo].median():.2f}")
            m3.metric("Desvio Padrão", f"{df[coluna_alvo].std():.2f}")
            
            # Gerando um histograma rápido dos dados importados
            st.bar_chart(df[coluna_alvo])
        else:
            st.warning("A coluna selecionada não contém valores numéricos para cálculos.")

    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
else:
    st.info("Aguardando o upload de uma planilha para iniciar a análise...")
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração Inicial da Página
st.set_page_config(page_title="Gestão Escolar 4.0", layout="wide", page_icon="🎓")

# Estilização básica para o título
st.title("🎓 Laboratório de Análise de Dados Educacionais")
st.markdown("---")

# 2. Barra Lateral e Upload de Arquivo
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3413/3413535.png", width=100)
st.sidebar.header("Painel de Controle")
arquivo_excel = st.sidebar.file_uploader("Importar Planilha de Alunos (.xlsx)", type=["xlsx"])

# 3. Lógica Principal do Aplicativo
if arquivo_excel is not None:
    try:
        # Lendo o arquivo
        df = pd.read_excel(arquivo_excel)

        # Garantindo que a coluna 'Nota Final' existe (Cálculo automático se faltar)
        if 'Nota Final' not in df.columns:
            colunas_notas = [c for c in df.columns if 'Nota' in c]
            if colunas_notas:
                df['Nota Final'] = df[colunas_notas].mean(axis=1).round(1)
        
        # Criando coluna de Situação para análises
        df['Situação'] = df['Nota Final'].apply(lambda x: 'Aprovado' if x >= 6.0 else 'Recuperação')

        # 4. Criação das Abas
        tab_tabela, tab_analise = st.tabs(["📋 Planilha Estilizada", "📊 Central de Gráficos"])

        # --- ABA 1: TABELA E MÉTRICAS ---
        with tab_tabela:
            st.subheader("Visualização Detalhada da Turma")
            
            # Função para destacar notas baixas em vermelho
            def destacar_notas(valor):
                if isinstance(valor, (int, float)):
                    color = 'red' if valor < 6.0 else '#006400' # Verde escuro
                    return f'color: {color}; font-weight: bold'
                return None

            # Exibindo a tabela com estilo
            df_colorido = df.style.applymap(destacar_notas, subset=['Nota Final'])
            st.dataframe(df_colorido, use_container_width=True)

            # Painel de métricas rápidas
            st.markdown("### Resumo Pedagógico")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Média Geral", f"{df['Nota Final'].mean():.1f}")
            m2.metric("Total de Alunos", len(df))
            m3.metric("Aprovados", len(df[df['Situação'] == 'Aprovado']))
            m4.metric("Em Recuperação", len(df[df['Situação'] == 'Recuperação']), delta_color="inverse")

        # --- ABA 2: GRÁFICOS DINÂMICOS ---
        with tab_analise:
            st.subheader("Análise Visual de Desempenho")
            
            # Seletor de tipo de gráfico
            tipo_grafico = st.selectbox(
                "Escolha o tipo de visualização:",
                ["Proporção de Aprovação (Pizza)", 
                 "Distribuição de Notas (Histograma)", 
                 "Ranking de Notas (Barras)", 
                 "Frequência vs Nota (Dispersão)"]
            )

            st.divider()

            if tipo_grafico == "Proporção de Aprovação (Pizza)":
                fig = px.pie(df, names='Situação', title="Percentual de Aprovação",
                             color='Situação', color_discrete_map={'Aprovado':'#228B22', 'Recuperação':'#FF4B4B'},
                             hole=0.4)
                st.plotly_chart(fig, use_container_width=True)

            elif tipo_grafico == "Distribuição de Notas (Histograma)":
                fig = px.histogram(df, x="Nota Final", nbins=10, 
                                   title="Frequência de Notas na Turma",
                                   color_discrete_sequence=['#636EFA'],
                                   labels={'Nota Final': 'Faixa de Nota', 'count': 'Qtd de Alunos'})
                st.plotly_chart(fig, use_container_width=True)

            elif tipo_grafico == "Ranking de Notas (Barras)":
                df_sorted = df.sort_values(by="Nota Final", ascending=True)
                fig = px.bar(df_sorted, x="Nota Final", y="Nome do Aluno", orientation='h',
                             title="Ranking Individual (Crescente)",
                             color="Nota Final", color_continuous_scale="RdYlGn")
                st.plotly_chart(fig, use_container_width=True)

            elif tipo_grafico == "Frequência vs Nota (Dispersão)":
                if 'Frequência (%)' in df.columns:
                    fig = px.scatter(df, x="Frequência (%)", y="Nota Final", 
                                     size="Nota Final", hover_name="Nome do Aluno",
                                     title="Relação entre Frequência e Resultado Final",
                                     trendline="ols")
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Coluna 'Frequência (%)' não encontrada na planilha.")

    except Exception as e:
        st.error(f"Ocorreu um erro no processamento: {e}")

else:
    # Tela de boas-vindas caso nenhum arquivo tenha sido carregado
    st.info("💡 Bem-vindo! Para começar, suba o arquivo 'dados_alunos.xlsx' na barra lateral.")
    st.image("https://img.freepik.com/vetores-gratis/ilustracao-do-conceito-de-analise-de-dados_114360-1597.jpg", width=400)

# --- CONCLUSÃO ---
st.markdown("---")
st.caption("🚀 **Conclusão:** Este laboratório demonstra como a integração entre Pandas e Streamlit permite que o professor transforme dados brutos em decisões pedagógicas. Através do destaque visual de notas e da alternância entre diferentes tipos de gráficos, conseguimos identificar instantaneamente quais alunos precisam de atenção especial, tornando o processo de ensino muito mais ágil e baseado em evidências.")
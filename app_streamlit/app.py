import streamlit as st

# Título da aplicação
st.title("📊 Laboratório de Notas: O Despertar da Interface")

# Nossa "matriz de dicionários" do capítulo anterior
planilha_alunos = [
    {"nome": "Aluno A", "notas": [8.0, 7.0, 9.0]},          #Ficha do Aluno A
    {"nome": "Aluno B", "notas": [5.5, 6.0, 8.0]},          #Ficha do Aluno B
    {"nome": "Aluno C", "notas": [10.0, 9.5, 10.0]},      #Ficha do Aluno C
    {"nome": "Aluno D", "notas": [6.0, 7.5, 8.0]},          #Ficha do Aluno D
    {"nome": "Aluno E", "notas": [4.0, 7.0, 6.0]}           #Ficha do Aluno E
]

st.subheader("Visualização da Planilha")

# O comando "mágico" que transforma listas/dicionários em tabelas visuais
st.write("Aqui estão os dados brutos da nossa turma:")
st.table(planilha_alunos)

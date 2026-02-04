# Exemplo de manipulação de dicionários em Python

# Organização por "Fichas" (Dicionários)
planilha_alunos = [
    {"nome": "Aluno A", "notas": [8.0, 7.0, 9.0]},          #Ficha do Aluno A
    {"nome": "Aluno B", "notas": [5.5, 6.0, 4.0]},          #Ficha do Aluno B
    {"nome": "Aluno C", "notas": [10.0, 9.5, 10.0]},        #Ficha do Aluno C
    {"nome": "Aluno D", "notas": [6.0, 7.5, 8.0]},          #Ficha do Aluno D
    {"nome": "Aluno E", "notas": [4.0, 5.0, 6.0]}           #Ficha do Aluno E
]

# Função para calcular a média das notas
def calcular_media(notas):                                  # Define a função que recebe uma lista de notas
    return sum(notas) / len(notas)                          # Retorna a média das notas

# Processar cada ficha e exibir resultados
for ficha in planilha_alunos:                               # Itera sobre cada dicionário na lista
    nome = ficha["nome"]                                    # Acessa o valor associado à chave "nome"
    notas = ficha["notas"]                                  # Acessa o valor associado à chave "notas"
    media = calcular_media(notas)                           # Calcula a média das notas
    status = "Aprovado" if media >= 7.0 else "Reprovado"    # Determina o status com base na média
    
    print(f"Nome: {nome}")                                  # Exibe o nome do aluno
    print(f"Notas: {notas}")                                # Exibe as notas do aluno
    print(f"Média: {media:.2f}")                            # Exibe a média formatada com duas casas decimais
    print(f"Status: {status}")                              # Exibe o status do aluno
    print("-" * 30)                                         # Separador visual entre os alunos
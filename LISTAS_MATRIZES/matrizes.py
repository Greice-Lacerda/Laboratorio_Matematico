#Exemplo de manipulação de matrizes em Python usando listas aninhadas

# Cada linha representa um aluno, cada coluna uma nota
matriz_notas = [
    ["Aluno A", 8.0, 7.0, 9.0],     # Linha 0 (Aluno A)
    ["Aluno B", 5.5, 6.0, 4.0],     # Linha 1 (Aluno B)
    ["Aluno C", 10.0, 9.5, 10.0],   # Linha 2 (Aluno C)
    ["Aluno D", 6.0, 7.5, 8.0],     # Linha 3 (Aluno D)
    ["Aluno E", 4.0, 5.0, 6.0]      # Linha 4 (Aluno E)
]

#Imprimindo a matriz de notas
print("\n")
print("=" * 50)
print("Nota do Aluno C na segunda prova:", matriz_notas[2][2])
print("=" * 50)
print("\n\n")

print("=" * 50)
print("Alunos da  turma:")
print("=" * 50)

#Imprimindo a nota do Aluno D na terceira prova
for aluno in matriz_notas:
        print(f"{aluno[0]}")
print("=" * 50)
print("\n\n")

#Calculo da media das notas de cada aluno
def calcular_media(aluno):          #Definindo a função para calcular a média
    notas = aluno[1:]               # Exclui o nome do aluno
    return sum(notas) / len(notas)  # Calcula a média

#Imprimindo a média das notas de cada aluno
print("=" * 50)
print("Média das notas dos alunos:")
print("=" * 50)

#calculando e imprimindo a média de cada aluno
for aluno in matriz_notas:              #Itera sobre cada aluno na matriz
    media = calcular_media(aluno)       #Calcula a média usando a função definida
    print(f"{aluno[0]}: {media:.2f}")   #Imprime o nome do aluno e sua média formatada com 2 casas decimais

print("=" * 50)                         #Imprime uma linha de separação no final

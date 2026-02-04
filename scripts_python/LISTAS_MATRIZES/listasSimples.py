# Exemplo de uso listas simples em Python

# Exemplo 1: Criando a lista inicial

# Lista de presença dos alunos
alunos = ["Ana", "Bruno", "Carla"]

# Adicionando um novo aluno ao final da lista
alunos.append("Daniel")

# Exibindo a lista atualizada
print(f"\nLista de presença atualizada: {alunos[4]}")


##Exemplo 2: Processando Notas (Inteiros e Floats)

# Lista de notas dos alunos
notas = [5.5, 8.0, 4.0, 9.5, 6.0]

# Adicionando uma nova nota à lista
#print("Alunos com nota acima de 7:")
#for n in notas:    if n >= 7.0:        print(f"-> Nota {n}: Aprovado")

### Exemplo 3: Manipulando Strings

# Lista de trabalhos entregues pelos alunos
trabalhos_entregues = ["Maquete", "Relatório", "Cartaz", "Vídeo", "Apresentação", "Infográfico", "Podcast", "Blog", "E-book", "Webinar", "Infográfico", "Podcast", "Blog", "E-book", "Webinar"]

# Contando a quantidade de trabalhos entregues
quantidade = len(trabalhos_entregues)

# Exibindo a quantidade de trabalhos entregues
#print(f"\nProfessor, foram entregues {quantidade} trabalhos no total.")
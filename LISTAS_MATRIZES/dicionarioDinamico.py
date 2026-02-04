#Exemplo de dicionarios dinâmicos em Python

# Lista que funcionará como nossa matriz de dicionários
diario_classe = []          # Matriz (lista principal) que armazenará os dicionários (fichas dos alunos)

print("\n")
print("="*40)
print("--- Cadastro de Alunos e Notas ---")
print("="*40)

while True:                                                         # Loop infinito para cadastro de alunos
    nome = input("\nNome do aluno (ou 'sair' para encerrar): ")     # Solicita o nome do aluno
    if nome.lower() == 'sair':                                      # Condição de saída do loop
        break                                                       # Encerra o loop se o usuário digitar 'sair'

    # Solicitando as notas do aluno
    n1 = float(input("Digite a Nota 1: "))
    n2 = float(input("Digite a Nota 2: "))
    n3 = float(input("Digite a Nota 3: "))
    
    # Criando a "ficha" do aluno usando um dicionário
    aluno = {
        "nome": nome,                       # Nome do aluno
        "notas": [n1, n2, n3]               # Lista de notas do aluno
    }
    
    # Adicionando a ficha na nossa matriz (lista principal)
    diario_classe.append(aluno)

print("\n" + "="*40)
print("RELATÓRIO FINAL DO PROFESSOR")
print("="*40)                 # Exibe as notas do aluno

# loop que processa os dados para calcular médias e status
for ficha in diario_classe:
    media = sum(ficha["notas"]) / len(ficha["notas"])       # Calcula a média das notas
    
    # Lógica de status
    if media >= 7.0:
        status = "✅ Aprovado"
    elif 5.0 <= media < 7.0:
        entregou_rec = input(f"\n⚠️  O aluno {ficha['nome']} entregou o trabalho de recuperação? (s/n): ")
        status = "✅ Aprovado via Recuperação" if entregou_rec.lower() == 's' else "❌ Reprovado na Recuperação"
    else:
        status = "❌ Reprovado"
    
    # Exibe o resultado final do aluno

    print(f"\nAluno: {ficha['nome']} | \nnotas: {ficha['notas']} | \nMédia: {media:.1f} | \nStatus: {status}")
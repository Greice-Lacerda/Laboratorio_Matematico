# 1. Definindo diferentes tipos de dados
nome_projeto = "Math Fusion"     # str (texto)
ano_atual = 2026                  # int (inteiro)
valor_pi = 3.1415                # float (decimal)
projeto_ativo = True             # bool (booleano)
primos = [2, 3, 5, 7, 11]        # list (lista/conjunto)

# 2. O comando type() revela a natureza de cada "caixa"
print(f"\nO conteúdo '{nome_projeto}' é do tipo: {type(nome_projeto)}")
print(f"\nO conteúdo '{ano_atual}' é do tipo: {type(ano_atual)}")
print(f"\nO conteúdo '{valor_pi}' é do tipo: {type(valor_pi)}")
print(f"\nO conteúdo '{projeto_ativo}' é do tipo: {type(projeto_ativo)}")
print(f"\nO conteúdo '{primos}' é do tipo: {type(primos)}")

# 3. Experimentando o acesso a listas (Índice 0)
print(f"\nExploração de Conjuntos:")
print(f"\nO primeiro número primo da minha lista é: {primos[0]}")
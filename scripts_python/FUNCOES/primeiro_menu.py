# Arquivo: primeiro_menu.py

# Aqui você importa o SEU arquivo externo: o geometria1.py!
import geometria1

# Loop principal do menu
while True:
    print("\n" + "="*30)                #Isso gera uma linha de separação
    print("   CENTRAL DE GEOMETRIA")    #Título do menu
    print("="*30)                       #Outra linha de separação

    # Opções do menu
    print("\nEscolha uma das opções abaixo:")
    print("[1] Calcular Área")
    print("[2] Calcular Perímetro")
    print("[3] Calcular Volume (Esfera)")
    print("[0] Sair do Programa")
    print("="*30)

    # Solicita a escolha do usuário
    opcao = input("Escolha uma operação: ")

    # Estrutura de decisão para cada opção
    match opcao:
        case "1":
            # Solicita o valor do raio
            r = float(input("\nDigite o raio: "))
            # Chama a função calcular_area do arquivo geometria1.py e imprime o resultado
            print(f"-> A Área é: {geometria1.calcular_area(r):.2f}")

        case "2":
            # Solicita o valor do raio
            r = float(input("Digite o raio: "))
            # Chama a função calcular_perimetro do arquivo geometria1.py e imprime o resultado
            print(f"-> O Perímetro é: {geometria1.calcular_perimetro(r):.2f}")
            
        case "3":
            # Solicita o valor do raio
            r = float(input("Digite o raio: "))
            # Chama a função calcular_volume_esfera do arquivo geometria1.py e imprime o resultado
            print(f"-> O Volume é: {geometria1.calcular_volume_esfera(r):.2f}")
            
        case "0":
            # Mensagem de despedida
            print("Desligando a central... Até logo, Professor!")
            break  # Encerra o loop while

        case _:
            # Mensagem de erro para opção inválida
            print("⚠️ Opção inválida. Tente os números de 0 a 3.")

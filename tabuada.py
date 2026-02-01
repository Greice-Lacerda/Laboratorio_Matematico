# Tabuada de um número qualquer fornecido pelo usuário

# Solicita ao usuário que insira um número
numero = int(input("\nDigite um número para ver sua tabuada: "))
valor_final = int(input("Digite até qual valor você quer ver a tabuada: "))

# Exibe a tabuada do número fornecido
print(f"\nTabuada de {numero}:\n")
for i in range(1, valor_final + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
# Programa para calcular a média ponderada de 4 notas

# Recebendo as notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Pesos das notas
peso1 = 2
peso2 = 2
peso3 = 3
peso4 = 3

# Calculando a média ponderada
soma_pesos = peso1 + peso2 + peso3 + peso4
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4) / soma_pesos

# Exibindo o resultado
print(f"A média ponderada das notas é: {media_ponderada:.2f}")
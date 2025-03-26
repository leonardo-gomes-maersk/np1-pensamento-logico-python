# Programa para calcular o IMC (Índice de Massa Corporal)

# Entrada de dados
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibição do resultado
print(f"Seu IMC é: {imc:.2f}")
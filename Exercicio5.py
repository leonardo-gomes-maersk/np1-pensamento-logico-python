# Programa para verificar se três medidas formam um triângulo e determinar seu tipo

# Entrada das medidas
lado1 = float(input("Digite a primeira medida: "))
lado2 = float(input("Digite a segunda medida: "))
lado3 = float(input("Digite a terceira medida: "))

# Verificação se as medidas formam um triângulo
if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    # Determinação do tipo de triângulo
    if lado1 == lado2 == lado3:
        print("As medidas formam um triângulo equilátero.")
    if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("As medidas formam um triângulo isósceles.")
    if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("As medidas formam um triângulo escaleno.")
else:
    print("As medidas não formam um triângulo.")
META_VENDAS = 15000

nomeVendedor = input("Digite o nome do vendedor: ")
montateVendas = float(input("Digite o montante de vendas: "))

if montateVendas >= META_VENDAS:
    print(f"Parabéns, {nomeVendedor}, você atingiu a meta de vendas!")
else:
    print(f"Infelizmente, {nomeVendedor}, você não atingiu a meta de vendas.")

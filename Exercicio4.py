g_Valor_ingresso = 100
g_Categorias = []

def __init__():
    qtd_ingressos = int(input("Quantos ingresso você deseja comprar?\n"))
    desconto = check_desconto(qtd_ingressos)
    preco_final(qtd_ingressos)

def check_desconto(qtd_ingressos):
    for c in range(qtd_ingressos):
        print(f"Ingresso {c+1}\n1 - Criança\n2 - Idoso\n3 - Professor/Estudante (com carteirinha)\n4 - Inteira\n")
        categoria = int(input(f"Escolha a categoria: "))
        match(categoria):
            case 1: preco = g_Valor_ingresso / 2
            case 2: preco = g_Valor_ingresso / 2
            case 3: preco = g_Valor_ingresso / 2
            case 4: preco = g_Valor_ingresso
        g_Categorias.append(preco)

def preco_final(qtd_ingressos):
    valor_final = 0.0
    for c in g_Categorias:
        valor_final += c
    if qtd_ingressos > 3:
        valor_final *= 0.9
    
    #lmao
    juros = lambda x: (((((x*1.02)*1.02)*1.02)*1.02)*1.02)*1.02

    print("-"*3 + " RESUMO DA COMPRA " + "-"*3 +
    f"\nQuantidade de ingressos: {qtd_ingressos}" +
    f"\nValor final com descontos aplicados: {valor_final}" +

    "\n\n" +

    "-"*3 + " FORMAS DE PAGAMENTO " + "-"*3 +
    f"\nÀ vista (10% de desc.): R${valor_final*0.9:.2f}" +
    f"\nParcelado em 3x de R${(valor_final / 3):.2f}" +
    f"\nParcelado em 6x de R${juros(valor_final) / 6 :.2f} (total: R${juros(valor_final):.2f})")           
__init__()

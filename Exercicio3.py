print("Digite o seu nome: ")
nome = input().title()
print("Qual foi a sua pontuação de produtividade?(De 0 a 100)")
while True:
    produtividade = int(input())
    if produtividade >= 0 or produtividade <= 100:
        break
    print("Valor inválido, digite a pontuação de produtividade de 0 a 100")
print("Digite qual foi a sua presença em %")
while True:
    presenca = int(input())
    if presenca >= 0 or presenca <= 100:
        break
    print("Presença inválida, digite um valor de 0 a 100")

if produtividade >= 80 and presenca >= 90:
    print(f"Parabéns{nome}, seu desempenho foi excelente! Continue o bom trabalho")
elif produtividade >= 60 and presenca >= 75:
    print(f"Muito bem {nome}, seu desempenho foi bom, mas ainda existe espaço para melhora")
else:
    print(f"Poxa {nome}, seu desempenho foi insatisfatório, busque se aprimorar para a próxima avaliação.")
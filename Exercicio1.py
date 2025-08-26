APROVADO = "APROVADO"
REPROVADO = "REPROVADO"

def __validar_info(idade,salario,wanted,nome):
    if all([21 <= idade <= 65, salario > wanted * 3]):
        situation = APROVADO
    else:
        situation = REPROVADO

    print("------------------------------\n"
    f"Seu nome: {nome}\n"
    f"Parcela: {wanted}\n"
    f"Situação: {situation}")
    "------------------------------\n"
    match situation:
        case "APROVADO":
            print("\nFicamos muito feliz de lhe disponibilizar este valor, volte sempre !!")
        case "REPROVADO":
            print(f"\nOi {nome}, entendo que esse momento pode ser desafiador"
                  " e lamento não poder ajudar com um empréstimo nesse momento.\n"
                  "Quero que saiba que, embora eu não possa fornecer o apoio "
                  "financeiro que você pediu, estou torcendo por você e acredito "
                   "que encontrará outras formas de superar esse desafio.")
              
def __init__():
    print("Analise de crédito bancário\n")
    nome = input("Nos diga seu nome\n")
    idade = int(input("Nos diga sua idade\n"))
    salario = float(input("Nos diga sua renda mensal $$\n"))
    wanted_value = float(input("Nos diga seu valor desejado para empréstimo\n"))
    __validar_info(idade,salario,wanted_value,nome)

__init__()

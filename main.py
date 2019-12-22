from datetime import date


# função  que verifica dia da semana retornando um inteiro
#  0 = segunda | 1= terça | 2= quarta | 3= quinta | 4= sexta | 5= sabado | 6= domingo
def verificaDiaData(dataCompleta):
    dataCompleta = dataCompleta.split("/")
    dia = int(dataCompleta[0])
    mes = int(dataCompleta[1])
    ano = int(dataCompleta[2])

    dataCompleta = date(year=ano, month=mes, day=dia)
    diaSemana = int(dataCompleta.weekday())

    return diaSemana


def calculaValorMeuCaninoFeliz(diaSemana, caesPequenos, caesGrandes):
    if diaSemana < 5:
        valorTotal = (caesPequenos * 20.00) + (caesGrandes * 40.00)
    else:
        valorTotal = ((caesPequenos * 20.00) + (caesGrandes * 40.00)) * 1.2

    return valorTotal


def calculaValorVaiRex(diaSemana, caesPequenos, caesGrandes):
    if diaSemana < 5:
        valorTotal = (caesPequenos * 15.00) + (caesGrandes * 50.00)

    else:
        valorTotal = ((caesPequenos * 20.00) + (caesGrandes * 55.00))
    return valorTotal


def calculaValorChowChawgas(caesPequenos, caesGrandes):
    valorTotal = (caesPequenos * 30.00) + (caesGrandes * 45.00)
    return valorTotal


def imprimeValorMeuCaninoFeliz(preco):
    print("Melhor Petshop: Meu  Canino Feliz")
    print("Preço total : %.2f reais\n" % preco)


def imprimeValorVaiRex(preco):
    print("Melhor Petshop: Vai Rex")
    print("Preço total : %.2f reais\n" % preco)


def imprimeValorChowChawgas(preco):
    print("Melhor Petshop: ChowChawgas")
    print("Preço total : %.2f reais\n" % preco)


print("\n Entre com os Dados: \n")
entrada = str(input())
dados = entrada.split(" ")

data = dados[0]
quantCaesPeq = int(dados[1])
quantCaesGrand = int(dados[2])

diaDaSemana = verificaDiaData(data)

precoMeuCanino = calculaValorMeuCaninoFeliz(
    diaDaSemana, quantCaesPeq, quantCaesGrand)
precoVaiRex = calculaValorVaiRex(diaDaSemana, quantCaesPeq, quantCaesGrand)
precoChowChawgas = calculaValorChowChawgas(quantCaesPeq, quantCaesGrand)

# print(precoMeuCanino)
# print(precoVaiRex)
# print(precoChowChawgas)

# considerando as distancias ja pre estabelecidas
if(precoMeuCanino == precoVaiRex == precoChowChawgas):
    imprimeValorChowChawgas(precoChowChawgas)

elif(precoMeuCanino < precoVaiRex) and (precoMeuCanino < precoChowChawgas):
    imprimeValorMeuCaninoFeliz(precoMeuCanino)

elif(precoVaiRex < precoMeuCanino) and (precoVaiRex < precoChowChawgas):
    imprimeValorVaiRex(precoVaiRex)

elif(precoMeuCanino == precoVaiRex):
    imprimeValorVaiRex(precoVaiRex)

elif (precoMeuCanino == precoChowChawgas):
    imprimeValorChowChawgas(precoChowChawgas)

elif (precoVaiRex == precoChowChawgas):
    imprimeValorChowChawgas(precoChowChawgas)

elif(precoChowChawgas < precoMeuCanino) and (precoChowChawgas < precoVaiRex):
    imprimeValorChowChawgas(precoChowChawgas)

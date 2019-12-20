from datetime import date


def verificaDiaData(dataCompleta):
    dataCompleta = dataCompleta.split("/")
    dia = int(dataCompleta[0])
    mes = int(dataCompleta[1])
    ano = int(dataCompleta[2])
    dataCompleta = date(year=ano, month=mes, day=dia)
    # verifica dia da semana | 0 = segunda | 1= terça | 2= quarta | 3= quinta | 4= sexta | 5= sabado | 6= domingo
    diaSemana = int(dataCompleta.weekday())
    return diaSemana


def meuCaninoFeliz(diaSemana, caesPequenos, caesGrandes):
    if diaSemana < 5:
        valorTotal = (caesPequenos * 20.00) + (caesGrandes * 40.00)
    else:
        valorTotal = ((caesPequenos * 20.00) + (caesGrandes * 40.00)) * 1.2

    return valorTotal


def vaiRex(diaSemana, caesPequenos, caesGrandes):
    if diaSemana < 5:
        valorTotal = (caesPequenos * 15.00) + (caesGrandes * 50.00)

    else:
        valorTotal = ((caesPequenos * 20.00) + (caesGrandes * 55.00))
    return valorTotal


def chowChawgas(caesPequenos, caesGrandes):
    valorTotal = (caesPequenos * 30.00) + (caesGrandes * 45.00)
    return valorTotal


entrada = str(input())
dados = entrada.split(" ")
data = dados[0]
quantCaesPeq = int(dados[1])
quantCaesGrand = int(dados[2])
data = verificaDiaData(data)
precoMeuCanino = meuCaninoFeliz(data, quantCaesPeq, quantCaesGrand)
precoVaiRex = vaiRex(data, quantCaesPeq, quantCaesGrand)
precoChowChawgas = chowChawgas(quantCaesPeq, quantCaesGrand)

#print(precoMeuCanino)
#print(precoVaiRex)
#print(precoChowChawgas)

if (precoMeuCanino < precoVaiRex) and (precoMeuCanino < precoChowChawgas):
    print("Melhor Petshop: Meu  Canino Feliz")
    print("Preço total : %.2f"%precoMeuCanino)

elif (precoVaiRex < precoMeuCanino) and (precoVaiRex < precoChowChawgas):
    print("Melhor Petshop: Vai Rex")
    print("Preço total : %.2f" % precoVaiRex)
else:
    print("Melhor Petshop: ChowChawgas")
    print("Preço total : %.2f reais" %precoChowChawgas)



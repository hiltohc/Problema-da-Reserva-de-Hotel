class lakewood:

    def __init__(self):
        self.classicacao = 3
        self.nome = "lakewood"
def calcSemana(dia):

    dia1= dia[10:13]
    if dia1== "sun":
        return "fimSemana"
    elif dia1 == "sat":
        return "fimSemana"
    else:
        return " semana"



def calcDiaria(tipoClitente,dia):
    dia1= calcSemana(dia)
    if tipoClitente == "regular":
        if dia1 == "semana":
            return 100
        else:
            return 80
    else:
        if dia1 == "semana":
            return 90
        else:
            return 80






def calcularDiaTotal(tipoClinte,dia1,dia2,dia3):
   a= calcDiaria(tipoClinte,dia1)
   b= calcDiaria(tipoClinte,dia2)
   c= calcDiaria(tipoClinte,dia3)
   d = a+b+c
   return d

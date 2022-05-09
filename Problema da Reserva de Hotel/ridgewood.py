class ridgewood :
    def __init__ (self):
        self.classicacao = 5
        self.nome = "ridgewood"
def calcSemana(dia):

    dia1= dia[10:13]
    if dia== "sun":
        return "fimSemana"
    elif dia == "sat":
        return "fimSemana"
    else:
        return " semana"



def calcDiaria(tipoClitente,dia):
    dia1 = calcSemana(dia)
    if tipoClitente == "regular":
        if dia1 == "semana":
            return 220
        else:
            return 100
    else:
        if dia1 == "semana":
            return 150
        else:
            return 40



def calcularDiaTotal(tipoClinte,dia1,dia2,dia3):
   a= calcDiaria(tipoClinte,dia1)
   b= calcDiaria(tipoClinte,dia2)
   c= calcDiaria(tipoClinte,dia3)
   d = a+b+c
   return d
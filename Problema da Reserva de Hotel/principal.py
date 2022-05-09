import lakewood
import ridgewood
import bridgewood

hotelLake = lakewood()
hotelRidgewood = ridgewood()
hotelbridgewood=bridgewood()

def calcularDiahotel(tipoClinte,dia1,dia2,dia3):
    a=hotelLake.calcularDiaTotal(tipoClinte,dia1,dia2,dia3)
    b=hotelRidgewood.calcularDiaTotal(tipoClinte,dia1,dia2,dia3)
    c=hotelbridgewood.calcularDiaTotal(tipoClinte,dia1,dia2,dia3)
    if (a > b) and (a > c) :
        if(a==b) and (hotelLake.classicacao> hotelRidgewood.classicacao):
         return print(' {} '.format(hotelLake.nome))
        elif (a == c) and (hotelLake.classicacao > hotelbridgewood.classicacao):
            return print(' {} '.format(hotelLake.nome))
        else:
            return print(' {} '.format(hotelLake.nome))
    elif(b > a) and (b > c):
        return print(' {} '.format(hotelbridgewood.nome))
    elif (b > a) and (b > c):
        return print(' {} '.format(hotelRidgewood.nome))



# retorna o hotel mais barato
cal1 = calcularDiahotel("Regular","16Mar2009(mon)", "17Mar2009(tues)","18Mar2009(wed)")
cal2 = calcularDiahotel("Regular","20Mar2009(fri)","21Mar2009(sat)"," 22Mar2009(sun)")
cal3 = calcularDiahotel("Rewards","26Mar2009(thur)","27Mar2009(fri)","28Mar2009(sat)")

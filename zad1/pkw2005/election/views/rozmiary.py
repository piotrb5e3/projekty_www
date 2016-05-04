from ..models import Gmina, RodzajGminy
class Rozmiar():
    def __init__(self):
        pass

def createranges():
    gminy = Gmina.objects.all()
    result = []
    s=RodzajGminy.objects.get(nazwa="statki")
    z=RodzajGminy.objects.get(nazwa="zagranica")
    r = Rozmiar()
    r.num = len(result)
    r.nazwa ="Statki i zagranica"
    r.waz = s.glosowWaznych + z.glosowWaznych
    r.k1 = s.glosowKand1 + z.glosowKand1
    r.k2 = s.glosowKand2 + z.glosowKand2
    if(r.waz > 0 ):
        r.p1 = "{0:.2f}".format(100 * r.k1 / r.waz)
        r.p2 = "{0:.2f}".format(100 * r.k2 / r.waz)
    else:
        r.p1 = "--.--"
        r.p2 = "--.--"

    result.append(r)

    r = Rozmiar()
    gm = gminy.filter(liczbaMieszkancow__lte=5000)
    r.num = len(result)
    r.nazwa ="do 5000"
    r.waz = sum( g.liczbaGlosowWaznych for g in gm)
    r.k1 =  sum( g.liczbaGlosowKand1 for g in gm)
    r.k2 =  sum( g.liczbaGlosowKand2 for g in gm)
    if(r.waz > 0 ):
        r.p1 = "{0:.2f}".format(100 * r.k1 / r.waz)
        r.p2 = "{0:.2f}".format(100 * r.k2 / r.waz)
    else:
        r.p1 = "--.--"
        r.p2 = "--.--"

    result.append(r)


    vals = [5000, 10000, 20000, 50000, 100000, 200000, 500000]
    for i in range(0, len(vals)-1):
        gm = gminy.filter(
            liczbaMieszkancow__lte=vals[i+1]
            ).filter(liczbaMieszkancow__gt=vals[i])

        r = Rozmiar()
        r.num = len(result)
        r.nazwa = "od " + str(vals[i] + 1) + " do " + str(vals[i + 1])
        r.waz = sum( g.liczbaGlosowWaznych for g in gm)
        r.k1 =  sum( g.liczbaGlosowKand1 for g in gm)
        r.k2 =  sum( g.liczbaGlosowKand2 for g in gm)
        if(r.waz > 0 ):
            r.p1 = "{0:.2f}".format(100 * r.k1 / r.waz)
            r.p2 = "{0:.2f}".format(100 * r.k2 / r.waz)
        else:
            r.p1 = "--.--"
            r.p2 = "--.--"

        result.append(r)

    r = Rozmiar()
    gm = gminy.filter(liczbaMieszkancow__gt=500000)
    r.nazwa ="pow 500000"
    r.num = len(result)
    r.waz = sum( g.liczbaGlosowWaznych for g in gm)
    r.k1 =  sum( g.liczbaGlosowKand1 for g in gm)
    r.k2 =  sum( g.liczbaGlosowKand2 for g in gm)
    if(r.waz > 0 ):
        r.p1 = "{0:.2f}".format(100 * r.k1 / r.waz)
        r.p2 = "{0:.2f}".format(100 * r.k2 / r.waz)
    else:
        r.p1 = "--.--"
        r.p2 = "--.--"

    result.append(r)

          
    return result



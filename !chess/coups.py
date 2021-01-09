from case import* 

def move(deplacement, ech, turn):
    depart = conversion_tab(str(deplacement[0] + deplacement[1]))
    fin = conversion_tab(str(deplacement[2] + deplacement[3]))
    pion = ech[depart]
    ech[fin] = pion
    ech[depart] = 0
    return ech   
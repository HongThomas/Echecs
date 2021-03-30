from case import* 

def move(deplacement, ech, turn):
    depart = conversion_tab(str(deplacement[0] + deplacement[1]))
    fin = conversion_tab(str(deplacement[2] + deplacement[3]))
    pion = ech[depart]
    ech[fin] = pion
    ech[depart] = 0
    return ech   

def pion(ech, pos_depart):
    coups_possibles = []
    pos_depart = conversion_tab(pos_depart)
    couleur = color(ech[pos_depart])


    if couleur == 'black':

        # Cas où les pièces sont au départs
        if pos_depart > 47 and pos_depart < 56:
            if color(ech[pos_depart-8]) =='empty':
                coups_possibles.append(pos_depart - 8)
            if color(ech[pos_depart-16]) =='empty':
                coups_possibles.append(pos_depart - 16)

        else:
            if color(ech[pos_depart - 8]) == 'empty' and exist(pos_depart-8):
                coups_possibles.append(pos_depart - 8)
            if color(ech[pos_depart - 9]) == 'black':
                coups_possibles.append(pos_depart - 9)
            if color(ech[pos_depart - 7]) =='black':
                coups_possibles.append(pos_depart - 7)

    else:


        if pos_depart < 16 and pos_depart > 7:
            if color(ech[pos_depart+8]) =='empty' and exist(pos_depart+8):              
                coups_possibles.append(pos_depart + 8)
            if color(ech[pos_depart+16]) =='empty' and exist(pos_depart+16):
                coups_possibles.append(pos_depart + 16)
        else:
            if color(ech[pos_depart + 8]) == 'empty' and exist(pos_depart+8):
                coups_possibles.append(pos_depart + 8)
            if color(ech[pos_depart + 9]) == 'white':
                coups_possibles.append(pos_depart + 9)
            if color(ech[pos_depart + 7]) =='white':
                coups_possibles.append(pos_depart + 7)
    return coups_possibles
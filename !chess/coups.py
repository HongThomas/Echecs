from case import* 

def move(deplacement, ech, turn):
    depart = conversion_tab(str(deplacement[0] + deplacement[1]))
    fin = conversion_tab(str(deplacement[2] + deplacement[3]))
    pion = ech[depart]
    ech[fin] = pion
    ech[depart] = 0
    return ech   

#def pion(dico):
#    cases_possibles = []
#    pos_depart = dico['pos']
#    if dico == 'white' and dico['type'] == 'pion':
#        cases_possibles += [pos+8]
#        if pos > 44 and pos < 56:
 #           cases_possibles += [pos+16] 
  #  else:
   #     cases_possibles += [pos-8]
    #    if pos > 7 and pos < 16:
     #       cases_possibles += [pos-8, pos-16]
      #  else:
       #     cases_possibles += [pos-8]
    #return cases_possibles

def mate(ech):
    state = 'continue'
    if 11 not in ech:
        state = 'win_white'
    if 6 not in ech:
        state = 'win_black'
    return state

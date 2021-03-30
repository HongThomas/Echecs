
def conversion(piece):
    '''Convertie valeur pièce
    en unicode. Prend en paramètre
    le numéro de la pièce.
    '''
    if piece == 0:      #Case vide
        return '\u26F6' 
    elif piece == 1:    #Pion b
        return '\u2659' 
    elif piece == 2:    #Tour b
        return '\u2656'
    elif piece == 3:    #Cavalier b
        return '\u2658'
    elif piece == 4:    #Fou b
        return '\u2657'
    elif piece == 5:    #Reine b
        return '\u2654'
    elif piece == 6:    #Roi b
        return '\u2655'
    elif piece == 7:    #Pion n
        return '\u265F'
    elif piece == 8:    #Tour n
        return '\u265C'
    elif piece == 9:    #Cavalier n
        return '\u265E'
    elif piece == 10:   #Fou n
        return '\u265D'
    elif piece == 11:   #Roi n
        return '\u265A'
    elif piece == 12:   #Reine n
        return '\u265B'
   
def reverse(ech):
    '''Inverse horizontalement
    le tableau de l'échéquier.
    Prend en paramètre le tableau.
    '''
    i = 0
    new_ech = []
    k = 56
    while i < 8:
        j = 0
        ligne = []
        while j < 8:
            tab = [ech[j + k]]
            ligne += tab
            j += 1
        new_ech += ligne
        k -= 8
        i += 1
    return new_ech

def affichage2(ech, turn):
    '''Affcihe l'échéquier selon
    sa couleur.
    Prend en paramètre le tableau 
    et la couleur du tour.
    '''
    if turn == 'white': # Tour des blancs
        i = 8
        k = 0
        ech = reverse(ech) # Inverser l'échéquier
        while i > 0:
            j = 0
            ligne = str(i) + "| "
            while j < 8:
                ligne += str(conversion(ech[j + k])) + " " 
                j += 1
            print(ligne)
            k += 8
            i -= 1
        print('--------------------')
        print('   a b c d e f g h')  
    else:           # Tour des noirs
        i = 0
        k = 0

        while i < 8:
            j = 0
            ligne = str(i+1) + "| "
            while j < 8:
                ligne += str(conversion(ech[j + k])) + " "
                j += 1
            print(ligne)
            k += 8
            i += 1
        print('--------------------')
        print('   a b c d e f g h')       

def affichage(ech):
    i = 8
    z = 56
    while i > 0:
        j = 0
        ligne = str(i) + "| "
        while j < 8:
            ligne += str(conversion(ech[z])) + " "
            z += 1
            j += 1
        
        print(ligne)
        i -= 1
        z-=16
    print('--------------------')
    print('   a b c d e f g h') 
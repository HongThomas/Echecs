from case import* 
from coups import*
from affiche import*

ech =   [   8, 9,10,11,12,10, 9, 8,
            7, 7, 7, 7, 7, 7, 7, 7,   
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1,
            2, 3, 4, 5, 6, 4, 3, 2,
        ]

def affichage(ech):
    i = 8
    z = 63
    while i > 0:
        j = 0
        ligne = str(i) + "| "
        while j < 8:
            ligne += str(conversion(ech[z])) + " "
            z -= 1
            j += 1
        print(ligne)
        i -= 1
    print('--------------------')
    print('   a b c d e f g h') 

affichage(ech)
from affiche import*
from case import*
from coups import*

ech =   [   8, 9,10,11,12,10, 9, 8,#noires
            7, 7, 7, 7, 7, 7, 7, 7,       
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, #cases vides
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1, 
            2, 3, 4, 5, 6, 4, 3, 2 ]#blancs

         
white = [ { 'type' : 'tour', 'pos' : 0, 'reach' : [0] }, { 'type' : 'cavalier', 'pos' : 1, 'reach' : [16,18] }, { 'type' : 'fou', 'pos' : 2, 'reach' : [2] },
        { 'type' : 'reine', 'pos' : 3 , 'reach' : [3] },
        { 'type' : 'roi', 'pos' : 4 , 'reach' : [4] }, { 'type' : 'fou', 'pos' : 5, 'reach' : [5] }, { 'type' : 'cavalier', 'pos' : 6 , 'reach' : [21,23] },
        { 'type' : 'tour', 'pos' : 7 , 'reach' : [7] }, 
        { 'type' : 'pion', 'pos' : 8, 'reach' : [16,24] }, { 'type' : 'pion', 'pos' : 9, 'reach' : [17,25] }, { 'type' : 'pion', 'pos' : 10, 'reach' : [18,26] }, 
        { 'type' : 'pion', 'pos' : 11, 'reach' : [19,27] },
        { 'type' : 'pion', 'pos' : 12, 'reach' : [20,28] }, { 'type' : 'pion', 'pos' : 13, 'reach' : [21,29] }, { 'type' : 'pion', 'pos' : 14, 'reach' : [22,30] }, 
        { 'type' : 'pion', 'pos' : 15, 'reach' : [23,31] } ] 
black = [ { 'type' : 'tour', 'pos' : 56, 'reach' : [56] }, { 'type' : 'cavalier', 'pos' : 56, 'reach' : [40,42] }, { 'type' : 'fou', 'pos' : 58, 'reach' : [58] }, 
        { 'type' : 'reine', 'pos' : 59 , 'reach' : [59] },
        { 'type' : 'roi', 'pos' : 60 , 'reach' : [60] }, { 'type' : 'fou', 'pos' : 61, 'reach' : [61] }, { 'type' : 'cavalier', 'pos' : 62 , 'reach' : [45,47] }, 
        { 'type' : 'tour', 'pos' : 63 , 'reach' : [63] }, 
        { 'type' : 'pion', 'pos' : 48, 'reach' : [40,32] }, { 'type' : 'pion', 'pos' : 49, 'reach' : [41,33] }, { 'type' : 'pion', 'pos' : 50, 'reach' : [42,34] }, 
        { 'type' : 'pion', 'pos' : 51, 'reach' : [43,35] },
        { 'type' : 'pion', 'pos' : 52, 'reach' : [44,36] }, { 'type' : 'pion', 'pos' : 53, 'reach' : [45,37] }, { 'type' : 'pion', 'pos' : 54, 'reach' : [46,38] }, 
        { 'type' : 'pion', 'pos' : 55, 'reach' : [47,39] } ]

jouer = True
while jouer:
        turn = 'white'
        print(affichage(ech, turn))
        deplacement = input('Tour blanc (dép->fin): ')
        ech = move(deplacement,ech, turn)
        print(affichage(ech, turn))


        turn = 'black'
        print(affichage(ech, turn))
        deplacement = input('Tour noir (dép->fin): ')
        ech = move(deplacement, ech, turn)
        print(affichage(ech, turn))
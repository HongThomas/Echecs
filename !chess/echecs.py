from affiche import*
from case import*
from coups import*

ech2 =  [   2, 3, 4, 5, 6, 4, 3, 2,
            1, 1, 1, 1, 1, 1, 1, 1,     
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            7, 7, 7, 7, 7, 7, 7, 7,
            8, 9,10,11,12,10, 9, 8,
        ]

ech =   [   8, 9,10,11,12,10, 9, 8,
            7, 7, 7, 7, 7, 7, 7, 7,   
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1,
            2, 3, 4, 5, 6, 4, 3, 2,
        ]

         
white = [ { 'type' : 'tour', 'pos' : 'a1', 'reach' : [0] }, { 'type' : 'cavalier', 'pos' : 'b1', 'reach' : [16,18] }, { 'type' : 'fou', 'pos' : 'c1', 'reach' : [2] },
        { 'type' : 'reine', 'pos' : 'd1' , 'reach' : [3] },
        { 'type' : 'roi', 'pos' : 'e1' , 'reach' : [4] }, { 'type' : 'fou', 'pos' : 'f1', 'reach' : [5] }, { 'type' : 'cavalier', 'pos' : 'g1', 'reach' : [21,23] },
        { 'type' : 'tour', 'pos' : 'h1' , 'reach' : [7] }, 
        { 'type' : 'pion', 'pos' : 'a2', 'reach' : [16,24] }, { 'type' : 'pion', 'pos' : 'b2', 'reach' : [17,25] }, { 'type' : 'pion', 'pos' : 'c2', 'reach' : [18,26] }, 
        { 'type' : 'pion', 'pos' : 'd2', 'reach' : [19,27] },
        { 'type' : 'pion', 'pos' : 'e2', 'reach' : [20,28] }, { 'type' : 'pion', 'pos' : 'f2', 'reach' : [21,29] }, { 'type' : 'pion', 'pos' : 'g2', 'reach' : [22,30] }, 
        { 'type' : 'pion', 'pos' : 'h2', 'reach' : [23,31] } ] 
black = [ { 'type' : 'tour', 'pos' : 'a8', 'reach' : [56] }, { 'type' : 'cavalier', 'pos' : 'b8', 'reach' : [40,42] }, { 'type' : 'fou', 'pos' : 'c8', 'reach' : [58] }, 
        { 'type' : 'reine', 'pos' : 'd8' , 'reach' : [59] },
        { 'type' : 'roi', 'pos' : 'e8' , 'reach' : [60] }, { 'type' : 'fou', 'pos' : 'f8', 'reach' : [61] }, { 'type' : 'cavalier', 'pos' : 'g8', 'reach' : [45,47] }, 
        { 'type' : 'tour', 'pos' : 'h8' , 'reach' : [63] }, 
        { 'type' : 'pion', 'pos' : 'a7', 'reach' : [40,32] }, { 'type' : 'pion', 'pos' : 'b7', 'reach' : [41,33] }, { 'type' : 'pion', 'pos' : 'c7', 'reach' : [42,34] }, 
        { 'type' : 'pion', 'pos' : 'd7', 'reach' : [43,35] },
        { 'type' : 'pion', 'pos' : 'e7', 'reach' : [44,36] }, { 'type' : 'pion', 'pos' : 'f7', 'reach' : [45,37] }, { 'type' : 'pion', 'pos' : 'g7', 'reach' : [46,38] }, 
        { 'type' : 'pion', 'pos' : 'h7', 'reach' : [47,39] } ]

jouer = 'o'
while jouer == 'o':
        turn = 'white'
        print(affichage(ech))
        print('****************************************')
        deplacement = input('Tour blanc (dép->fin): ')
        ech = move(deplacement,ech, turn)

        print('****************************************')

        turn = 'black'
        print(affichage(ech))
        print('****************************************')
        deplacement = input('Tour noir (dép->fin): ')
        ech = move(deplacement, ech, turn)
 
        print('****************************************')
        jouer = input('Continuer ? ')
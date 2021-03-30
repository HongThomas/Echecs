def conversion_tab(case):
    '''Convertie cases échecs en position.
    '''
    let = ord(case[0])
    num = ord(case[1])
    n = (let-97)+(num-49)*8
    return n

def exist(case):
    '''Verifie si la case existe donc
    dans le tableau ech entre 0 et 63.
    '''
    return ( case < 64 and case >= 0)

def color(pos):
    '''retourne
        si blanc, noir ou vide.
    '''
    if pos > 6:
        return 'black'
    elif pos == 0:
        return 'empty'
    return 'white'

def case(case,ech):
    '''Retourne un tableau avec si case existe,
    la couleur et case de la pièce.
    '''
    position = conversion_tab(case)
    tab_case = []
    if not exist(case):
        tab_case.append(False)
    tab_case.append(True)
    tab_case.append(color(case,ech))
    tab_case.append(position)
    return tab_case
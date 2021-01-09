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
    exist = conversion_tab(case)
    return ( exist < 64 and exist >= 0)

def color(case,ech):
    '''Convertie case puis retourne
        si blanc, noir ou vide.
    '''
    pos = conversion_tab(case)
    if ech[pos] > 6:
        return 'black'
    elif ech[pos] == 0:
        return 'empty'
    return 'white'

def case(case,ech):
    '''Retourne un tableau si case existe,
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


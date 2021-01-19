ech = [1,2,3]

def echec(ech):
    if 4 in ech:
        return 'lol'
    if 5 in ech:
        return 'xd'
    return 'nope'

k = echec(ech)
while k != 'xd' and k != 'lol':
    print('0')
    v = int(input('v: '))
    ech.append(v)
    k = echec(ech)
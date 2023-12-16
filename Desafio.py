heroisXp = [ 
    ['Avel',1000],
    ['Covalsqui',2500],
    ['Madalena',8500],
    ['jaco',4000],
    ['Irineu',10300],
]



def ClassificadroDeNivel(xp):
    if xp <= 1000:
        return ('Ferro')
    elif xp > 1000 and xp <= 2000:
        return ('Bronze')
    elif xp > 2000 and xp <= 5000:
        return ('Prata Ouro')
    elif xp > 5000 and xp <= 8000:
        return ('Platina Diamante')
    elif xp > 8000 and xp <= 9000:
        return ('Ascendnte')
    elif xp > 9000 and xp <= 10000:
        return ('imortal')
    elif xp > 1000:
        return ('Radiante')



for heroi in heroisXp:
    NivelDoHeroi = ClassificadroDeNivel(heroi[1]) 
    nome = heroi[0]

    print(f"O nivel do heroi {nome} é {NivelDoHeroi}")


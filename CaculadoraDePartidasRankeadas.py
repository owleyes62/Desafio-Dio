# Potência Tech iFood - Programação do Zero

PerfilHeroi_H_V_D = [ 
    ['Avel', 10 , 20],
    ['Covalsqui',100 , 30],
    ['Madalena',60 , 70],
    ['jaco',200, 50],
    ['Irineu',120, 2],
]



def CaculadoraDePartidas(numVitorias):
    if numVitorias <= 10:
        return ('Ferro')
    elif numVitorias > 10 and numVitorias <= 20:
        return ('Bronze')
    elif numVitorias > 20 and numVitorias <= 50:
        return ('Prata')
    elif numVitorias > 50 and numVitorias <= 80:
        return ('Ouro')
    elif numVitorias > 80 and numVitorias <= 90:
        return ('Diamante')
    elif numVitorias > 90 and numVitorias <= 100:
        return ('Ledanrio')
    elif numVitorias > 100:
        return ('Imortal')



for Perfil in PerfilHeroi_H_V_D:
    nome = Perfil[0]
    numVitorias = Perfil[1] - Perfil[2]
    NivelDoHeroi = CaculadoraDePartidas(numVitorias)
    print(f"O heroi {nome} tem saldo de {numVitorias} partidas vencidas e esta no nivel {NivelDoHeroi}")

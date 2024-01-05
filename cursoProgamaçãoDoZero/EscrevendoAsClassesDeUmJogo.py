# Potência Tech iFood - Programação do Zero

class Heroi():
    nome = 'cacau'
    idade = 23 
    tipo = 'guerreiro'

    def Ataque (self):
        if self.tipo == 'guerreiro':
            return  f"o guerreio {self.nome} atacou usando espada"
        if self.tipo == 'mago':
            return f"o mago {self.nome} atacou usando magia"
        if self.tipo == 'monge':
            return f"o monge {self.nome} atacou usando artes marciais"
        if self.tipo == 'ninja':
            return f"o ninja {self.nome} atacou usando shuriken"
     

heroi_cacau = Heroi()
resultado_ataque = heroi_cacau.Ataque()
print(resultado_ataque)
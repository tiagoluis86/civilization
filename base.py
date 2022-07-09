# Classes principais do jogo

class Civilization:
    def __init__(self, nome, lider, vantagem, desvantagem):
        self.nome = nome
        self.lider = lider
        self.vantagem = vantagem
        self.desvantagem = desvantagem

class Tecnologia:
    def __init__(self, nome, retorno, duracao):
        self.nome = nome
        self.retorno = retorno
        self.duracao = duracao

class Construcao:
    def __init__(self, nome, funcao, dano, defesa, vida, tempo_construcao):
        self.nome = nome
        self.funcao = funcao
        self.dano = dano
        self.defesa = defesa
        self.vida = vida
        self.tempo_construcao = tempo_construcao

class Unidade:
    def __init__(self, nome, dano, defesa, funcao, vida, tempo_construcao):
        self.nome = nome
        self.dano = dano
        self.defesa = defesa
        self.funcao = funcao
        self.vida = vida
        self.tempo_construcao = tempo_construcao
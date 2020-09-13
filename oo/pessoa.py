class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar (self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
        davilucas = Pessoa(nome='Davi Lucas')
        danilo = Pessoa(davilucas, nome='Danilo')
        print(Pessoa.cumprimentar(danilo))
        print(id(danilo))
        print(danilo.cumprimentar())
        print(danilo.nome)
        print(danilo.idade)
        for filho in danilo.filhos:
            print(filho.nome)

class Pessoa:
    olhos = 2
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
        danilo.sobrenome = 'Ramos'
        del danilo.filhos
        danilo.olhos = 1
        del danilo.olhos
        print(danilo.__dict__)
        print(davilucas.__dict__)
        Pessoa.olhos = 3
        print(Pessoa.olhos)
        print(danilo.olhos)
        print(davilucas.olhos)
        print(id(Pessoa.olhos), id(danilo.olhos), id(davilucas.olhos))

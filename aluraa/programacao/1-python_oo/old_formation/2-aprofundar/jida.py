class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def dar_like(self):
        self._likes += 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao


class Serie(Programa) :
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print('Nome: {} - Ano: {} - Duração: {} - Likes: {}' .format(vingadores.nome, vingadores.ano, vingadores.duracao,vingadores.likes))

vikins = Serie('vikins ', 2016, 10)
vikins.dar_like()
vikins.dar_like()
vikins.dar_like()
print('Nome: {} - Ano: {} - temporadas: {} - Likes:{}' .format(vikins.nome, vikins.ano, vikins.temporadas,vikins.likes))

filmes_series = [ vingadores, vikins ]

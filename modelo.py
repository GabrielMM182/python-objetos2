class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return (f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes}')

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return (f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return (f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}')

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item): #duck type
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

velozes = Filme('velozes e furiosos', 2001, 117)
evil = Filme('evil dead', 1982, 98)
office = Serie('the office', 2005, 9)
round = Serie('round6', 2021, 1)

velozes.dar_likes()
velozes.dar_likes()
evil.dar_likes()
round.dar_likes()
office.dar_likes()
office.dar_likes()
office.dar_likes()
office.dar_likes()

filmes_e_series = [velozes, office, evil, round]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana.listagem)}')


for programa in playlist_fim_de_semana.listagem:
    print(programa)

print(f'Tá ou não tá? {office in playlist_fim_de_semana}')
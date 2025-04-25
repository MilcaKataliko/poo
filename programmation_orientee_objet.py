"""class Rectacle:
   # largeur = 3
    #hauteur = 2

    def calculer_surface(self):
        return self.largeur * self.hauteur

    def __init__(self, longeur, largeur, couleur="red"):
        self.longeur = longeur
        self.largeur = largeur
        self.couleur = couleur
    def calculer_surface(self):
        return self.longeur * self.largeur

rectacle = Rectacle(5,3,)
print(rectacle.longeur)
print(rectacle.largeur)
print(rectacle.couleur)"""

"""class Film:
    def __init__(self, name):
        self.name = name
    
    def watch(self):
        print("bon visionnage")

class FilmCassette(Film):
    pass

film = Film("2001: l'odyste de l'espace")
filme_cassette = FilmCassette("Blader Runner")

film.name
film.watch()

filme_cassette.name
filme_cassette.watch()"""

class Film:
    def __init__(self, name):
        self.name = name
        self.magnetic_tape = True
    
    def rewind(self):
        print("c'est long a rembobiner")
        self.magnetic_tape = True

film = Film("2001: l'odyste de l'espace")
filme_cassette = FilmCassette("Blader Runner")

print(filme_cassette.name)
print(filme_cassette.magnetic_tape)
filme_cassette.watch()
filme_cassette.rewind()
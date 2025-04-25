class Animal:
    def crier(self):
        print("un cri d'animal")

class Chien(Animal):
    def crier(self):
        print("woauf! woauf!")

class Chat(Animal):
    def crier(self):
        print("Miaou!")

class Inconnu(Animal):
    def crier(self):
        return super().crier()
animal = Animal()
cri_animal = animal.crier()

chien = Chien()
cri_chien = chien.crier()

chat = Chat()
cri_chat = chat.crier()

inconnu = Inconnu()
cri_animal_inconnu= inconnu.crier()
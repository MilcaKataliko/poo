class Stagiaire:

    def __init__(self, numi, age, nom, prenom, note1, note2):
        self.numinsription=numi
        self.__age=age
        self.__nom=nom
        self.__prenom=prenom
        self.__note1=note1
        self.__note2=note2

        def calculer_Moyenne(self):
            moyenne=(self.__note1+ self.__note2)/2
            print("La moyenne:", moyenne)
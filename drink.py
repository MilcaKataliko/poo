class Drink:
    def __init__(self, price):
        self.price = price
    def drink(self):
        print("je ne sais pas c'est, mais je le bois")
class Coffee(Drink):
    prices = {"simple":1, "serre":1, "allonge":1.5}

    def __init__(self, type):
        self.type = type
        super().__init__(price=self.prices.get(type, 1))

    def drink(self):
        print(f"un bon café de {self.type} qui coute {self.price}$ pour me reveiller !")

Coffee = Coffee("allonge")
boire = Coffee.drink()

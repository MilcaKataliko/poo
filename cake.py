class cake:
    def __init__(self, flavor):
        self.flavor = flavor
    
    def cut_in_part(self):
        print("Le gateau est coupé en 4parts")
cake = cake("chocolate")
print (cake.flavor)
cake.cut_in_part()
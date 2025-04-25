fruit = "pomme"
match fruit:
    case "pomme":
        print("j'aime les pommes!")
    case "banane":
        print("j'aime les bananes")
    case "orange":
        print("Les oranges sont bonnes pour la sante")
    case_:
        print("je ne connais pas ce fruit")

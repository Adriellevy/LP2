import ship
class Cargo(ship.Ship):
    def __init__(self, cargo, quality, draft, crew):
        ship.Ship.__init__(self, draft, crew)
        self.cargo = cargo
        self.quality = quality
        if self.quality == 1:
            self.draft = 3.5 + draft
        elif self.quality == 0.5:
            self.draft = 2 + draft
        elif self.quality == 0.25:
            self.draft = 0.5 + draft
        else:
            raise TypeError("Something else went wrong")

    def is_worth_it(self):
        try:
            peso = self.draft - (self.crew * 1.5)
            if peso < 20:
                raise TypeError("No merece ser  saqueado")
            else:
                print("Merece ser saqueado")
        except TypeError as error:
            print(error)


import ship
class Cruise (ship.Ship):
    def __init__(self, passengers, draft, crew):
        ship.Ship.__init__(self,draft,crew)
        self.passengers = passengers
        self.draft = (2.25 * passengers) + draft

    def is_worth_it(self):
        try:
            peso = self.draft - (self.crew * 1.5) - (self.passengers * 2.25)
            if peso < 20:
                raise TypeError("No merece ser  saqueado")
            else: print("Merece ser saqueado")
        except TypeError as error:
           print(error)




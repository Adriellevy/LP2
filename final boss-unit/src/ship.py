class Ship:
    def __init__(self, draft, crew):
        self.crew = crew
        self.draft = (1.5 * self.crew) + draft

    def is_worth_it(self):
        try:
            peso = self.draft - (self.crew * 1.5)
            if peso < 20:
                    raise TypeError("No merece ser  saqueado")
            else:
                    print("Merece ser saqueado")
        except TypeError as error:
                  print(error)


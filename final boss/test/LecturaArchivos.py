import pandas as pd
import math
def lectura():
    Barcos = pd.read_csv("ships.csv")
    """
    Segmentacion de los datos en los 3 diferentes tipos de datos 
                 Ship:
                    - Cargo == null 
                    - extra == null
                 Cargo: 
                    - extra == null
                 Pasangers: 
                    - Cargo == null    
    """
    Cargos = Barcos[Barcos["quality"].notna()]
    Pasageros = Barcos[Barcos["quality"].isna() & Barcos["extra"].notna()]
    Ships = Barcos[Barcos["quality"].isna() & Barcos["extra"].isna()]
    """
    print("Barcos:\n "+str(Barcos)+"\n")
    print("Cargos: \n"+str(Cargos)+"\n")
    print("Pasajeros: \n"+str(Pasageros)+"\n")
    print("Ships: \n"+str(Ships)+"\n")
    """


if __name__ == "__main__":
  lectura()

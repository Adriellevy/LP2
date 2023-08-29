import pandas as pd
import Tests
def lectura():
    Barcos = pd.read_csv("ships.csv",index_col=0)
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


    Tripulacion = Cargos['crew']
    #Tripulacion = Barcos[Barcos["crew"]]
    #Tripulacion = Barcos[Barcos["crew"]]

    print("Barcos:\n " + str(Barcos) + "\n")
    print("Cargos: \n" + str(Cargos) + "\n")
    print(str(Tripulacion))
    """for i in range(0,len(Cargos)):
        
        Tests.test_negativo_cargo(Cargos[[i,"draft"]],Cargos[i,"crew"]])
    """
   # print("Barcos:\n "+str(Barcos)+"\n")
   # print("Cargos: \n"+str(Cargos)+"\n")
   # print("Pasajeros: \n"+str(Pasageros)+"\n")
   # print("Ships: \n"+str(Ships)+"\n")



if __name__ == "__main__":
  lectura()

from src import ship
from src import cargo
from src import cruise
def main() -> None:
  barco=ship.Ship(20,15)
  cargamento=cargo.Cargo(10,2,10,12)
  crucero=cruise.Cruise(30,10,10)

  cargamento.is_worth_it()
  barco.is_worth_it()
  crucero.is_worth_it()
if __name__ == "__main__":
  main()

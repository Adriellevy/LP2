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

def test_negativo_ship():
  barquito=ship.Ship(20,15)
  barquito2 = ship.Ship(-20, 15)
  barquito3=ship.Ship(0,0)
  assert barquito.is_worth_it()
  assert barquito2.is_worth_it()
  assert barquito3.is_worth_it()

def test_positivo_ship():
  barquito1 = ship.Ship(20, 30)
  assert barquito1.is_worth_it()

def test_negativo_cargo():
  carga1=cargo.Cargo(10,1,10,12)
  carga2 = cargo.Cargo(10, 1, 10, 12)
  carga3 = cargo.Cargo(10, 3, 10, 12)  # quality 3 no existe,tira error
  carga4=cargo.Cargo(0,0,0,0)
  assert carga1.is_worth_it()
  assert carga2.is_worth_it()
  assert carga3.is_worth_it()
  assert carga4.is_worth_it()

def test_positivo_cargo():
  carga1=cargo.Cargo(40,1,10,12)
  assert carga1.is_worth_it()
  carga2=cargo.Cargo(10,0.5,10,12)

def test_negativo_cruise():
  crucero1=cruise.Cruise(1,20,15)
  crucero2=cruise.Cruise(-1,5,20)
  crucero3=cruise.Cruise(0,0,0)
  assert crucero1.is_worth_it()
  assert crucero2.is_worth_it()
  assert crucero3.is_worth_it()

def teste_positivo_cruise():
  crucero4=cruise.Cruise(20,30,50)
if __name__ == "__main__":
  main()

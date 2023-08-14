from src import ship
from src import cargo
from src import cruise

def test_negativo_ship(barco):
  barco=ship.Ship(barco)
  assert barco.is_worth_it()

def test_positivo_ship(barco):
  barco = ship.Ship(barco)
  assert barco.is_worth_it()

def test_negativo_cargo(cargo_):
  cargo_ = ship.Ship(cargo_)
  assert cargo_.is_worth_it()

def test_positivo_cargo(cargo_):
  cargo_ = ship.Ship(cargo_)
  assert cargo_.is_worth_it()

def test_negativo_cruise(crucero):
  crucero = ship.Ship(crucero)
  assert crucero.is_worth_it()

def test_positivo_cruise(crucero):
  crucero = ship.Ship(crucero)
  assert crucero.is_worth_it()



"""from src import ship
from src import cargo
from src import cruise

def test_negativo_ship(draft_,crew_):
  barco=ship.Ship(draft_,crew_)
  assert barco.is_worth_it()

def test_positivo_ship(draft_, crew_):
  barco = ship.Ship(draft_, crew_)
  assert barco.is_worth_it()

def test_negativo_cargo(draft_,quality_, crew_):
  cargo_ = cargo.Cargo(draft_,quality_, crew_)
  assert cargo_.is_worth_it()

def test_positivo_cargo(draft_,quality_, crew_):
  cargo_ = cargo.Cargo(draft_,quality_ ,crew_)
  assert cargo_.is_worth_it()

def test_negativo_cruise(passengers_, draft_,crew_):
  crucero = cruise.Cruise(passengers_, draft_, crew_)
  assert crucero.is_worth_it()

def test_positivo_cruise(passengers_,draft_,crew_):
  crucero = cruise.Cruise(passengers_, draft_,crew_)
  assert crucero.is_worth_it()


"""
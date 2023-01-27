from abc import ABC

from serviceable import Serviceable
from engine import Engine
from battery import Battery

class Car(Serviceable, ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery


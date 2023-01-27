from abc import ABC

from ..car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        if self.warning_light_on:
            return True
        else:
            return False

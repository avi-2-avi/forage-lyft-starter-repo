from abc import ABC
from car import Car
from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class CarFactory(ABC):
    """
    Creator class for cars
    """
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(current_date, last_service_date))

    @staticmethod
    def create_glissage(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(current_date, last_service_date))

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(current_date, last_service_date))

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(current_date, last_service_date))

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(current_date, last_service_date))

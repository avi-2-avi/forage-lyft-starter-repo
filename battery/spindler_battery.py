from abc import ABC
from datetime import datetime, date
from battery import Battery

class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.needs_service():
            return True
        else:
            return False
         


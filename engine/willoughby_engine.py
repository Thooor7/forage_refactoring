from abc import ABC

from car import Car


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int) -> None:
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        pass

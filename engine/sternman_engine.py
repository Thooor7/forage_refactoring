from abc import ABC

from car import Car


class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool) -> None:
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        pass

from abc import ABC, abstractmethod

class Battery(Serviceable):
    def needs_service(self) -> bool:
        pass
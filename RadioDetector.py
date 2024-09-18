from abc import ABC, abstractmethod

class RadioDetector(ABC):
    @abstractmethod
    def detect_radios(self):
        pass

    @abstractmethod
    def is_radio(self, description: str) -> bool:
        pass

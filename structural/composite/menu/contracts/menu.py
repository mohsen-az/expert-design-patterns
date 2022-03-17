from abc import ABC, abstractmethod


class Menu(ABC):

    @abstractmethod
    def build(self):
        pass

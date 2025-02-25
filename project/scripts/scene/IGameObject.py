from .__init__ import *

from abc import abstractmethod
from typing import Iterable

from scripts.window.interface.IDrawble import IDrawble


class IGameObject(IDrawble):
    @abstractmethod
    def mechanics(self) -> Iterable[InteractiveMechanic]:
        pass


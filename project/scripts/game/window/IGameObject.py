from abc import abstractmethod
from typing import Iterable

from pygame import Surface

from scripts.game.mechanics.interactives.IntreactiveMechanic import InteractiveMechanic

from scripts.game.window.IDrawble import IDrawble


class IGameObject(IDrawble):
    @abstractmethod
    def mechanics(self) -> Iterable[InteractiveMechanic]:
        pass


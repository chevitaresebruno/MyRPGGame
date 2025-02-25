from abc import ABC, abstractmethod

from pygame.event import Event

from scripts.game.events.ILodable import ILoadable
from scripts.game.events.EventCartridge import EventCartridge


class InteractiveMechanic(ABC):
    def __init__(self):
        ABC.__init__(self)
    
    @abstractmethod
    def toLoad(self, event: Event) -> list[EventCartridge]:
        pass

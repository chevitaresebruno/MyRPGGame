from .__init__ import *

from typing import Iterable

from .EventCartridge import EventCartridge


class ILoadable(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def toLoad(self) -> EventCartridge | Iterable[EventCartridge]:
        pass


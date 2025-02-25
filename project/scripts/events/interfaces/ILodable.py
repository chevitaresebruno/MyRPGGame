from .. import *

from typing import Iterable

from ..EventCartridge import EventCartridge


class ILoadable(ABC):
    def __init__(self):
        ABC.__init__(self)

    @abstractmethod
    def toLoad(self) -> EventCartridge | Iterable[EventCartridge]:
        pass


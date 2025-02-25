from .. import *

from ..interfaces.ILodable import ILoadable
from ..EventCartridge import EventCartridge


class ExitAction(ILoadable):
    def __init__(self):
        self.infinityLoop: bool = True

    def __exit(self, event: Event) -> None:
        self.infinityLoop = False

    def toLoad(self) -> EventCartridge:
        return EventCartridge(self.__exit, QUIT)
    

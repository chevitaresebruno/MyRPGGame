from .__init__ import *

from .Action import Action


class EventCartridge:
    def __init__(self, do: IInteractiveFunction, kind: int):
        self.action: Action = Action(do)
        self.kind: int = kind
        

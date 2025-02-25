import pygame
from pygame.event import Event, get

from scripts.game.mechanics.interactives.IntreactiveMechanic import InteractiveMechanic

from .Action import Action
from .EventCartridge import EventCartridge


class EventController:
    def __init__(self):
        self.e: Event = None
        self.quit: list[Action] = list()
        self.kdown: list[Action] = list()
        self.kup: list[Action] = list()

    def loop(self):
        for self.e in get():
            match self.e.type:
                case pygame.QUIT:
                    for ev in self.quit:
                        ev.do(self.e)
                case pygame.KEYDOWN:
                    for ev in self.kdown:
                        ev.do(self.e)
                case pygame.KEYUP:
                    for ev in self.kup:
                        ev.do(self.e)

    def loadEvent(self, cartrigde: EventCartridge) -> None:
        match cartrigde.kind:
            case pygame.QUIT:
                self.quit.append(cartrigde.action)
            case pygame.KEYDOWN:
                self.kdown.append(cartrigde.action)
            case pygame.KEYUP:
                self.kup.append(cartrigde.action)

    def loadEvents(self, cartrigdes: list[EventCartridge]) -> None:
        for cartrigde in cartrigdes:
            self.loadEvent(cartrigde)

    def loadMechanic(self, mechanic: InteractiveMechanic) -> None:
        events = mechanic.toLoad()

        if(iter(events)):
            self.loadEvents(events)
        else:    
            self.loadEvent(events)

    def loadMechanics(self, mechanics: list[InteractiveMechanic]) -> None:
        for mechanic in mechanics:
            self.loadMechanic(mechanic)


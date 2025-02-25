import pygame
from pygame import Rect
from pygame.event import Event
from pygame.math import Vector2

from scripts.game.events.EventCartridge import EventCartridge
from scripts.game.mechanics.interactives.IntreactiveMechanic import InteractiveMechanic
from scripts.game.mechanics.statics.RigidyBody import RigidyBody


class TopDownMovement(RigidyBody):
    def __init__(self):
        RigidyBody.__init__(self)

    def __move(self, event: Event) -> None:
        match event.key:
            case pygame.K_w:
                self.move(Vector2(0, -1))
            case pygame.K_s:
                self.move(Vector2(0, 1))
            case pygame.K_a:
                self.move(Vector2(-1, 0))
            case pygame.K_d:
                self.move(Vector2(1, 0))

    def __stop(self, event: Event) -> None:
        match event.key:
            case pygame.K_w:
                self.move(Vector2(0, 0))
            case pygame.K_s:
                self.move(Vector2(0, 0))
            case pygame.K_a:
                self.move(Vector2(0, 0))
            case pygame.K_d:
                self.move(Vector2(0, 0))

    def toLoad(self) -> tuple[EventCartridge]:
        return EventCartridge(self.__move, pygame.KEYDOWN), EventCartridge(self.__stop, pygame.KEYUP)


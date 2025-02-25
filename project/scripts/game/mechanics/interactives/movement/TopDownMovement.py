import pygame
from pygame import Rect
from pygame.event import Event
from pygame.math import Vector2

from scripts.game.events.EventCartridge import EventCartridge
from scripts.game.mechanics.interactives.IntreactiveMechanic import InteractiveMechanic
from scripts.game.mechanics.statics.RigidyBody import RigidyBody


class TopDownMovement:
    def __init__(self, startPos: tuple[int]):
        self.__rigidyBody: RigidyBody = RigidyBody(Rect((0, 0, 0, 0)))
        self.__rigidyBody.move(Vector2(startPos))

    def move(self, event: Event) -> None:
        match event.key:
            case pygame.K_w:
                self.__move(Vector2(0, -1))
            case pygame.K_s:
                self.__move(Vector2(0, 1))
            case pygame.K_a:
                self.__move(Vector2(-1, 0))
            case pygame.K_d:
                self.__move(Vector2(1, 0))

    def stop(self, event: Event) -> None:
        match event.key:
            case pygame.K_w:
                self.__move(Vector2(0, 0))
            case pygame.K_s:
                self.__move(Vector2(0, 0))
            case pygame.K_a:
                self.__move(Vector2(0, 0))
            case pygame.K_d:
                self.__move(Vector2(0, 0))

    def toLoad(self) -> tuple[EventCartridge]:
        return EventCartridge(self.move, pygame.KEYDOWN), EventCartridge(self.stop, pygame.KEYUP)

    def __move(self, vector: Vector2):
        self.__rigidyBody.move(vector)


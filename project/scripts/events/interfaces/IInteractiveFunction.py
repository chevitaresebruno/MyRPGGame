from typing import Callable

from pygame.event import EventType


IInteractiveFunction = Callable[[object, EventType], None]


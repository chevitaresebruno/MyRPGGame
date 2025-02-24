from pygame.time import Clock


class Ticker:
    def __init__(self, fps: int):
        self.__clock = Clock()
        self.__fps = fps
    
    def update(self) -> None:
        self.__clock.tick(self.__fps)
        
        
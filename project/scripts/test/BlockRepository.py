from pygame.surface import Surface

from scripts.tools.Colors import *
from scripts.sprite.Repository import Repository

from .BlockImage import BlockImage
from .BlockStates import BlockStates


class BlockRepository(Repository):
    def __init__(self):
        super().__init__()
        self.rgb: tuple[Surface] = (BlockImage.build(RED, (20, 20)), BlockImage.build(GREEN, (20, 20)), BlockImage.build(BLUE, (20, 20)))
        self.cmyk: tuple[Surface] = (BlockImage.build(CYAN, (20, 20)), BlockImage.build(MAGENTA, (20, 20)), BlockImage.build(YELLOW, (20, 20)), BlockImage.build(BLACK, (20, 20)))
        
    def getBase(self) -> tuple[Surface]:
        return self.rgb
    
    def getFirst(self) -> Surface:
        return self.rgb[0]
        
    def getByState(self, state: BlockStates) -> tuple[Surface] | None:
        match(state):
            case BlockStates.RGB:
                return self.rgb
            case BlockStates.CMYK:
                return self.cmyk
            
        return None
    
    
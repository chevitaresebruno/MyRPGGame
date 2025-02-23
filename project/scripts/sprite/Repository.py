from .__init__ import *


class Repository(ABC):
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def getBase(self) -> tuple[Surface]:
        pass
    
    @abstractmethod
    def getFirst(self) -> Surface:
        pass
    
    @abstractmethod
    def getByState(self, state: Enum) -> tuple[Surface]:
        pass
    
    def timeUpdate(self, state: Enum) -> int:
        return int((1/state.value)*1000)
    
    
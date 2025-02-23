from time import time


class Timer:
    def __init__(self, increment: int):
        self.__increment: int = increment
        self.__next: int = increment
        
    def canUpdate(self) -> bool:
        if(Timer.__milisecond() > self.__next):        
            self.__next = Timer.__milisecond() + self.__increment
            return True
        
        return False
    
    def reset(self):
        self.__next == time()
    
    @staticmethod
    def __milisecond() -> int:
        return int(time())*1000
    
    
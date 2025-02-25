from .__init__ import *

from .LayerObject import LayerObject


class Layer:
    def __init__(self):
        self.__first: LayerObject = None
        self.__last: LayerObject = None
        self.__size: int = 0
    
    def add(self, obj: IDrawble) -> None:
        if(self.__size == 0):
            self.__first = LayerObject(obj)
            self.__last = self.__first
        else:
            self.__last.next = LayerObject(obj)
            self.__last = self.__last.next
        self.__size += 1

    def __len__(self) -> int:
        return self.__size

    def __iter__(self):
        current = self.__first
        while current:
            yield current.obj
            current = current.next
            
        
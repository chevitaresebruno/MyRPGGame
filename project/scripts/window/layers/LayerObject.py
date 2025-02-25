from .__init__ import *


class LayerObject:
    def __init__(self, obj: IDrawble):
        self.obj: IDrawble = obj
        self.next: LayerObject = None


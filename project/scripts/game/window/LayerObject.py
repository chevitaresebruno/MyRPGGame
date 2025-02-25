from .IDrawble import IDrawble


class LayerObject:
    def __init__(self, obj: IDrawble):
        self.obj: IDrawble = obj
        self.next: LayerObject = None


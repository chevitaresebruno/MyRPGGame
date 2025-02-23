from pygame import Color, Surface


class BlockImage:
    @staticmethod
    def build(color: Color, size: tuple):
        image = Surface(size)
        image.fill(color)
        
        return image
    
    
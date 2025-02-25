from __init__ import *

from scripts.game.Game import Game
from scripts.tools.SceneLoader import SceneLoader


def main() -> int:
    Game.init()
    
    game = Game(60, (200, 200))
    game.load(SceneLoader.loadFromXml(SCENES_DIR / "test.xml"))
    
    game.mainLoop()

    Game.end()

if __name__ == "__main__":
    main()
    
    
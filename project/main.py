from __init__ import *


def main() -> int:
    pg.init()
    
    window = pg.display.set_mode((200, 200))
    
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()
                
        window.fill((20, 20, 20))
        pg.display.flip()
                

if __name__ == "__main__":
    main()
    
    
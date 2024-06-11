import random
import pygame as pg


# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)
BLAWG_IMAGE = pg.image.load("./Images/blawg.jpeg")

BLAWG_IMAGE_IMAGE_SMALL = pg.transform.scale(
    BLAWG_IMAGE, (BLAWG_IMAGE.get_width() // 2, BLAWG_IMAGE.get_height() // 2)
)


class Blocks(pg.sprite.Sprite):
    def __init__(self, height: int):
        super().__init__()

        self.image = pg.image.load("./Images/blawg.jpeg")

        # Scale the image down
        self.image = pg.transform.scale(
        self.image, (self.image.get_width() // 2, self.image.get_height() // 2)
    )

        self.rect = self.image.get_rect()
        self.rect.top = height
        self.vel_x = 10

    def update(self):
        self.rect.x += self.vel_x


        # Bounce off the edge of the screen0.

        if self.rect.left < 0:
            self.rect.left = 0
            self.vel_x *= -1
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vel_x *= -1


   




def start():
    times_clicked = 0
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group

    score = 0
    level = 0
    font = pg.font.SysFont("Futura", 24)

    all_sprites = pg.sprite.Group()
    blawgs = pg.sprite.Group()
    stopped_blawgs = pg.sprite.Group()

    pg.display.set_caption("Stack up!")


    block = Blocks(640)
    all_sprites.add(block)
    blawgs.add(block)

    # --Main Loop--
    while not done:

        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                times_clicked += 1

                if len(stopped_blawgs) == 0:
                    for block in blawgs:
                        block.vel_x = 0
                        blawgs.remove(block)

                        stopped_blawgs.add(block)

                        block = Blocks(640-(80*(times_clicked)))
                        all_sprites.add(block)
                        blawgs.add(block)
                        score += 1
                else:
                    for block in blawgs:
                        stacked_blocks = pg.sprite.spritecollide(block, stopped_blawgs, False)

                    if stacked_blocks:
                        # Creates a new block 

                        block.vel_x = 0
                        blawgs.remove(block)
                        stopped_blawgs.add(block)

                        block = Blocks(640-(80*(times_clicked)))
                        all_sprites.add(block)
                        blawgs.add(block)

                        # get Score
                        score += 1
                        print(f"Your score is: {score}")
                    else:
                        print(f"You Lost! Your score was {score}")
                        pg.quit()
                        
                



                if times_clicked == 9:
                    times_clicked = 0
                    all_sprites.empty()
                    stopped_blawgs.empty()

                    block = Blocks(640)
                    all_sprites.add(block)
                    blawgs.add(block)


                




            

                            


                
        # --- Update the world  state
        # Update the state of all sprites
        all_sprites.update()

        # for block in blawgs:
        #     print(block.vel_x, end=" ")
        #     print()   


        

        # --- Draw items
        screen.fill(WHITE)

        # Draw all the sprites
        score_image = font.render(f"Score: {score}", True, BLACK)

        all_sprites.draw(screen)


        screen.blit(score_image, (5, 5))

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()
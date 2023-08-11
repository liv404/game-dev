import pygame
import csv
import random


def main():
    pygame.init()
    display_width = 1280
    display_height = 720

    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Magic 8 Ball - liv's version")
    font = pygame.font.Font('Signlode.ttf', 100)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    screen.fill(WHITE)
    pygame.display.flip()

    magic_ball = Magic_Ball(490, 210)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(magic_ball)

    running = True
    clock = pygame.time.Clock()
    display_text = None  # To hold the text to be displayed

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display_text = get_phrase()  # Get the text to be displayed

        all_sprites.update()

        screen.fill(WHITE)
        all_sprites.draw(screen)

        if display_text is not None:
            text = font.render(str(display_text), True, BLACK)
            textRect = text.get_rect()
            textRect.center = (display_width / 2, 120)
            screen.blit(text, textRect)  # Render the text on the screen

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

class Magic_Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/8.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def get_phrase():
    with open ("responses.csv") as responses:
        reader = csv.reader(responses)
        rows = list(reader)
        index = random.randint(0, 19)
        answer = rows[index]
        return answer[0]

if __name__ == "__main__":

    main()
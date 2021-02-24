import pygame
pygame.init()

colors = {'red': (255, 100, 100)}


class window:
    def __init__(self, width=600, height=600, title='BlockGame Window'):
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.width = width
        self.height = height
        self.clicked = 0

    def run(self):
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.clicked = 1
            elif event.type == pygame.MOUSEBUTTONUP:
                self.clicked = 0

    def rect(self, x, y, width, height, color):
        pygame.draw.rect(self.window, color if colors[color] in colors else color, (x + width / 2 + self.width / 2, y + height / 2 + self.height / 2))

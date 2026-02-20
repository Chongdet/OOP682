import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("pygame 01")
running = True
while running:
    pygame.time.delay(100)
    pygame.display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
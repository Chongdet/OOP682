import pygame
pygame.init()
game_icon = pygame.image.load('image/my_icon.png')
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("pygame 01")
pygame.display.set_icon(game_icon)
running = True
sara = pygame.image.load('image/sara.png')
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(120)
    screen.fill((255, 255, 255))  # Fill screen with white color
    font = pygame.font.SysFont("knit", 36)
    text = font.render(f"FPS: {clock.get_fps():.2f}", True, (0, 0, 0))
    screen.blit(sara, (50, 50))
    screen.blit(text, (300, 230))
    pygame.display.update()

pygame.display.flip()
pygame.quit()
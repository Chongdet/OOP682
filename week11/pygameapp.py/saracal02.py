import pygame
pygame.init()
game_icon = pygame.image.load('image/my_icon.png')
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("pygame 01")
pygame.display.set_icon(game_icon)
running = True
sara_sheet = pygame.image.load('image/sara.png')
sara_ract = pygame.Rect(0, 0, 34, 56)
sara_pos = pygame.Rect(50, 50, 34, 56)
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and sara_pos.x > 0:
        sara_pos.x -= 5
    elif key[pygame.K_RIGHT] and sara_pos.x + sara_ract.width < 400 :
        sara_pos.x += 5
    elif key[pygame.K_UP] and sara_pos.y > 0:
        sara_pos.y -= 5
    elif key[pygame.K_DOWN] and sara_pos.y + sara_ract.height < 300 :
        sara_pos.y += 5
    clock.tick(144)
    screen.fill((255, 255, 255))  # Fill screen with white color
    font = pygame.font.SysFont("knit", 36)
    text = font.render(f"FPS: {clock.get_fps():.2f}", True, (0, 0, 0))
    screen.blit(sara_sheet, sara_pos, sara_ract)
    screen.blit(text, (260, 10))
    pygame.display.update()

pygame.display.flip()
pygame.quit()
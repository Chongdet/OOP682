import sys, os
import pygame
from chars.sara import Hero

class Saraadventure(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        try:
            self.icon = pygame.image.load("image/my_icon.png")
            pygame.display.set_icon(self.icon)
        except:
            pass
        self.caption = "Sara's Adventure"
        self.font = pygame.font.SysFont("knit", 30)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.caption)
        self.running = True
        self.hero = Hero("Sara", "image/sara.png", 50, 50)

    def headle_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

    def drow_text(self, text, position, color=(0, 0, 0)):
        font = self.font
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, position)
    
    def headle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.hero.left()
        if keys[pygame.K_RIGHT]:
            self.hero.right()
        if keys[pygame.K_UP]:
            self.hero.up()
        if keys[pygame.K_DOWN]:
            self.hero.down()

    def start(self):
        self.start_time = pygame.time.get_ticks()
        elapsed_time = 0
        while self.running:
            # คำนวณเวลาที่ผ่านไป (มิลลิวินาที)
            elapsed_time = pygame.time.get_ticks() - self.start_time
            self.headle_close()
            self.screen.fill((255, 255, 255))  # White background
            # ส่ง elapsed_time เข้าไปให้ Hero จัดการ
            self.hero.update(elapsed_time) 
            self.hero.draw(self.screen)
            self.drow_text("Welcome to Sara's Adventure!", (50, 20))
            self.clock.tick(144)
            self.headle_input()
            pygame.display.flip()

if __name__ == "__main__":
    game = Saraadventure()
    game.start()
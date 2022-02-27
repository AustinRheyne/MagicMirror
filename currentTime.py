import pygame
from datetime import datetime

class CurrentTime:
    def __init__(self, screen):
        self.font = pygame.font.SysFont('calibri', 200)
        self.text = self.font.render(datetime.now().strftime("%H:%M:%S"), False, (255, 255, 255))
        self.rect = self.text.get_rect()
        self.screen = screen

    def update(self):
        self.text = self.font.render(datetime.now().strftime("%H:%M:%S"), False, (255, 255, 255))
        self.text = pygame.transform.rotate(self.text, 90)
        self.rect = self.text.get_rect()
        self.rect.centery = self.screen.get_rect().centery
        self.blit_me()

    def blit_me(self):
        self.screen.blit(self.text, self.rect)
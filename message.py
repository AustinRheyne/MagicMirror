import pygame
import json
import datetime
class Message:
    def __init__(self, screen):
        h = screen.get_height()
        self.currentMessage = "Don't forget to drink some water!"
        self.font = pygame.font.SysFont('calibri', int((2000*h/1080)/len(self.currentMessage)))
        self.text = self.font.render(self.currentMessage, False, (255, 255, 255))
        self.rect = self.text.get_rect()
        self.screen = screen

    def update(self):
        self.text = self.font.render(self.currentMessage, False, (255, 255, 255))
        self.text = pygame.transform.rotate(self.text, 90)
        self.rect = self.text.get_rect()
        self.rect.centery = self.screen.get_rect().centery
        self.rect.right = self.screen.get_rect().right - 20
        self.blit_me()

    def blit_me(self):
        self.screen.blit(self.text, self.rect)
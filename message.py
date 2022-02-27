import pygame
import json
from datetime import datetime
import random
class Message:
    def __init__(self, screen):
        with open('goodDay.json', "r") as f:
            data = json.load(f)

        if int(datetime.now().strftime("%H")) > 12:
            self.currentMessage = random.choice(data["Night"])
        else:
            self.currentMessage = random.choice(data["Morning"])

        h = screen.get_height()
        self.font = pygame.font.SysFont('calibri', int((2000*h/1080)/len(self.currentMessage)))
        self.text = self.font.render(self.currentMessage, True, (255, 255, 255))
        self.text = pygame.transform.rotate(self.text, 90)
        self.rect = self.text.get_rect()
        self.rect.centery = self.screen.get_rect().centery
        self.rect.right = self.screen.get_rect().right - 20
        self.screen = screen

    def update(self):
        self.blit_me()

    def blit_me(self):
        self.screen.blit(self.text, self.rect)
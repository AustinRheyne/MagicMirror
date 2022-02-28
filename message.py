import pygame
import json
from datetime import datetime
import time
import random
class Message:
    def __init__(self, screen):
        with open('goodDay.json', "r") as f:
            self.data = json.load(f)

        if int(datetime.now().strftime("%H")) > 12:
            self.currentMessage = random.choice(self.data["Night"])
        else:
            self.currentMessage = random.choice(self.data["Morning"])

        h = screen.get_height()
        self.screen = screen
        self.font = pygame.font.SysFont('calibri', int((2000*h/1080)/len(self.currentMessage)))
        self.text = self.font.render(self.currentMessage, True, (255, 255, 255))
        self.text = pygame.transform.rotate(self.text, 90)
        self.rect = self.text.get_rect()
        self.rect.centery = self.screen.get_rect().centery
        self.rect.right = self.screen.get_rect().right - 20

        self.last_updated_message = time.time()
        self.message_frequency = 10 # This is in seconds

    def update(self):
        if time.time() - self.last_updated_message >= self.message_frequency:
            print("updating!")
            self.last_updated_message = time.time()
            new_msg = self.currentMessage
            while new_msg == self.currentMessage:
                if int(datetime.now().strftime("%H")) > 12:
                    new_msg = random.choice(self.data["Night"])
                else:
                    new_msg = random.choice(self.data["Morning"])
            self.currentMessage = new_msg
            h = self.screen.get_height()
            self.font = pygame.font.SysFont('calibri', int((2000 * h / 1080) / len(self.currentMessage)))
            self.text = self.font.render(self.currentMessage, True, (255, 255, 255))
            self.text = pygame.transform.rotate(self.text, 90)
            self.rect = self.text.get_rect()
            self.rect.centery = self.screen.get_rect().centery
            self.rect.right = self.screen.get_rect().right - 20

        self.blit_me()

    def blit_me(self):
        self.screen.blit(self.text, self.rect)
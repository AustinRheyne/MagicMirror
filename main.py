import pygame
from currentTime import CurrentTime
from message import Message

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

time = CurrentTime(screen)
msg = Message(screen)
def eventLoop():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

while True:
    eventLoop()
    screen.fill((0,0,0))

    msg.update()
    time.update()

    pygame.display.flip()
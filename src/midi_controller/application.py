import pygame
from pygame import midi
import logging
from logging import getLogger


logger = getLogger(__name__)
logging.basicConfig(filename=__name__+'.log', encoding='utf-8', level=logging.DEBUG)


def main() -> None:
    pygame.init()
    pygame.midi.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((1280, 720))
    running = True
    while running:
        window.fill("black")
        running = tick()
        pygame.display.update()
        clock.tick(60)


def midi() -> None:
    device = pygame.midi.Input(1)
    print(device.read(3))


def tick() -> bool:
    if pygame.event.peek(pygame.QUIT):
        pygame.midi.quit()
        return False

    # Handle midi events
    midi()

    # Handle game events
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    return True

if __name__ == "__main__":
    main()

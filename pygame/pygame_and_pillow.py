def hide_initial_pygame_message():
    from os import environ
    if 'PYGAME_HIDE_SUPPORT_PROMPT' not in environ:
        environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''
    del environ


hide_initial_pygame_message()  # to hide the initial pygame message

import PIL
from PIL import Image
import pygame


def image_pill2pygame(image):
    data = image.tobytes()
    size = image.size
    mode = image.mode
    return pygame.image.fromstring(data, size, mode)


def image_pygame2pill(image, mode):
    data = pygame.image.tostring(image, mode)
    size = image.get_size()
    return PIL.Image.frombytes(mode, size, data)

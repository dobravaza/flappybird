import random
import pygame
class Pipe:
    def __init__(self, screen_width, screen_height, gap_size, pipe_top_image, pipe_bottom_image):
        self.screen_width = screen_width
        self.gap_start = random.randint(50, screen_height - 50 - gap_size)  # 50 jest marginesem od góry i dołu ekranu
        # self.pipe_top_image = pygame.transform.flip(pipe_top_image, False, True)

        self.gap_size = gap_size
        self.width = pipe_top_image.get_width()
        self.height = pipe_top_image.get_height()
        self.x = screen_width
        self.pipe_top_image = pipe_top_image
        self.pipe_bottom_image = pipe_bottom_image

    def move(self, speed):
        self.x -= speed

    def off_screen(self):
        return self.x + self.width < 0

    def draw(self, screen):
        screen.blit(self.pipe_top_image, (self.x, self.gap_start - self.height))
        screen.blit(self.pipe_bottom_image, (self.x, self.gap_start + self.gap_size))

    def get_top_rect(self):
        return pygame.Rect(self.x, 0, self.width, self.gap_start)

    def get_bottom_rect(self):
        return pygame.Rect(self.x, self.gap_start + self.gap_size, self.width,
                           self.height - (self.gap_start + self.gap_size))


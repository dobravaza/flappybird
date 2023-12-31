import pygame


class Player:
    def __init__(self, x, y, player_image, player_falling,player_jumping):
        self.pos = pygame.Vector2(x, y)
        self.falling_image = pygame.image.load(player_falling)
        self.flying_image = pygame.image.load(player_image)
        self.jumping_image = pygame.image.load(player_jumping)
        width = int(self.flying_image.get_width() * 1)
        height = int(self.flying_image.get_height() * 1)
        self.flying_image = pygame.transform.scale(self.flying_image, (width, height))
        self.falling_image = pygame.transform.scale(self.falling_image, (width, height))

        self.current_image = self.flying_image
        width = int(self.current_image.get_width() * 1)
        height = int(self.current_image.get_height() * 1)
        self.current_image = pygame.transform.scale(self.current_image, (width, height))
        self.velocity = 0.5
        self.gravity = 1.5
        self.jump_power = -10

    def get_rect(self):
        return pygame.Rect(self.pos.x, self.pos.y, self.current_image.get_width(), self.current_image.get_height())

    def update(self, dt, screen_height):
        """Aktualizacja pozycji gracza"""
        self.velocity += self.gravity * dt
        self.pos.y += self.velocity * dt


        if self.pos.y < 0:
            self.pos.y = 0
            self.velocity = 0

        elif self.pos.y > screen_height:
            self.pos.y = screen_height


        if self.velocity > 0:

            self.current_image = self.falling_image
        else:
            self.current_image = self.flying_image

    def jump(self):
        self.velocity += self.jump_power



    def draw(self, screen):
        screen.blit(self.current_image,
                    (self.pos.x - self.current_image.get_width() / 2, self.pos.y - self.current_image.get_height() / 2))

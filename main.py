# Przykładowy plik prezentujący podstawową pętlę gry w pygame
import pygame
from Player import Player
# Inicjalizacja pygame
pygame.init()
screen = pygame.display.set_mode((1280, 600))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont(None, 36)
watermark_text = font.render("@dobravaza", True, (0,0,0))

#tło
background_image = pygame.image.load("assets/bg_main.jpg")
# player_falling = pygame.image.load("assets/yellowbird-downflap.png")
# player_image = pygame.image.load("assets/yellowbird-midflap.png")

#klasa player
PLAYER_STARTING_X_POS = 50
PLAYER_STARTING_Y_POS = screen.get_height() / 2
player = Player(PLAYER_STARTING_X_POS, PLAYER_STARTING_Y_POS, "assets/yellowbird-midflap.png", "assets/yellowbird-downflap.png", player_jumping="assets/yellowbird-upflap.png")

while running:
    # sprawdź zdarzenia
    # zdarzenie pygame.QUIT oznacza, że użytkownik kliknął X, aby zamknąć okno
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    #rysuj tło
    screen.blit(background_image, (0,0))

    time_passed = clock.tick(60)
    dt = time_passed / 50.0
    player.draw(screen)
    player.update(dt, screen.get_height())

    screen.blit(watermark_text, (10, screen.get_height() - watermark_text.get_height() - 10))
    pygame.display.flip()

pygame.quit()

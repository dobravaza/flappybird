# Przykładowy plik prezentujący podstawową pętlę gry w pygame
import pygame
from Player import Player
from Pipe import Pipe
# Inicjalizacja pygame
pygame.init()
screen = pygame.display.set_mode((1280, 600))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont(None, 36)
watermark_text = font.render("@dobravaza", True, (0,0,0))

#tło
background_image = pygame.image.load("assets/bg_main.jpg")
#rureczki
pipe_top_image = pygame.image.load("assets/pipe-green.png")
pipe_bottom_image = pygame.image.load("assets/pipe-green.png")

#screen
screen_widht = screen.get_width()
screen_height = screen.get_height()


#gap
gap_size = 150
#klasa player
PLAYER_STARTING_X_POS = 200
PLAYER_STARTING_Y_POS = screen.get_height() / 2
player = Player(PLAYER_STARTING_X_POS, PLAYER_STARTING_Y_POS, "assets/yellowbird-midflap.png", "assets/yellowbird-downflap.png", player_jumping="assets/yellowbird-upflap.png")



#testing
pipes = []
frame_count = 0
#tesing

while running:
    # sprawdź zdarzenia
    # zdarzenie pygame.QUIT oznacza, że użytkownik kliknął X, aby zamknąć okno
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
    screen.blit(background_image, (0,0))
    #testing
    frame_count += 0.5

    if frame_count % 180 == 0:
        new_pipe = Pipe(screen_widht, screen_height, gap_size, pipe_top_image, pipe_bottom_image)
        pipes.append(new_pipe)
        new_pipe.move(5)
        new_pipe.draw(screen)

    for pipe in pipes:

        pipe.move(5)
        pipe.draw(screen)
    for pipe in pipes:
        if player.get_rect().colliderect(pipe.get_top_rect()) or player.get_rect().colliderect(pipe.get_bottom_rect()):
            print("Kolizja!")

    pipes = [pipe for pipe in pipes if not pipe.off_screen()]




    time_passed = clock.tick(60)
    dt = time_passed / 50.0
    player.draw(screen)
    player.update(dt, screen.get_height())

    screen.blit(watermark_text, (10, screen.get_height() - watermark_text.get_height() - 10))
    pygame.display.flip()

pygame.quit()

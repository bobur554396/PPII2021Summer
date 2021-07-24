import pygame

# Initialize pygame program
pygame.init()

# Surface
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("First game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True

color = BLUE

# Main loop
while running:
  # Event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        # if color == BLUE:
        #   color = RED
        # else:
        #   color = BLUE
        color = RED if color == BLUE else BLUE

  screen.fill(WHITE)

  pygame.draw.rect(screen, color, (100, 100, 150, 150))


  pygame.display.flip()


pygame.quit()

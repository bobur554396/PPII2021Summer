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

clock = pygame.time.Clock()
FPS = 60
# Frames Per Second

x, y = 100, 100

# Main loop
while running:
  # Event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        color = RED if color == BLUE else BLUE
      # if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
      if event.key in [pygame.K_RIGHT, pygame.K_d]:
        x += 10
      if event.key in [pygame.K_LEFT, pygame.K_a]:
        x -= 10
      if event.key in [pygame.K_UP, pygame.K_w]:
        y -= 10
      if event.key in [pygame.K_DOWN, pygame.K_s]:
        y += 10


  screen.fill(WHITE)

  pygame.draw.rect(screen, color, (x, y, 100, 100))

  pygame.display.flip()

  clock.tick(FPS)


pygame.quit()

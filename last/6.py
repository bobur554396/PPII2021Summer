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

x, y = 200, 20
dx, dy = 5, 5

# Main loop
while running:
  # Event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        color = RED if color == BLUE else BLUE

  pressed = pygame.key.get_pressed()

  if pressed[pygame.K_RIGHT]: x += dx
  if pressed[pygame.K_LEFT]: x -= dx
  if pressed[pygame.K_UP]: y -= dy
  if pressed[pygame.K_DOWN]: y += dy


  screen.fill(WHITE)
  
  pygame.draw.rect(screen, color, (x, y, 100, 100))

  pygame.display.flip()

  clock.tick(FPS)


pygame.quit()

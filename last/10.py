import pygame
import random

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

clock = pygame.time.Clock()
# Frames Per Second
FPS = 5

color = GREEN
block = 15
dx, dy = block, 0
radius = 10

food_location = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)

body = [[70, 100], [85, 100], [100, 100]]
# Init
# 1) [70, 100], [85, 100], [100, 100]

# Moving to the right
# 2) [85, 100], [100, 100], [115, 100]

# Moving to the right
# 2) [100, 100], [115, 100], [130, 100]


# Moving to the down
# 3) [100, 100], [115, 100], [115, 115]

# Main loop
while running:
  # Event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        body.append([0, 0])
        food_location = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
      if event.key == pygame.K_RIGHT:
        dx, dy = block, 0
      if event.key == pygame.K_LEFT:
        dx, dy = -block, 0
      if event.key == pygame.K_UP:
        dx, dy = 0, -block
      if event.key == pygame.K_DOWN:
        dx, dy = 0, block

  # Move our snake
  for i in range(len(body) - 1, 0, -1):
    body[i][0] = body[i - 1][0] # x - point
    body[i][1] = body[i - 1][1] # y - point

  body[0][0] += dx
  body[0][1] += dy

  if body[0][0] >= SCREEN_WIDTH:
    body[0][0] = 0

  if body[0][1] >= SCREEN_HEIGHT:
    body[0][1] = 0

  # Check for collision head of the snake with food location

  screen.fill(WHITE)

  # Draw food
  pygame.draw.circle(screen, GREEN, food_location, radius)


  # Draw snake
  for i, point in enumerate(body):
    color = RED if i == 0 else BLUE
    pygame.draw.circle(screen, color, point, radius)


  pygame.display.flip()

  clock.tick(FPS)

pygame.quit()

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

# Main loop
while running:
  # Event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  # Game main logic

  # Drawing objects

pygame.quit()

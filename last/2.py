import pygame

# Initialize pygame program
pygame.init()

# Surface
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First game")

# RGB ([0-255], [0-255], [0-255])
#        Red     Green    Blue


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True
PI = 3.14

# Main loop
while running:
  # Event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(WHITE)


  pygame.draw.line(screen, RED, (10, 10), (100, 100), 4)

  pygame.draw.circle(screen, GREEN, (100, 30), 25)
  pygame.draw.circle(screen, GREEN, (170, 30), 25, 3)

  pygame.draw.rect(screen, BLUE, (20, 120, 100, 50))
  pygame.draw.rect(screen, BLUE, (150, 120, 100, 50), 3)

  pygame.draw.ellipse(screen, RED, (270, 30, 100, 50))
  pygame.draw.ellipse(screen, RED, (380, 30, 100, 50), 3)

  pygame.draw.arc(screen, RED, (20, 200, 100, 100), 0, PI / 2, 3)
  pygame.draw.arc(screen, GREEN, (20, 200, 100, 100), PI / 2, PI, 3)
  pygame.draw.arc(screen, BLUE, (20, 200, 100, 100), PI, 3 * PI / 2, 3)
  pygame.draw.arc(screen, BLACK, (20, 200, 100, 100), 3 * PI / 2, 2 * PI, 3)

  pygame.display.flip()
  


pygame.quit()

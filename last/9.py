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
FPS = 60

x, y = 200, 20
dx, dy = 5, 5


class Ball:
  def __init__(self, *args, **kwargs):
    self.size = 50
    self.x = random.randint(0, SCREEN_WIDTH - self.size)
    self.y = random.randint(0, SCREEN_HEIGHT - self.size)
    self.dx = random.randint(-5, 5)
    self.dy = random.randint(-5, 5)
    self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.x + self.size > SCREEN_WIDTH or self.x < 0:
      self.dx *= -1

    if self.y + self.size > SCREEN_HEIGHT or self.y < 0:
      self.dy *= -1

  def draw(self):
    pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.size, self.size))


balls = [Ball()]

# Main loop
while running:
  # Event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        balls.append(Ball())

  for ball in balls:
    ball.move()

  screen.fill(WHITE)

  for ball in balls:
    ball.draw()

  pygame.display.flip()

  clock.tick(FPS)


pygame.quit()

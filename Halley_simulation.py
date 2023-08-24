import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

# Planet colors
PLANET_COLORS = [
    (255, 0, 0),    # Mercury
    (255, 165, 0),  # Venus
    (0, 0, 255),    # Earth
    (255, 255, 0),  # Mars
]

# Constants for planet orbits
ORBIT_RADIUS = [60, 100, 150, 220]  # Radii of orbits for Mercury, Venus, Earth, Mars
ORBIT_SPEED = [0.02, 0.015, 0.01, 0.007]  # Orbital speeds of planets

# Load comet texture
comet_texture = pygame.image.load(r'PATH_TO_TEXTURE')

# Font for labels
font = pygame.font.Font(None, 20)

# Function to calculate planet position
def calculate_planet_position(angle, radius):
    x = WIDTH // 2 + radius * math.cos(angle)
    y = HEIGHT // 2 + radius * math.sin(angle)
    return x, y

clock = pygame.time.Clock()

running = True
angle = 0
comet_x = -20  # Initial position of the comet
comet_y = HEIGHT // 2
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Draw planet orbits
    for radius in ORBIT_RADIUS:
        pygame.draw.circle(screen, GRAY, (WIDTH // 2, HEIGHT // 2), radius, 1)

    # Draw planets and labels
    for i, radius in enumerate(ORBIT_RADIUS):
        planet_x, planet_y = calculate_planet_position(angle * ORBIT_SPEED[i], radius)
        pygame.draw.circle(screen, PLANET_COLORS[i], (int(planet_x), int(planet_y)), 10)

        # Draw planet labels
        planet_label = font.render(f"Planet {i+1}", True, WHITE)
        screen.blit(planet_label, (planet_x - 20, planet_y + 15))

    # Draw comet passing behind the planets
    comet_x += 1  # Adjust the speed of the comet's pass
    pygame.draw.circle(screen, WHITE, (comet_x, comet_y), 5)
    comet_label = font.render("Comet", True, WHITE)
    screen.blit(comet_label, (comet_x + 10, comet_y - 10))

    pygame.display.flip()
    clock.tick(60)

    angle += 0.01  # Adjust the speed of simulation

    if comet_x > WIDTH:
        running = False  # Exit simulation when the comet passes through

pygame.quit()
sys.exit()

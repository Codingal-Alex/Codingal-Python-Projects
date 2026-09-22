import pygame
import random

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# -----------------------------
# Background image
# -----------------------------
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (800, 600))

# -----------------------------
# Sounds
# -----------------------------
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

collision_sound = pygame.mixer.Sound("collision.wav")

# Player
player = pygame.Rect(375, 500, 50, 50)

# Enemies
enemies = []

for i in range(7):
    enemy = pygame.Rect(
        random.randint(0, 750),
        random.randint(0, 300),
        50,
        50
    )
    enemies.append(enemy)

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True

while running:

    # Draw background
    screen.blit(background, (0, 0))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5

    if keys[pygame.K_RIGHT]:
        player.x += 5

    if keys[pygame.K_UP]:
        player.y -= 5

    if keys[pygame.K_DOWN]:
        player.y += 5

    # Keep player inside screen
    if player.left < 0:
        player.left = 0

    if player.right > 800:
        player.right = 800

    if player.top < 0:
        player.top = 0

    if player.bottom > 600:
        player.bottom = 600

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Draw enemies and check collision
    for enemy in enemies:

        pygame.draw.rect(screen, RED, enemy)

        if player.colliderect(enemy):
            score += 1

            # Play collision sound
            collision_sound.play()

            # Move enemy to a new random position
            enemy.x = random.randint(0, 750)
            enemy.y = random.randint(0, 300)

    # Display score
    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()

pygame.quit()

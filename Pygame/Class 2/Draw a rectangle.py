import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Blue Rectangle")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the burple rectangle
    pygame.draw.rect(
        screen,
        (125, 0, 255),
        pygame.Rect(30, 30, 60, 60)
    )

    # Update the display
    pygame.display.flip()

pygame.quit()

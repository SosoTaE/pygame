import pygame
import random

pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.Font(None, 36)  # Use default font, size 36
text_color = (255, 255, 255)  # White
score = 0
score_step = 10

text_surface = font.render(f"Score: {score}", True, text_color)

text_rect = text_surface.get_rect()
text_rect.center = (50, 20)

width = random.randint(10, 50)
height = random.randint(10, 50)

rect_x = (screen_width - width) // 2
rect_y = (screen_height - height) // 2
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

rect = pygame.Rect(rect_x, rect_y, width, height)

# Timer settings
start_time = 10  # Seconds
current_time = start_time
timer_font = pygame.font.Font(None, 48)
timer_color = (255, 0, 0)  # Red

# Time variables
time_elapsed = 0
clock = pygame.time.Clock()

# Run until the user quits
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse click position
            x, y = pygame.mouse.get_pos()

            if rect_x < x and x < rect_x + width and rect_y < y and y < rect_y + height:
                width = random.randint(10, 50)
                height = random.randint(10, 50)
                rect_x = random.randint(0, screen_width - width)
                rect_y = random.randint(0, screen_height - height)
                rect = pygame.Rect(rect_x, rect_y, width, height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                score += 1
                text_surface = font.render(f"Score: {score}", True, text_color)

                # Increase time if score is a multiple of score_step
                if score % score_step == 0:
                    current_time += start_time

    # Update timer
    dt = clock.tick()  # Get time passed since last frame
    time_elapsed += dt
    if time_elapsed >= 1000:  # 1000 milliseconds = 1 second
        current_time -= 1
        time_elapsed = 0

    # Render timer text
    timer_text = timer_font.render(f"Time: {current_time}", True, timer_color)
    timer_rect = timer_text.get_rect()
    timer_rect.center = (screen_width // 2, 20)

    # Game over condition
    if current_time == 0:
        running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    # Draw the rectangle
    pygame.draw.rect(screen, color, rect)

    # Draw the score and timer
    screen.blit(text_surface, text_rect)
    screen.blit(timer_text, timer_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()

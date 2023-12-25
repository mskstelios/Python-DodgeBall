import pygame
import sys
import random

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (211, 211, 211)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

COLOR_LIST = [BLUE, GREEN, RED, GREY]

# Initialization
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Dodge Ball Game')

# Load the background image
background = pygame.image.load('background.jpg').convert()
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))


# Game Class
class Dodge(pygame.sprite.Sprite):
    def __init__(self, x, y, size, radius, color):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.radius = radius
        self.color = color
        self.dx = random.choice([-1, 1]) * random.randint(1, 5)
        self.dy = random.choice([-1, 1]) * random.randint(1, 5)

    def draw(self):
        if self.size == 0:
            pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
        else:
            self.color = random.choice(COLOR_LIST)
            pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))

    def update_position(self, mouse_pos):
        self.x, self.y = mouse_pos

    def movement(self):
        self.x += self.dx
        self.y += self.dy
        if self.y < 0 or self.y > WINDOW_HEIGHT - self.size:
            self.dy *= -1

        if self.x < 0 or self.x > WINDOW_WIDTH - self.size:
            self.dx *= -1

    def check_collision_circle(self, other):
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return distance < self.radius + other.radius

    def check_collision_square(self, other):
        return (
            self.x < other.x + other.size
            and self.x + self.radius > other.x
            and self.y < other.y + other.size
            and self.y + self.radius > other.y
        )


# Function to generate new enemy
def create_enemy():
    new_enemy = Dodge(
        random.randint(0, WINDOW_WIDTH),
        random.randint(0, WINDOW_HEIGHT),
        0, 10,
        random.choice(COLOR_LIST),
    )
    enemies.append(new_enemy)


# Show game over screen
def show_game_over_screen():
    window.fill(BLACK)
    game_over_text = font.render("Game Over", True, YELLOW)
    game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    restart_text = font.render("Press 'R' to Restart", True, WHITE)
    restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
    quit_text = font.render("Press 'Q' to Quit", True, WHITE)
    quit_rect = quit_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
    window.blit(game_over_text, game_over_rect)
    window.blit(restart_text, restart_rect)
    window.blit(quit_text, quit_rect)
    pygame.display.update()


# Show "YOU WON" screen
def show_you_won_screen():
    window.fill(BLACK)
    you_won_text = font.render("YOU WON!", True, GREEN)
    you_won_rect = you_won_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    restart_text = font.render("Press 'R' to Restart", True, WHITE)
    restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
    quit_text = font.render("Press 'Q' to Quit", True, WHITE)
    quit_rect = quit_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
    window.blit(you_won_text, you_won_rect)
    window.blit(restart_text, restart_rect)
    window.blit(quit_text, quit_rect)
    pygame.display.update()


# Start screen to select difficulty level
def start_screen():
    window.fill(BLACK)
    difficulty_text = font.render("Select Difficulty:", True, WHITE)
    difficulty_rect = difficulty_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
    options = [("E", "Easy"), ("M", "Medium"), ("H", "Hard"), ("I", "Impossible")]
    y = WINDOW_HEIGHT // 2
    for key, label in options:
        text = font.render(f"Press '{key}' for {label}", True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, y))
        window.blit(text, text_rect)
        y += 50
    pygame.display.update()


# Create Labels
font = pygame.font.Font(None, 30)

# Import sounds
square_hit_sound = pygame.mixer.Sound('squarel_hit.ogg')
lose_sound = pygame.mixer.Sound('lose_sound.ogg')
win_sound = pygame.mixer.Sound('win_sound.ogg')

# Game Variables
game_over = False
difficulty = None
score = 0
score_number = 10

while True:
    start_screen()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key).upper()
            if key in ["E", "M", "H", "I"]:
                difficulty = key
                score_number = 10 if key == "E" else 7 if key == "M" else 4 if key == "H" else 2

    if difficulty:
        break

# Create Shapes
circle = Dodge(100, 100, 0, 10, WHITE)
square = Dodge(100, 100, 20, 0, RED)
enemies = []


# Create the "To Win" text
to_win_text = font.render("Win = 100", True, YELLOW)
to_win_rect = to_win_text.get_rect(center=(WINDOW_WIDTH // 2, 30))


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if (
            event.type != pygame.QUIT
            and event.type == pygame.KEYDOWN
            and event.key == pygame.K_q
            or event.type == pygame.QUIT
        ):
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            score = 0
            circle.x = 100
            circle.y = 100
            enemies.clear()
            game_over = False

    if not game_over:
        mouse_pos = pygame.mouse.get_pos()
        circle.update_position(mouse_pos)
        window.blit(background, (0, 0))
        if circle.check_collision_square(square):
            square_hit_sound.play()
            score += 1
            square.x = random.randint(0, WINDOW_WIDTH - square.size)
            square.y = random.randint(0, WINDOW_HEIGHT - square.size)
        elif score % score_number == 0 and len(enemies) < score // score_number:
            create_enemy()

        score_text = font.render(f'Score: {score}', True, WHITE)

        window.blit(score_text, (10, 10))
        window.blit(to_win_text, to_win_rect)
        circle.draw()
        square.draw()

        for enemy in enemies:
            enemy.draw()
            enemy.movement()
            if enemy.check_collision_circle(circle):
                lose_sound.play()
                game_over = True
                show_game_over_screen()
                break

        if score == 100:
            win_sound.play()
            game_over = True
            show_you_won_screen()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()

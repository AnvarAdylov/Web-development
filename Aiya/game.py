import pygame
import sys
import random
import os
import math

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Player attributes
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5

# Track attributes
TRACK_WIDTH = SCREEN_WIDTH
TRACK_HEIGHT = 100
TRACK_SPEED = 5

# Object attributes
OBJECT_WIDTH = 50
OBJECT_HEIGHT = 30
OBJECT_SPEED = 5

# Difficulty levels
EASY = 2
MEDIUM = 3
HARD = 4

# Set time limit for each difficulty (in seconds)
time_limit = {
    EASY: 300,   # 5 minutes for easy
    MEDIUM: 300, # 5 minutes for medium
    HARD: 300    # 5 minutes for hard
}

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trolley Problem Game")

clock = pygame.time.Clock()

# Load player image
player_image = pygame.image.load('./Aiya/images/player.png')  # Replace 'player.png' with your image file
player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))

object_image = pygame.image.load('./Aiya/images/object.png')
object_image = pygame.transform.scale(object_image, (OBJECT_WIDTH, OBJECT_HEIGHT))

# Load track images with alpha channel
track_image_easy = pygame.image.load('./Aiya/images/track_easy.png').convert_alpha()
track_image_medium = pygame.image.load('./Aiya/images/track_medium.png').convert_alpha()
track_image_hard = pygame.image.load('./Aiya/images/track_hard.png').convert_alpha()

# Map difficulty levels to track images
track_images = {
    EASY: track_image_easy,
    MEDIUM: track_image_medium,
    HARD: track_image_hard,
}

# Background images for different difficulty levels (scaled to the window size)
background_images = {
    EASY: pygame.transform.scale(pygame.image.load('./Aiya/images/background_easy.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    MEDIUM: pygame.transform.scale(pygame.image.load('./Aiya/images/background_medium.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    HARD: pygame.transform.scale(pygame.image.load('./Aiya/images/background_hard.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT)),
}
# Background music for different difficulty levels
music_tracks = {
    EASY: './Aiya/music/easy_music.mp3',
    MEDIUM: './Aiya/music/medium_music.mp3',
    HARD: './Aiya/music/hard_music.mp3',
}


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT // 2
        self.speedy = 0

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Object(pygame.sprite.Sprite):
    def __init__(self, track, existing_objects, player_rect):
        super().__init__()
        self.image = object_image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = track.centery - OBJECT_HEIGHT // 2
        self.speedx = -OBJECT_SPEED

        # Check if the object is far enough from existing objects and the player
        while not self.is_object_far_enough(existing_objects) or self.is_too_close_to_player(player_rect):
            self.rect.x = random.randrange(max(player_rect.right + 100, SCREEN_WIDTH // 2), SCREEN_WIDTH)

    def is_object_far_enough(self, existing_objects):
        min_distance = 100  # Adjust the minimum distance as needed
        for obj in existing_objects:
            distance = math.hypot(self.rect.x - obj.rect.x, self.rect.y - obj.rect.y)
            if distance < min_distance:
                return False
        return True

    def is_too_close_to_player(self, player_rect):
        min_distance_to_player = 100  # Adjust the minimum distance to the player as needed
        distance_to_player = math.hypot(self.rect.x - player_rect.centerx, self.rect.y - player_rect.centery)
        return distance_to_player < min_distance_to_player

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.kill()  # Remove the object when it goes off the screen

# Function to display the main menu
def show_menu():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 48)
    title_text = font.render("Track Switching Game", True, (0, 0, 0))
    screen.blit(title_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4))

    easy_text = font.render("Easy", True, (0, 0, 0))
    medium_text = font.render("Medium", True, (0, 0, 0))
    hard_text = font.render("Hard", True, (0, 0, 0))

    screen.blit(easy_text, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2))
    screen.blit(medium_text, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 + 50))
    screen.blit(hard_text, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 + 100))

    pygame.display.flip()

# Function to initialize the game based on the selected difficulty
def initialize_game(difficulty):
    tracks = [pygame.Rect(0, i * TRACK_HEIGHT, TRACK_WIDTH, TRACK_HEIGHT) for i in range(difficulty)]
    current_track = 0

    player = Player()
    objects = pygame.sprite.Group()

    all_sprites = pygame.sprite.Group(player, objects)

    return player, objects, all_sprites, tracks, current_track

# Display the main menu
show_menu()
# Game loop for the main menu
menu_running = True
while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # Easy
                difficulty = EASY
                menu_running = False
            elif event.key == pygame.K_2:  # Medium
                difficulty = MEDIUM
                menu_running = False
            elif event.key == pygame.K_3:  # Hard
                difficulty = HARD
                menu_running = False

# Initialize the game based on the selected difficulty
player, objects, all_sprites, tracks, current_track = initialize_game(difficulty)
# Initialize Pygame mixer
pygame.mixer.init()

# Load background music
pygame.mixer.music.load(music_tracks[difficulty])

# Play the background music on loop
pygame.mixer.music.play(-1)
# Game loop for the actual game
running = True
score = 0
generation_counter = 0  # Counter for slowing down generation

# Get the start time
start_time = pygame.time.get_ticks()

while running:
    # Calculate elapsed time
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Convert to seconds

    # Check if the time limit is reached
    if elapsed_time >= time_limit[difficulty]:
        running = False  # End the game when the time limit is reached

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_track = max(current_track - 1, 0)
            elif event.key == pygame.K_DOWN:
                current_track = min(current_track + 1, len(tracks) - 1)

    player.rect.centery = tracks[current_track].centery

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.speedy = -PLAYER_SPEED
    elif keys[pygame.K_DOWN]:
        player.speedy = PLAYER_SPEED
    else:
        player.speedy = 0

    all_sprites.update()

    # Check collision with objects
    hits = pygame.sprite.spritecollide(player, objects, True)
    for hit in hits:
        score += 5  # Each object gives 5 to the score

    # Create new objects only on the active track and from a certain distance of the player
    if random.randint(0, 100) < 10 and generation_counter % 20 == 0:
        new_object = Object(tracks[current_track], objects, player.rect)
        objects.add(new_object)
        all_sprites.add(new_object)
        generation_counter = 0  # Reset the counter when a new object is generated

    # Increment generation counter
    generation_counter += 1

    # Draw background
    screen.blit(background_images[difficulty], (0, 0))

    # Draw tracks
    for i, track in enumerate(tracks):
        screen.blit(track_images[difficulty], track)

    # Draw sprites
    all_sprites.draw(screen)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Display time remaining
    time_remaining = max(0, time_limit[difficulty] - elapsed_time)
    time_text = font.render(f"Time: {time_remaining} seconds", True, (0, 0, 0))
    screen.blit(time_text, (SCREEN_WIDTH - 200, 10))

    pygame.display.flip()
    clock.tick(60)

# Stop the background music when the game is over
pygame.mixer.music.stop()

# Display the final message with the score
final_message_font = pygame.font.Font(None, 48)
final_message = final_message_font.render(f"Game Over! Your Score: {score}", True, (255, 0, 0))
screen.blit(final_message, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4))
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.delay(3000)  # 3000 milliseconds (3 seconds)

pygame.quit()
sys.exit()
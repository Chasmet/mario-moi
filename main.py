import pygame
import sys

pygame.init()

# Fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Moi Bros - Avec ma tête !")
clock = pygame.time.Clock()

# === TA PHOTO COMME MARIO ===
try:
    player_image = pygame.image.load('assets/player.png')
    player_image = pygame.transform.scale(player_image, (52, 72))
except:
    print("⚠️  Place ta photo dans assets/player.png")
    player_image = pygame.Surface((52, 72))
    player_image.fill((200, 30, 30))

player_rect = player_image.get_rect()
player_rect.x = 100
player_rect.y = 400

vel_y = 0
on_ground = False
speed = 6

# Plateformes
platforms = [
    pygame.Rect(0, 500, WIDTH, 100),
    pygame.Rect(150, 420, 130, 20),
    pygame.Rect(320, 320, 130, 20),
    pygame.Rect(500, 380, 110, 20),
]

# Pipe verte
pipe = pygame.Rect(650, 410, 60, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_q]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += speed
    if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and on_ground:
        vel_y = -17
        on_ground = False

    # Gravité
    vel_y += 0.85
    player_rect.y += vel_y

    # Collisions
    on_ground = False
    for p in platforms:
        if player_rect.colliderect(p) and vel_y >= 0:
            player_rect.bottom = p.top
            vel_y = 0
            on_ground = True

    # Limites
    player_rect.left = max(0, player_rect.left)
    player_rect.right = min(WIDTH, player_rect.right)
    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT
        vel_y = 0

    # Dessin
    screen.fill((135, 206, 235))

    for p in platforms:
        pygame.draw.rect(screen, (210, 180, 140), p)

    # Pipe
    pygame.draw.rect(screen, (0, 170, 0), pipe)
    pygame.draw.rect(screen, (0, 130, 0), (pipe.x - 8, pipe.y - 30, pipe.width + 16, 35))

    # TON VISAGE
    screen.blit(player_image, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
import pygame

pygame.init()

# Pencere boyutları
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Top Hareketi")

pygame.mixer.init()


# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Topun başlangıç konumu
x, y = 400, 300
radius = 20
speed = 5

running = True
while running:
    pygame.time.delay(30)  # FPS ayarı

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    keys = pygame.key.get_pressed()  # Tuşları oku
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill(WHITE)  # Ekranı temizle
    pygame.draw.circle(screen, RED, (x, y), radius)  # Topu çiz
    pygame.display.update()  # Ekranı güncelle

pygame.quit()

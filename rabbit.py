import pygame
import sys

# Инициализация
pygame.init()

# Настройки окна
width, height = 500, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Заяц")

# Цвета
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
PINK = (255, 182, 193)

# Главный цикл
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Уши
    pygame.draw.ellipse(screen, GRAY, (170, 50, 40, 120))  # левое ухо
    pygame.draw.ellipse(screen, GRAY, (290, 50, 40, 120))  # правое ухо

    # Голова
    pygame.draw.circle(screen, GRAY, (250, 250), 100)

    # Глаза
    pygame.draw.circle(screen, WHITE, (210, 230), 20)
    pygame.draw.circle(screen, WHITE, (290, 230), 20)
    pygame.draw.circle(screen, BLACK, (210, 230), 7)
    pygame.draw.circle(screen, BLACK, (290, 230), 7)

    # Нос
    pygame.draw.circle(screen, PINK, (250, 270), 10)

    # Рот
    pygame.draw.arc(screen, BLACK, (230, 270, 40, 30), 3.14, 0, 2)

    # Обновление экрана
    pygame.display.flip()

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

# Завершение
pygame.quit()
sys.exit()
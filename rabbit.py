import pygame
import sys

# Инициализация
pygame.init()

# Параметры окна
width, height = 500, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Заяц через функции")

# Цвета
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
PINK = (255, 192, 203)
BLACK = (0, 0, 0)
DARK_GRAY = (150, 150, 150)


def draw_ears():
    # Уши
    pygame.draw.ellipse(screen, GRAY, (170, 30, 40, 100))  # левое
    pygame.draw.ellipse(screen, GRAY, (290, 30, 40, 100))  # правое
    pygame.draw.ellipse(screen, PINK, (180, 40, 20, 80))   # внутренняя часть левого
    pygame.draw.ellipse(screen, PINK, (300, 40, 20, 80))   # внутренняя часть правого


def draw_head():
    # Голова
    pygame.draw.circle(screen, GRAY, (250, 180), 70)

    # Глаза
    pygame.draw.circle(screen, WHITE, (225, 170), 15)
    pygame.draw.circle(screen, WHITE, (275, 170), 15)
    pygame.draw.circle(screen, BLACK, (225, 170), 5)
    pygame.draw.circle(screen, BLACK, (275, 170), 5)

    # Нос
    pygame.draw.polygon(screen, PINK, [(245, 190), (255, 190), (250, 200)])

    # Улыбка
    pygame.draw.arc(screen, BLACK, (230, 200, 40, 20), 3.14, 0, 2)


def draw_body():
    # Туловище
    pygame.draw.ellipse(screen, GRAY, (190, 240, 120, 160))

    # Нижние лапки
    pygame.draw.circle(screen, GRAY, (200, 390), 25)
    pygame.draw.circle(screen, GRAY, (300, 390), 25)

    # Передние лапки
    pygame.draw.ellipse(screen, DARK_GRAY, (170, 270, 30, 50))
    pygame.draw.ellipse(screen, DARK_GRAY, (300, 270, 30, 50))


def draw_bunny():
    draw_ears()
    draw_head()
    draw_body()


# Главный цикл
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    draw_bunny()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
sys.exit()

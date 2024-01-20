import pygame

# Инициализация pygame
pygame.init()

# Определение размеров окна и игрового поля
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 100  # Размер клетки игрового поля
GRID_WIDTH = SCREEN_WIDTH // 8  # Ширина игрового поля
GRID_HEIGHT = SCREEN_HEIGHT // 5  # Высота игрового поля

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Lemmings')

# Создание игрового поля с препятствиями
grid = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана белым цветом
    screen.fill(WHITE)

    # Отрисовка игрового поля
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                color = BLACK
                pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Обновление экрана
    pygame.display.flip()

# Выход из игры
pygame.quit()


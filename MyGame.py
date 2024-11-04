import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размера окна
window_size = (1200, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Игра на выживание")

# Загрузка изображений
image1 = pygame.image.load("photo_2024-11-04_09-36-11.png")  # Объект игрока
image2 = pygame.image.load("787878.png")    # Падающие объекты
image_rect1 = image1.get_rect()

# Список для хранения падающих объектов
falling_objects = []
num_objects = 5  # Количество падающих объектов

# Инициализация падающих объектов
for _ in range(num_objects):
    rect = image2.get_rect()
    rect.x = random.randint(0, window_size[0] - rect.width)
    rect.y = random.randint(-600, -50)  # Начальная позиция выше экрана
    falling_objects.append(rect)

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect1.x = mouseX - image_rect1.width // 2
            image_rect1.y = mouseY - image_rect1.height // 2

    # Движение падающих объектов
    for rect in falling_objects:
        rect.y += 5  # Скорость падения
        if rect.y > window_size[1]:  # Если объект вышел за нижнюю границу
            rect.x = random.randint(0, window_size[0] - rect.width)
            rect.y = random.randint(-100, -50)

    # Проверка на столкновения
    for rect in falling_objects:
        if image_rect1.colliderect(rect):
            print("Произошло столкновение! Игра окончена.")
            run = False  # Завершаем игру при столкновении

    # Отрисовка
    screen.fill((0, 0, 0))
    for rect in falling_objects:
        screen.blit(image2, rect)
    screen.blit(image1, image_rect1)

    pygame.display.flip()
    clock.tick(60)  # Ограничение FPS

pygame.quit()
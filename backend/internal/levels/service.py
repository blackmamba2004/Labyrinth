import random
import math

# Класс бота для построения лабиринта
class Cleaner:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Получение случайного элемента массива
def get_random_item(array):
    index = math.floor(random.random() * len(array))
    return array[index]

# Получение случайного числа в пределах [min, max]
def rand(min_val, max_val):
    return math.floor(random.random() * (max_val - min_val + 1)) + min_val

# Функция для генерации лабиринта
def generate_maze(m, n):
    # Проверка, что размеры матрицы нечётные
    if m % 2 == 0 or n % 2 == 0:
        raise ValueError("Размеры m и n должны быть нечётными")

    # Создание матрицы и установка всех ячеек как стен (1)
    matrix = [[1] * n for _ in range(m)]

    # Создание начального положения бота и изменение соответствующих клеток
    cleaner = Cleaner(rand(1, n // 2) * 2 - 1, rand(1, m // 2) * 2 - 1)
    matrix[1][0], matrix[m-2][n-1], matrix[cleaner.y][cleaner.x] = 0, 0, 0

    # Запуск генерации лабиринта
    count_of_cells = (m // 2) * (n // 2)
    count_of_visited_cells = 1

    while count_of_visited_cells < count_of_cells:
        count_of_visited_cells = move_cleaner(cleaner, matrix, m, n, count_of_visited_cells)

    return matrix

# Функция перемещения бота и изменения ячеек
def move_cleaner(cleaner, matrix, m, n, count_of_visited_cells):
    directions = []

    # Добавление возможных направлений
    if cleaner.x > 1:
        directions.append([-2, 0])
    if cleaner.x < n - 2:
        directions.append([2, 0])
    if cleaner.y > 1:
        directions.append([0, -2])
    if cleaner.y < m - 2:
        directions.append([0, 2])

    # Получение случайного направления и перемещение
    dx, dy = get_random_item(directions)
    new_x, new_y = cleaner.x + dx, cleaner.y + dy

    # Если направление ведет в непосещённую клетку, создаём путь
    if matrix[new_y][new_x] == 1:
        matrix[new_y][new_x] = 0
        matrix[cleaner.y + dy // 2][cleaner.x + dx // 2] = 0
        count_of_visited_cells += 1

    cleaner.x, cleaner.y = new_x, new_y
    return count_of_visited_cells

# Отображение матрицы лабиринта в консоли
def display_maze(matrix):
    for row in matrix:
        for cell in row:
            if cell == 1:
                print("\033[40m   \033[0m", end="")  # Чёрный цвет для стен
            else:
                print("\033[47m   \033[0m", end="")  # Белый цвет для путей
        print()

# Основная программа
m, n = 27, 27
maze = generate_maze(m, n)
# display_maze(maze)
from concurrent.futures import ThreadPoolExecutor
import random
import time
from functools import reduce

def rot90(matrix):
    """
    Поворачивает матрицу на 90 градусов против часовой стрелки.

    :param matrix: Исходная матрица.
    :return: Повернутая матрица.
    """
    return [list(reversed(col)) for col in zip(*matrix)]

def rot270(matrix):
    """
    Поворачивает матрицу на 90 градусов по часовой стрелке.

    :param matrix: Исходная матрица.
    :return: Повернутая матрица.
    """
    return [list(row) for row in list(zip(*matrix))[::-1]]

def big_sum(mas_a, mas_b):
    """
    Вычисляет сумму двух массивов, представляющих большие числа.

    :param mas_a: Первый массив.
    :param mas_b: Второй массив.
    :return: Массив, представляющий сумму двух больших чисел.
    """
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    x = int_mas_a + int_mas_b
    return list(map(int, str(x)))

def big_diff(mas_a, mas_b):
    """
    Вычисляет разность двух массивов, представляющих большие числа.

    :param mas_a: Первый массив.
    :param mas_b: Второй массив.
    :return: Массив, представляющий разность двух больших чисел.
    """
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    x = int_mas_a - int_mas_b
    return list(map(int, str(abs(x)))) if x < 0 else list(map(int, str(x)))

def how_much_same(mas_a, mas_b):
    """
    Подсчитывает количество одинаковых элементов в двух массивах.

    :param mas_a: Первый массив.
    :param mas_b: Второй массив.
    :return: Количество одинаковых элементов.
    """
    return len(set(map(abs, mas_a)) & set(map(abs, mas_b)))

def get_arr(length):
    """
    Получает массив от пользователя.

    :param length: Длина массива.
    :return: Массив, введенный пользователем.
    """
    return [int(input(f"Введите элемент {i+1}: ")) for i in range(length)]

def gen_arr(length):
    """
    Генерирует случайный массив.

    :param length: Длина массива.
    :return: Случайный массив.
    """
    time.sleep(random.randint(1, 10))
    return [random.randint(0, 9) for _ in range(length)]

def get_matrix(length, width):
    """
    Получает матрицу от пользователя.

    :param length: Длина матрицы.
    :param width: Ширина матрицы.
    :return: Матрица, введенная пользователем.
    """
    return [[int(input(f"Введите элемент [{i}][{j}]: ")) for j in range(width)] for i in range(length)]

def gen_matrix(length, width):
    """
    Генерирует случайную матрицу.

    :param length: Длина матрицы.
    :param width: Ширина матрицы.
    :return: Случайная матрица.
    """
    return [[random.randint(0, 9) for _ in range(width)] for _ in range(length)]

def gen_or_get_mas():
    """
    Запрашивает у пользователя, хочет ли он ввести массив вручную или сгенерировать его случайно.

    :return: Массив, введенный пользователем или сгенерированный случайно.
    """
    choice = input("Желаете ввести массив вручную? y/n \n В случае отказа массив будет сгенерирован случайно: ")
    if choice == 'y':
        length = int(input("Введите длину массива: "))
        return get_arr(length)
    elif choice == 'n':
        length = int(input("Введите длину массива: "))
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(gen_arr, length) for _ in range(3)]
            results = [future.result() for future in futures]
            for i, result in enumerate(results):
                print(f"Массив {chr(ord('a') + i)}: {result}")
            char = input("Выберите понравившийся массив (a, b или c): ")
            return results[ord(char) - ord('a')]
    else:
        print("Неверные данные")
        return []

def gen_or_get_mat():
    """
    Запрашивает у пользователя, хочет ли он ввести матрицу вручную или сгенерировать её случайно.

    :return: Матрица, введенная пользователем или сгенерированная случайно.
    """
    choice = input("Желаете ввести матрицу вручную? y/n \n В случае отказа матрица будет сгенерирована случайно: ")
    if choice == 'y':
        length = int(input("Введите длину матрицы: "))
        width = int(input("Введите ширину матрицы: "))
        return get_matrix(length, width)
    elif choice == 'n':
        length = int(input("Введите длину матрицы: "))
        width = int(input("Введите ширину матрицы: "))
        return gen_matrix(length, width)
    else:
        print("Неверные данные")
        return []

def menu():
    """
    Основное меню программы.
    """
    point = int(input("Выберите пункт меню: "))
    if point == 1:
        mas_a = gen_or_get_mas()
        mas_b = gen_or_get_mas()
        operation = int(input("Сумма (1) или разность (2): "))
        if operation == 1:
            print(big_sum(mas_a, mas_b))
        elif operation == 2:
            print(big_diff(mas_a, mas_b))
        else:
            print("Error")
    elif point == 2:
        mat = gen_or_get_mat()
        direction = int(input("Повернуть матрицу на право (1) или на лево (2): "))
        if direction == 1:
            print(rot90(mat))
        elif direction == 2:
            print(rot270(mat))
        else:
            print("Error")
    elif point == 3:
        mas_a = gen_or_get_mas()
        mas_b = gen_or_get_mas()
        print(how_much_same(mas_a, mas_b))
    elif point == 4:
        exit()
    else:
        print("Error")

if __name__ == "__main__":
    while True:
        print(
            "Задачи\n 1. Входные данные: 2 массива с числами одинакового размера. Нужно произвести сумму чисел из массивов, первый массив должен быть отсортирован в порядке убывания, второй в порядке возрастания. Если числа в массивах совпадают, их сумма будет равна нулю. Конечный массив нужно отсортировать в порядке возрастания.\n2. Входные данные: матрица N на M. Требуется повернуть матрицу на 90 градусов против часовой или по часовой.\n 3. Входные данные: 2 массива с цифрами, каждый представляет собой большое число. Нужно произвести сумму или разность массивов.\n4. Закончить работу программы")
        menu()

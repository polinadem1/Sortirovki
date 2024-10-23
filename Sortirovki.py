import random
# Реализация сортировки выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Обмен значениями

# Генерация случайного массива
def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Генерация почти отсортированного массива
def generate_nearly_sorted_array(size):
    arr = list(range(size))  # Создаем отсортированный массив
    for _ in range(size // 10):  # Перемешиваем 10% элементов
        idx1, idx2 = random.randint(0, size-1), random.randint(0, size-1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

# Генерация массива, отсортированного в обратном порядке
def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))  # Возвращаем массив, отсортированный в обратном порядке

# Тестирование сортировки на разных типах массивов
def main():
    size = 10  # Вы можете изменить размер массива здесь

    # Генерация и сортировка случайного массива
    random_array = generate_random_array(size)
    print("Случайный массив до сортировки:", random_array)
    selection_sort(random_array)
    print("Случайный массив после сортировки:", random_array)

    # Генерация и сортировка почти отсортированного массива
    nearly_sorted_array = generate_nearly_sorted_array(size)
    print("\nПочти отсортированный массив до сортировки:", nearly_sorted_array)
    selection_sort(nearly_sorted_array)
    print("Почти отсортированный массив после сортировки:", nearly_sorted_array)

    # Генерация и сортировка массива в обратном порядке
    reverse_sorted_array = generate_reverse_sorted_array(size)
    print("\nМассив в обратном порядке до сортировки:", reverse_sorted_array)
    selection_sort(reverse_sorted_array)
    print("Массив в обратном порядке после сортировки:", reverse_sorted_array)

if __name__ == "__main__":
    main()




import random
# Реализация сортировки вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы, которые больше key, на одну позицию вперед
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Генерация случайного массива
def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Генерация почти отсортированного массива
def generate_nearly_sorted_array(size):
    arr = list(range(size))  # Создаем отсортированный массив
    for _ in range(size // 10):  # Перемешиваем 10% элементов
        idx1, idx2 = random.randint(0, size-1), random.randint(0, size-1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

# Генерация массива, отсортированного в обратном порядке
def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))  # Возвращаем массив, отсортированный в обратном порядке

# Тестирование сортировки на разных типах массивов
def main():
    size = 10  #изменить размер массива здесь

    # Генерация и сортировка случайного массива
    random_array = generate_random_array(size)
    print("Случайный массив до сортировки:", random_array)
    insertion_sort(random_array)
    print("Случайный массив после сортировки:", random_array)

    # Генерация и сортировка почти отсортированного массива
    nearly_sorted_array = generate_nearly_sorted_array(size)
    print("\nПочти отсортированный массив до сортировки:", nearly_sorted_array)
    insertion_sort(nearly_sorted_array)
    print("Почти отсортированный массив после сортировки:", nearly_sorted_array)

    # Генерация и сортировка массива в обратном порядке
    reverse_sorted_array = generate_reverse_sorted_array(size)
    print("\nМассив в обратном порядке до сортировки:", reverse_sorted_array)
    insertion_sort(reverse_sorted_array)
    print("Массив в обратном порядке после сортировки:", reverse_sorted_array)

if __name__ == "__main__":
    main()



import random
# Реализация сортировки пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Проходим по массиву и "всплываем" самый большой элемент в конец
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Меняем элементы местами
                swapped = True
        # Если ни один элемент не был поменян местами, массив уже отсортирован
        if not swapped:
            break

# Генерация случайного массива
def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Генерация почти отсортированного массива
def generate_nearly_sorted_array(size):
    arr = list(range(size))  # Создаем отсортированный массив
    for _ in range(size // 10):  # Перемешиваем 10% элементов
        idx1, idx2 = random.randint(0, size-1), random.randint(0, size-1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

# Генерация массива, отсортированного в обратном порядке
def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))  # Возвращаем массив, отсортированный в обратном порядке

# Тестирование сортировки на разных типах массивов
def main():
    size = 10  #изменить размер массива здесь

    # Генерация и сортировка случайного массива
    random_array = generate_random_array(size)
    print("Случайный массив до сортировки:", random_array)
    bubble_sort(random_array)
    print("Случайный массив после сортировки:", random_array)

    # Генерация и сортировка почти отсортированного массива
    nearly_sorted_array = generate_nearly_sorted_array(size)
    print("\nПочти отсортированный массив до сортировки:", nearly_sorted_array)
    bubble_sort(nearly_sorted_array)
    print("Почти отсортированный массив после сортировки:", nearly_sorted_array)

    # Генерация и сортировка массива в обратном порядке
    reverse_sorted_array = generate_reverse_sorted_array(size)
    print("\nМассив в обратном порядке до сортировки:", reverse_sorted_array)
    bubble_sort(reverse_sorted_array)
    print("Массив в обратном порядке после сортировки:", reverse_sorted_array)

if __name__ == "__main__":
    main()



import random

# Реализация сортировки слиянием
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину массива
        left_half = arr[:mid]  # Левую часть массива
        right_half = arr[mid:]  # Правую часть массива

        # Рекурсивно сортируем обе половины
        merge_sort(left_half)
        merge_sort(right_half)

        # Слияние отсортированных половин
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Копируем оставшиеся элементы, если они остались
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Генерация случайного массива
def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Генерация почти отсортированного массива
def generate_nearly_sorted_array(size):
    arr = list(range(size))  # Создаем отсортированный массив
    for _ in range(size // 10):  # Перемешиваем 10% элементов
        idx1, idx2 = random.randint(0, size-1), random.randint(0, size-1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

# Генерация массива, отсортированного в обратном порядке
def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))  # Возвращаем массив, отсортированный в обратном порядке

# Тестирование сортировки на разных типах массивов
def main():
    size = 10  #изменить размер массива здесь

    # Генерация и сортировка случайного массива
    random_array = generate_random_array(size)
    print("Случайный массив до сортировки:", random_array)
    merge_sort(random_array)
    print("Случайный массив после сортировки:", random_array)

    # Генерация и сортировка почти отсортированного массива
    nearly_sorted_array = generate_nearly_sorted_array(size)
    print("\nПочти отсортированный массив до сортировки:", nearly_sorted_array)
    merge_sort(nearly_sorted_array)
    print("Почти отсортированный массив после сортировки:", nearly_sorted_array)

    # Генерация и сортировка массива в обратном порядке
    reverse_sorted_array = generate_reverse_sorted_array(size)
    print("\nМассив в обратном порядке до сортировки:", reverse_sorted_array)
    merge_sort(reverse_sorted_array)
    print("Массив в обратном порядке после сортировки:", reverse_sorted_array)

if __name__ == "__main__":
    main()



import random
# Реализация сортировки Шелла
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Начальный интервал делим пополам
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Уменьшаем интервал
    return arr

# Генерация случайного массива
def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Генерация почти отсортированного массива
def generate_nearly_sorted_array(size):
    arr = list(range(size))  # Создаем отсортированный массив
    for _ in range(size // 10):  # Перемешиваем 10% элементов
        idx1, idx2 = random.randint(0, size-1), random.randint(0, size-1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

# Генерация массива, отсортированного в обратном порядке
def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))  # Возвращаем массив, отсортированный в обратном порядке

# Тестирование сортировки на разных типах массивов
def main():
    size = 10  #изменить размер массива здесь

    # Генерация и сортировка случайного массива
    random_array = generate_random_array(size)
    print("Случайный массив до сортировки:", random_array)
    shell_sort(random_array)
    print("Случайный массив после сортировки:", random_array)

    # Генерация и сортировка почти отсортированного массива
    nearly_sorted_array = generate_nearly_sorted_array(size)
    print("\nПочти отсортированный массив до сортировки:", nearly_sorted_array)
    shell_sort(nearly_sorted_array)
    print("Почти отсортированный массив после сортировки:", nearly_sorted_array)

    # Генерация и сортировка массива в обратном порядке
    reverse_sorted_array = generate_reverse_sorted_array(size)
    print("\nМассив в обратном порядке до сортировки:", reverse_sorted_array)
    shell_sort(reverse_sorted_array)
    print("Массив в обратном порядке после сортировки:", reverse_sorted_array)

if __name__ == "__main__":
    main()



import random
# Реализация сортировки Шелла с использованием последовательности Хиббарда
def shell_sort_hibbard(arr):
    n = len(arr)
    
    # Генерация последовательности Хиббарда
    gaps = []
    k = 1
    while (2 ** k - 1) < n:
        gaps.insert(0, 2 ** k - 1)  # Вставляем элементы в начале списка
        k += 1

    # Сортировка по интервалам из последовательности Хиббарда
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

# Генерация случайного массива
def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Генерация почти отсортированного массива
def generate_nearly_sorted_array(size):
    arr = list(range(size))  # Создаем отсортированный массив
    for _ in range(size // 10):  # Перемешиваем 10% элементов
        idx1, idx2 = random.randint(0, size-1), random.randint(0, size-1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

# Генерация массива, отсортированного в обратном порядке
def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))  # Возвращаем массив, отсортированный в обратном порядке

# Тестирование сортировки на разных типах массивов
def main():
    size = 10  #изменить размер массива здесь

    # Генерация и сортировка случайного массива
    random_array = generate_random_array(size)
    print("Случайный массив до сортировки:", random_array)
    shell_sort_hibbard(random_array)
    print("Случайный массив после сортировки:", random_array)

    # Генерация и сортировка почти отсортированного массива
    nearly_sorted_array = generate_nearly_sorted_array(size)
    print("\nПочти отсортированный массив до сортировки:", nearly_sorted_array)
    shell_sort_hibbard(nearly_sorted_array)
    print("Почти отсортированный массив после сортировки:", nearly_sorted_array)

    # Генерация и сортировка массива в обратном порядке
    reverse_sorted_array = generate_reverse_sorted_array(size)
    print("\nМассив в обратном порядке до сортировки:", reverse_sorted_array)
    shell_sort_hibbard(reverse_sorted_array)
    print("Массив в обратном порядке после сортировки:", reverse_sorted_array)

if __name__ == "__main__":
    main()




import random
# Реализация сортировки Шелла с использованием последовательности Пратта
def shell_sort_pratt(arr):
    n = len(arr)
    
    # Генерация последовательности Пратта
    gaps = generate_pratt_sequence(n)
    
    # Сортировка по интервалам из последовательности Пратта
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

# Генерация последовательности Пратта: числа вида 2^i * 3^j < n
def generate_pratt_sequence(n):
    sequence = set()
    i = 1
    while i < n:
        j = i
        while j < n:
            sequence.add(j)
            j *= 3
        i *= 2
    return sorted(sequence, reverse=True)

# Генерация случайного массива
def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Генерация почти отсортированного массива
def generate_nearly_sorted_array(size):
    arr = list(range(size))  # Создаем отсортированный массив
    for _ in range(size // 10):  # Перемешиваем 10% элементов
        idx1, idx2 = random.randint(0, size-1), random.randint(0, size-1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

# Генерация массива, отсортированного в обратном порядке
def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))  # Возвращаем массив, отсортированный в обратном порядке

# Тестирование сортировки на разных типах массивов
def main():
    size = 10  #изменить размер массива здесь

    # Генерация и сортировка случайного массива
    random_array = generate_random_array(size)
    print("Случайный массив до сортировки:", random_array)
    shell_sort_pratt(random_array)
    print("Случайный массив после сортировки:", random_array)

    # Генерация и сортировка почти отсортированного массива
    nearly_sorted_array = generate_nearly_sorted_array(size)
    print("\nПочти отсортированный массив до сортировки:", nearly_sorted_array)
    shell_sort_pratt(nearly_sorted_array)
    print("Почти отсортированный массив после сортировки:", nearly_sorted_array)

    # Генерация и сортировка массива в обратном порядке
    reverse_sorted_array = generate_reverse_sorted_array(size)
    print("\nМассив в обратном порядке до сортировки:", reverse_sorted_array)
    shell_sort_pratt(reverse_sorted_array)
    print("Массив в обратном порядке после сортировки:", reverse_sorted_array)

if __name__ == "__main__":
    main()



import random
# Реализация алгоритма быстрой сортировки
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Опорный элемент
        left = [x for x in arr if x < pivot]  # Элементы меньше опорного
        middle = [x for x in arr if x == pivot]  # Элементы равные опорному
        right = [x for x in arr if x > pivot]  # Элементы больше опорного
        return quick_sort(left) + middle + quick_sort(right)

# Генерация случайного массива
def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Генерация почти отсортированного массива
def generate_nearly_sorted_array(size):
    arr = list(range(size))  # Создаем отсортированный массив
    for _ in range(size // 10):  # Перемешиваем 10% элементов
        idx1, idx2 = random.randint(0, size - 1), random.randint(0, size - 1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]  # Меняем местами два случайных элемента
    return arr

# Генерация массива, отсортированного в обратном порядке
def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))  # Возвращаем массив, отсортированный в обратном порядке

# Тестирование сортировки на разных типах массивов
def main():
    size = 10  #изменить размер массива здесь

    # Генерация и сортировка случайного массива
    random_array = generate_random_array(size)
    print("Случайный массив до сортировки:", random_array)
    sorted_random_array = quick_sort(random_array)
    print("Случайный массив после сортировки:", sorted_random_array)

    # Генерация и сортировка почти отсортированного массива
    nearly_sorted_array = generate_nearly_sorted_array(size)
    print("\nПочти отсортированный массив до сортировки:", nearly_sorted_array)
    sorted_nearly_sorted_array = quick_sort(nearly_sorted_array)
    print("Почти отсортированный массив после сортировки:", sorted_nearly_sorted_array)

    # Генерация и сортировка массива в обратном порядке
    reverse_sorted_array = generate_reverse_sorted_array(size)
    print("\nМассив в обратном порядке до сортировки:", reverse_sorted_array)
    sorted_reverse_sorted_array = quick_sort(reverse_sorted_array)
    print("Массив в обратном порядке после сортировки:", sorted_reverse_sorted_array)

if __name__ == "__main__":
    main()



import random
# Реализация алгоритма пирамидальной сортировки (Heap Sort)
def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # Левый потомок
    right = 2 * i + 2  # Правый потомок

    # Проверяем, является ли левый потомок больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Проверяем, является ли правый потомок больше, чем самый большой элемент на данный момент
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если самый большой элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами
        heapify(arr, n, largest)  # Рекурсивно преобразуем в пирамиду

def heap_sort(arr):
    n = len(arr)

    # Построение пирамиды (перегруппировка массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Перемещаем текущий корень в конец
        heapify(arr, i, 0)  # Вызываем heapify на уменьшенной куче

# Генерация случайного массива
def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Генерация почти отсортированного массива
def generate_nearly_sorted_array(size):
    arr = list(range(size))  # Создаем отсортированный массив
    for _ in range(size // 10):  # Перемешиваем 10% элементов
        idx1, idx2 = random.randint(0, size - 1), random.randint(0, size - 1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]  # Меняем местами два случайных элемента
    return arr

# Генерация массива, отсортированного в обратном порядке
def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))  # Возвращаем массив, отсортированный в обратном порядке

# Тестирование сортировки на разных типах массивов
def main():
    size = 10  #изменить размер массива здесь

    # Генерация и сортировка случайного массива
    random_array = generate_random_array(size)
    print("Случайный массив до сортировки:", random_array)
    heap_sort(random_array)
    print("Случайный массив после сортировки:", random_array)

    # Генерация и сортировка почти отсортированного массива
    nearly_sorted_array = generate_nearly_sorted_array(size)
    print("\nПочти отсортированный массив до сортировки:", nearly_sorted_array)
    heap_sort(nearly_sorted_array)
    print("Почти отсортированный массив после сортировки:", nearly_sorted_array)

    # Генерация и сортировка массива в обратном порядке
    reverse_sorted_array = generate_reverse_sorted_array(size)
    print("\nМассив в обратном порядке до сортировки:", reverse_sorted_array)
    heap_sort(reverse_sorted_array)
    print("Массив в обратном порядке после сортировки:", reverse_sorted_array)

if __name__ == "__main__":
    main()





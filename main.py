import time


# Базовий клас для всіх алгоритмів (Абстракція за Мейєром)
class SortingStrategy:
    def sort(self, data):
        # Цей метод буде перевизначений у дочірніх класах
        pass


# Реалізація бульбашкового сортування
class BubbleSort(SortingStrategy):
    def sort(self, data):
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


# Реалізація швидкого сортування
class QuickSort(SortingStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data

        pivot = data[len(data) // 2]
        # Використовуємо звичайні цикли для більшої наочності
        left, middle, right = [], [], []

        for item in data:
            if item < pivot:
                left.append(item)
            elif item == pivot:
                middle.append(item)
            else:
                right.append(item)

        return self.sort(left) + middle + self.sort(right)


# Керуючий клас (Контекст / Менеджер)
class ArraySorter:
    def __init__(self, strategy: SortingStrategy):
        # Поліморфізм: ми не знаємо, який саме алгоритм тут,
        # ми просто знаємо, що у нього є метод .sort()
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def perform_sort(self, array):
        print(f"--- Запуск сортування: {self._strategy.__class__.__name__} ---")
        start_time = time.time()
        result = self._strategy.sort(array)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time:.6f} сек.")
        return result


# --- Головна частина програми ---
if __name__ == "__main__":
    # Створюємо масив для тестів
    test_data = [19, 2, 31, 45, 6, 11, 121, 27]

    print(f"Вхідний масив: {test_data}\n")

    # Створюємо об'єкт-контекст
    sorter = ArraySorter(BubbleSort())

    # Сортуємо бульбашкою
    print("Результат (Bubble):", sorter.perform_sort(test_data))

    print("-" * 30)

    # Змінюємо алгоритм на "Швидкий" на льоту (динамічний поліморфізм)
    sorter.set_strategy(QuickSort())
    print("Результат (Quick):", sorter.perform_sort(test_data))

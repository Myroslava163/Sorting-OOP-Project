# Алгоритм сортування бульбашкою
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Алгоритм швидкого сортування
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Головна функція-диспетчер
def sort_manager(arr, algorithm_name):
    """
    Приймає масив та назву алгоритму, викликає відповідну функцію.
    """
    if algorithm_name == "bubble":
        return bubble_sort(arr)
    elif algorithm_name == "quick":
        return quick_sort(arr)
    else:
        return "Помилка: невідомий алгоритм"

# Демонстрація
data = [3, 1, 4, 1, 5, 9, 2]
print("Виклик через функції (Bubble):", sort_manager(data, "bubble"))
# Домашнее задание 6:
# Написать программу на любом языке в любой парадигме для бинарного поиска.
# На вход подаётся целочисленный массив и число.
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

# Решение:
# Реализуем бинарный поиск методом итераций в императивной (процедурной) парадигме.

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


def print_result(index):
    if index is None:
        print(-1)
    else:
        print("Индекс искомого элемента =", index)


if __name__ == '__main__':
    my_list = [1, 4, 7, 10, 13, 16, 19]

    result_1 = binary_search(my_list, 7)
    print_result(result_1)

    result_2 = binary_search(my_list, 6)
    print_result(result_2)

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

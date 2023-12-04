# Задача № 1:
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру
# для сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

numbers = [8, 5, 2, 0, 1, 7, 7]


def sort_list_imperative(nums_array):
    flag = True
    while flag:
        flag = False
        for i in range(len(nums_array) - 1):
            if nums_array[i + 1] > nums_array[i]:
                temp = nums_array[i]
                nums_array[i] = nums_array[i + 1]
                nums_array[i + 1] = temp
                flag = True
    print(nums_array)


# Задача №2:
# Написать точно такую же процедуру, но в декларативном стиле.

def sort_list_declarative(nums_array):
    nums_array.sort(reverse=True)
    print(nums_array)

# Домашнее задание:
# Два игрока по очереди ставят крестики и нолики на игровое поле.
# Игра завершается когда кто-то победил, либо наступила ничья, либо игроки отказались играть.
# Написать игру в “Крестики-нолики”. Можете использовать любые парадигмы, которые посчитаете наиболее подходящими.
# Можно реализовать доску как угодно - как одномерный массив или двумерный массив (массив массивов).
# Можно использовать как правила, так и хардкод, на своё усмотрение.
# Главное, чтобы в игру можно было поиграть через терминал компьютера.

array = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
p1 = 'X'
p2 = 'O'


def print_field(field):
    for row in field:
        for col in row:
            print(col, end='\t')
        print()


def next_turn(player):
    flag = True
    while flag:
        i = int(input("Укажите строку: ")) - 1
        j = int(input("Укажите столбец: ")) - 1
        if array[i][j] == '_':
            array[i][j] = player
            flag = False
            print_field(array)
        else:
            print("-> Некорректные координаты, повторите ввод.")


def win_condition(arr):
    for i in range(len(arr)):
        if (arr[i][0] != '_' and arr[i][0] == arr[i][1] == arr[i][2]) or (
                arr[0][i] != '_' and arr[0][i] == arr[1][i] == arr[2][i]):
            return True
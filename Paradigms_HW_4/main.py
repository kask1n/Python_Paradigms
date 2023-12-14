# Домашнее задание 4:
# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).


import pearson_correlation as p

if __name__ == '__main__':
    x = [8, 2, 32, 9, 0]
    y = [-5, -3, 44, 8, -10]
    correlation = p.pearson_correlation(x, y)
    print("Корреляция Пирсона =", correlation)

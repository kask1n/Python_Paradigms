import math


def pearson_correlation(x, y):
    n = len(x)
    median_x = sum(x) / n
    median_y = sum(y) / n
    numerator = sum([(xi - median_x) * (yi - median_y) for xi, yi in zip(x, y)])
    denominator = math.sqrt(sum([((xi - median_x) ** 2) * ((yi - median_y) ** 2) for xi, yi in zip(x, y)]))
    return numerator / denominator

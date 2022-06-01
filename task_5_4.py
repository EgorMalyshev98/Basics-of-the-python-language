"""Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего"""

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


# result = [12, 44, 4, 10, 78, 123]

def get_num(sr: list):
    res = [sr[i] for i in range(1, len(sr)) if sr[i] > sr[i - 1]]
    return res


print(get_num(src))

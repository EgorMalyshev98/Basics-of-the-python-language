"""Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список
 с сохранением порядка их следования в исходном списке"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


# result = [23, 1, 3, 10, 4, 11]


def get_uniq_numbers(sr: list):
    unique_nums = []
    tmp = set()
    for num in sr:
        if num not in tmp:
            unique_nums.append(num)
        else:
            try:
                unique_nums.remove(num)
            except ValueError:
                continue
        tmp.add(num)
    return unique_nums


print(get_uniq_numbers(src))

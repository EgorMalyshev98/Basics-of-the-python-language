# Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2

a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2

res_list = [a, b, c, d]

for res in res_list:
    print(type(res))

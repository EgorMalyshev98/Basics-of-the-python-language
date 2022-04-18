# Реализовать склонение слова «процент» во фразе «N процентов»
for x in range(100):
    x += 1
    if 11 <= x <= 14:
        print(str(x) + " процентов")
    elif x % 10 in [0, 5, 6, 7, 8, 9]:
        print(str(x) + " процентов")
    elif x % 10 in [2, 3, 4]:
        print(str(x) + " процента")
    else:
        print(str(x) + " процент")

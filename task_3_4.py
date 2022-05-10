Full_names = "Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", \
             "Анна Савельева"


def thesaurus_adv(*names) -> dict:
    f_names = [name.split(' ') for name in names]
    f_dict = {}
    for (i, fn) in enumerate(f_names):
        n_dict = {}
        group = []
        for x in range(len(f_names)):
            if f_names[x][-1][0] == fn[-1][0] and \
                    f_names[x][0][0] == fn[0][0]:
                group.append(' '.join(f_names[x]))
                n_dict.setdefault(fn[0][0], group)
        f_dict.setdefault(fn[-1][0], n_dict)
    return f_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

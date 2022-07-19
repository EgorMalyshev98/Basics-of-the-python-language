from itertools import zip_longest


def user_hobby_dict(users_file, hobbys_file):
    hobby_list = []
    users_list = []

    with open(hobbys_file, 'r', encoding='utf-8') as hr:
        for line in hr:
            hobby_list.append(tuple(line.strip().split(',')))

    with open(users_file, 'r', encoding='utf-8') as ur:
        for line in ur:
            # Разбиваем строку на элементы, убираем скрытые символы с помощью strip(), преобразуем в кортеж.
            users_list.append(tuple(line.strip().split(',')))

    hobby_list.pop(0)  # Убираем первую строку с заголовками из кортежа
    users_list.pop(0)
    if len(users_list) >= len(hobby_list):

        # Генерирурем словарь. Ключ: user, значение - хобби. Помещаем значения из кортежей в переменные с помощью zip().
        # Если в кортеже хобби пусто, в словарь попадает None
        dictt = {u: h for u, h in zip_longest(users_list, hobby_list)}

        return dictt

    else:
        raise ValueError('Хобби больше, чем пользователей')


user_file = 'users.csv'
hobby_file = 'hobby.csv'

print(user_hobby_dict(user_file, hobby_file))

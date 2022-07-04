def find_spamer(filename):
    ip_list = []
    with open(filename, 'r', encoding='utf-8') as fr:  # Открываем файл на чтение

        for line in fr:  # Читаем файл построчно
            res = line.split(' ')[0]
            ip_list.append(res)  # Вставляем полученный ip в список

    counter = {}  # Создаем словарь-счетчик

    for ip in ip_list:  # Проверяем, есть ли ip в словаре, если нет, добавляем новый ключ
        if ip in counter:
            counter[ip] += 1
        else:
            counter[ip] = 1

    counter_sorted = sorted(counter.items(), key=lambda i: i[1], reverse=True)  # Сортируем список по значению ключей

    return counter_sorted[0][0], counter_sorted[0][1]  # Возвращаем отдельно первый ip и кол-во запросов


file = 'nginx_logs.txt'
sp_ip, count = find_spamer(file)
print(f'ip: {sp_ip}, count: {count}')

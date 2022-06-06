# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию,
# новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
#

price_list = [5.8, 46.51, 97, 56.08, 36.51, 99, 77.8, 43.31, 6, 155.2, 16.51]


def format_price(prices):
    st_prices = []
    for i in range(len(prices)):
        try:
            row = str(prices[i])
            rub, cop = map(str, row.split(".", 1))
            if len(rub) < 2:
                rub = '0' + rub
            if len(cop) < 2:
                cop += '0'
            st_prices.append(f'{rub} руб {cop} коп')
        except ValueError:
            row = str(prices[i])
            if len(row) < 2:
                rub = '0' + row
                cop = '00'
            else:
                rub = row
                cop = '00'
            st_prices.append(f'{rub} руб {cop} коп')
    return st_prices


print(format_price(price_list))

print(id(price_list))

price_list.sort()

print(format_price(price_list))

print(id(price_list))

price_list.sort(reverse=True)

desc_price_list = price_list[0:5]

desc_price_list.sort()

print(format_price(desc_price_list))




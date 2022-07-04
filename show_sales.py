import sys


def show(argv):
    if len(argv) == 1:

        with open(file_name, 'r', encoding='utf-8') as fr:
            for line in fr:
                print(line)

    elif len(argv) == 2:
        pr, par1 = argv
        i = 1
        with open(file_name, 'r', encoding='utf-8') as fr:

            for line in fr:
                if i < int(par1):
                    i += 1
                    continue
                print(line)

    elif len(argv) == 3:
        pr, par1, par2 = argv
        i = 1
        with open(file_name, 'r', encoding='utf-8') as fr:

            for line in fr:
                if int(par1) <= i <= int(par2):
                    print(line)
                    i += 1
                else:
                    i += 1
    else:
        print(f'Введите не более двух аргументов, вы ввели: {len(argv) - 1}')


file_name = 'bakery.csv'

if __name__ == '__main__':

    sys.exit(show(sys.argv))

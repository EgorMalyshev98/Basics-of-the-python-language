import sys


def add(argv):
    pr, summ = argv
    with open(file_name, 'a', encoding='utf-8') as fw:
        fw.write(str(summ) + '\n')


file_name = 'bakery.csv'

if __name__ == '__main__':

    sys.exit(add(sys.argv))

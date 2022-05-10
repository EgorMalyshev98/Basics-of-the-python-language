
def num_translate_adv(key: str) -> str:
    """Translates numbers from 1 to 10 from English into Russian"""

    dict_num = {
        "one": 'один',
        "two": 'два',
        "three": 'три',
        "four": 'четыре',
        "five": 'пять',
        "six": 'шесть',
        "seven": 'семь',
        "eight": 'восемь',
        "nine": 'девять',
        "ten": 'десять'
    }
    if key.istitle():
        return dict_num.get(key.lower()).capitalize()
    else:
        return dict_num.get(key)


print(num_translate_adv('Two'))


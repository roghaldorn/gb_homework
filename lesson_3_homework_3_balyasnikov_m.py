from random import randint


def get_jokes(number, joke_list=[], space=' '):
    """
    Gives random jokes, in the amount of input number.
    Takes an integer, output some cool jokes as list.
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    while len(joke_list) < number:
        random_number = randint(0, 4)
        joke_list.append((lambda x: nouns[x] + space + adverbs[x] + space + adjectives[x])(random_number))

    return joke_list


# print(get_jokes(3))

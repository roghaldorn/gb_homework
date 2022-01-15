def num_translate_adv(number):
    """Translate numbers with retaining upper case, takes an integer, outputs a string."""
    translate_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    if isinstance(number, str) and number.lower() in translate_dict:
        if number[0].isupper():
            return translate_dict[number.lower()].capitalize()  # adv
        else:
            return translate_dict[number.lower()]
    else:
        return None

# print(num_translate_adv('zero'))

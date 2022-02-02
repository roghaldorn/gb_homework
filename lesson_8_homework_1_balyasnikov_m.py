import re


def email_parse(mail):
    pattern = r'^(?P<username>[a-zA-Z0-9_.+-]+)@(?P<domain>[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$)'  # не увидел здесь смысла в re.compile
    if re.match(pattern, mail):
        for el in re.finditer(pattern, mail):
            result = el.groupdict()
            return result
    else:
        raise ValueError(f'Wrong e-mail: {mail}')


print(email_parse('test@test.ru'))

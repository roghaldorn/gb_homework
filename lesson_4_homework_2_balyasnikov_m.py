from sys import argv
from requests import get
from decimal import Decimal
from _datetime import datetime


def currency_rates(char_code, value=None, resp_date=None):
    """
    Displaying the current exchange rate, takes a string from CMD in format 'bar'
    """
    response = get('https://www.cbr.ru/scripts/XML_daily.asp')
    response_cont = response.content.decode(encoding=response.encoding)
    if response.status_code != 200:
        print('Response Failed')
        return False
    for content_data in response_cont.split('<CharCode>')[1:]:
        if str(char_code[0]).upper() in content_data.split('</Value>')[0]:
            value = Decimal(content_data[content_data.find('lue>') + 4:content_data.find('</Value>')].replace(',', '.'))
    for content_data in response_cont.split('Date="')[1:]:
        resp_date = datetime.strptime(content_data.split('"')[0], '%d.%m.%Y')
    return value, resp_date


print(currency_rates(argv[1:]))

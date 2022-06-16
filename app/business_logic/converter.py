import requests
import xmltodict


def parse_cbr(char_code='USD') -> float or None:
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    data = xmltodict.parse(response.content)
    list_valute = data.get('ValCurs').get('Valute')
    for value in list_valute:
        if value['CharCode'] == char_code:
            return float(value['Value'].replace(',', '.'))


def to_rub(valute_value, nominal) -> float:
    return valute_value * nominal

from functions import *


def test():
    assert search_by_code('CLP') == [
        {'position': 42, 'code': 'CLP', 'country': 'Chile', 'currency': 'Peso chileno', 'decimals': '0'}]
    assert search_by_country('Chile') == [{'position': 41, 'code': 'CLF', 'country': 'Chile', 'currency': 'Unidad de fomento', 'decimals': '4'}, {
        'position': 42, 'code': 'CLP', 'country': 'Chile', 'currency': 'Peso chileno', 'decimals': '0'}]
    assert search_by_currency('Peso Chileno') == [
        {'position': 42, 'code': 'CLP', 'country': 'Chile', 'currency': 'Peso chileno', 'decimals': '0'}]
    assert search_decimals('CLP') == 0
    assert search_by_code(
        {'CLP'}) == "El campo de consulta debe ser del tipo str"
    assert search_by_country(
        {'CLP'}) == "El campo de consulta debe ser del tipo str"
    assert search_by_currency(
        {'CLP'}) == "El campo de consulta debe ser del tipo str"
    assert search_decimals(
        {'CLP'}) == "El campo de consulta debe ser del tipo str"


if __name__ == '__main__':
    test()

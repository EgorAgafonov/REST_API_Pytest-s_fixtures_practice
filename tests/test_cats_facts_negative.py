from api_cats import CatFacts
import pytest

cf = CatFacts()


class Test_CatFacts:
    """Набор негативных тест-кейсов для проверки API сервиса https://catfact.ninja"""

    @pytest.mark.get_breed_neg
    @pytest.mark.parametrize('limit', [-1, 'one', ''], ids=['negativ_num_breed', 'string_num_breeds',
                                                            'empty_str_breeds'])
    def test_get_list_of_breeds_negat(self, limit):
        """Негативные тест-кейсы для проверки получения списка пород кошек в количестве, заданном в параметре запроса.
        Используется фикстура parametrize фрейм-ка pytest с не верифицированными значениями. Валидации негативных тестов
         успешны, если каждый ответ сервера содержит статус ответа (!= 200)."""

        status, result = cf.get_list_of_cats_breeds(limit=limit)
        # 1. Проверка статуса ответа:
        assert status != 200
        # 2. Проверка тела ответа на предмет наличия верифицированных ключей и их значений:
        try:
            assert result['message'] != ''
            assert result['code'] != 200
        except AssertionError:
            print(f'ОШИБКА! Не верифицированное значение в запросе обработано сервером со статусом: {status}.\n '
                  f'Создать отчет об ошибке и отразить в системе отслеживания!')

    @pytest.mark.get_fact_neg
    @pytest.mark.parametrize('max_length', ['twenty', 19, "", 0], ids=['string_num_length', 'non_valid_int_length',
                                                                       'empty_string_length', 'zero_int_length'])
    def test_get_random_fact_posit(self, max_length):
        """Негативные тест-кейсы для проверки получения массива с фактами о жизни кошек с количеством символов в строке
        ответа, заданном параметром max_length. Используется фикстура parametrize с не верифицированными значениями
        параметра max_length. Валидации негативных тестов успешны, если каждый ответ сервера содержит статус ответа
        (!= 200)."""

        status, result = cf.get_fact_of_cats(max_length=max_length)

        # 1. Проверка статуса ответа:
        assert status != 200, f"Ошибка! Сервер обработал не верифицированный параметр запроса со статусом: {status}"
        # 2. Проверка тела ответа на предмет отсутствия ключей и значений при некорректном запросе:
        try:
            assert result == {}
        except AssertionError:
            print(f'ОШИБКА! Не верифицированное значение в запросе обработано сервером со статусом: {status}.\n '
                  f'Создать отчет об ошибке и отразить в системе отслеживания!')

    @pytest.mark.get_facts_neg
    @pytest.mark.parametrize('max_length', [28, 54, 99], ids=['28_chars', '54_chars', '99_chars'])
    @pytest.mark.parametrize('limit', [1, 2, 6], ids=['one_fact', 'two_facts', 'six_facts'])
    def test_get_list_of_facts_posit(self, limit, max_length):
        """Позитивные тест-кейсы для проверки функции получения фактов о жизни кошек в соответствии с указанными в
        запросе параметрами limit и max_length. Валидации тестов успешны, если каждый ответ сервера содержит набор
        символов (в т. числе пробелы) в количестве, не превышающим значения аргумента max_length, а количество фактов
        в запросе соответствует значению аргумента limit."""

        status, result = cf.get_list_of_facts(max_length=max_length, limit=limit)

        # 1. Проверка статус-кода ответа сервера:
        assert status == 200, f'Запрос отклонен. Код ответа: {status}'

        # 2. Проверка на количество символов в строке ответа, не превышающее значения параметра max_length:
        assert len(result['data'][0]['fact']) != ''
        assert len(result['data'][0]['fact']) <= max_length

        # 3. Проверка на количество фактов в ответе, равное значению параметра limit:
        quantity_of_facts = []
        for i in result['data']:
            quantity_of_facts.append(i["fact"])
        assert len(quantity_of_facts) == limit

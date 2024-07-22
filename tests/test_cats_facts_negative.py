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
         успешны, если каждый ответ сервера содержит отрицательный статус ответа."""

        status, result = cf.get_list_of_cats_breeds(limit=limit)


        print(status)
        print(result)


        # assert status == 200, f'Запрос отклонен. Код ответа: {status}'
        # assert len(list_of_breeds) == limit, 'Количество пород в списке не соответствует заданному значению'

    @pytest.mark.get_fact_neg
    @pytest.mark.parametrize('max_length', [20, 50, 70], ids=['30_chars', '50_chars', '70_chars'])
    def test_get_random_fact_posit(self, max_length):
        """Позитивные тест-кейсы для проверки получения случайного факта о жизни кошек. Валидации тестов успешны,
        если каждый ответ сервера содержит строку символов (в т. числе пробелы) в количестве, не превышающим значения
        аргумента max_length."""

        status, result = cf.get_fact_of_cats(max_length=max_length)

        assert status == 200, f'Запрос отклонен. Код ответа: {status}'
        try:
            assert len(result["fact"]) <= max_length, ('ОШИБКА! Количество символов в строке ответа больше параметра '
                                                       'max_length')
            assert result["length"] <= max_length, ('ОШИБКА! Int-значение ключа length в ответе '
                                                    'больше int-значения max_length запроса')
        except KeyError:
            raise Exception("Ответ сервера не содержит данных (словарь пуст)")

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











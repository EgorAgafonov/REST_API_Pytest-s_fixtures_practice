from api_cats import CatFacts
import pytest

cf = CatFacts()


class Test_CatFacts:
    """Набор позитивных тест-кейсов для проверки API сервиса https://catfact.ninja"""

    @pytest.mark.get_breed
    @pytest.mark.parametrize('limit', [1, 2, 9], ids=['one_breed', 'two_breeds', 'three_breeds'])
    def test_get_list_of_breeds_posit(self, limit):
        """Позитивные тест-кейсы для проверки получения списка пород кошек в количестве, заданном в параметре запроса.
        Используется фикстура parametrize фрейм-ка pytest с верифицированными значениями. Валидации тестов успешны,
        если каждый ответ сервера содержит список пород кошек в количестве, соответствующим значению аргумента limit."""

        status, result = cf.get_list_of_cats_breeds(limit=limit)

        list_of_breeds = []
        for i in result["data"]:
            breed = result["data"][0]["breed"]
            list_of_breeds.append(breed)

        assert status == 200, f'Запрос отклонен. Код ответа: {status}'
        assert len(list_of_breeds) == limit, 'Количество пород в списке не соответствует заданному значению'

    @pytest.mark.get_fact
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

    @pytest.mark.get_facts
    @pytest.mark.parametrize('max_length', [19, 54, 99], ids=['19_chars', '54_chars', '99_chars'])
    @pytest.mark.parametrize('limit', [1, 2, 9], ids=['one_fact', 'two_fact', 'nine_fact'])
    def test_get_list_of_facts_posit(self, max_length, limit):
        """"""

        status, result = cf.get_list_of_facts(max_length=max_length, limit=limit)

        list_of_facts = []
        for i in result["data"]:
            fact = result["data"][0]["fact"]
            list_of_facts.append(fact)

            assert status == 200, f'Запрос отклонен. Код ответа: {status}'
        try:
            for
            assert len(result["fact"]) <= max_length, ('ОШИБКА! Количество символов в строке ответа больше параметра '
                                                       'max_length')
            assert result["length"] <= max_length, ('ОШИБКА! Int-значение ключа length в ответе '
                                                    'больше int-значения max_length запроса')
        except KeyError:
            raise Exception("Ответ сервера не содержит данных (словарь пуст)")

        assert len(list_of_facts) == limit, 'Количество фактов в списке не соответствует заданному значению'







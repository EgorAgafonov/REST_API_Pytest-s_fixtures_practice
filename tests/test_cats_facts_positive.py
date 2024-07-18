from api_cats import CatFacts
import pytest


class TestCatFacts:
    """Набор позитивных тест-кейсов для проверки API сервиса https://catfact.ninja"""

    def __init__(self):
        self.cf = CatFacts()

    @pytest.mark.one_cats
    @pytest.mark.parametrize('limit', [1, 2, 9], ids=['one_breed', 'two_breeds', 'three_breeds'])
    def test_get_list_of_breeds_positive(self, limit):
        """Позитивные тест-кейсы для проверки получения списка пород кошек в количестве, заданном в параметре запроса.
        Используется фикстура parametrize фрейм-ка pytest с верифицированными значениями. Валидации тестов успешны,
        если каждый ответ сервера содержит список пород кошек в количестве, соответствующим значению аргумента limit."""

        status, result = self.cf.get_list_of_cats_breeds(limit=limit)

        list_of_breeds = []
        for i in result["data"]:
            breed = result["data"][0]["breed"]
            list_of_breeds.append(breed)

        assert status == 200, f'Запрос отклонен. Код ответа: {status}'
        assert len(list_of_breeds) == limit, 'Количество пород в списке не соответствует заданному значению'

    @pytest.mark.two_cats
    @pytest.mark.parametrize('max_length', [30, 50, 70], ids=['30_chars', '50_chars', '70_chars'])
    def test_get_random_fact_positive(self, max_length):
        """"""

        status, result = self.cf.get_fact_of_cats(max_length=max_length)

        assert status == 200, f'Запрос отклонен. Код ответа: {status}'
        assert len(result["fact"]) <= max_length, ('ОШИБКА! Количество символов в строке ответа больше параметра '
                                                   'max_length')
        assert result["length"] <= max_length, ('ОШИБКА! Количество символов в строке ответа больше параметра '
                                                'max_length')

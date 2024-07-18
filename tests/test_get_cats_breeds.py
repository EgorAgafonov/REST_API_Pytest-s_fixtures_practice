from api_cats import CatFacts
import pytest

cf = CatFacts()


class TestCatFacts:
    """Набор позитивных тест-кейсов для проверки API сервиса https://catfact.ninja"""

    @pytest.mark.one
    @pytest.mark.parametrize('limit', [1, 2, 9], ids=['one_breed', 'two_breeds', 'three_breeds'])
    def test_get_list_of_breeds_positive(self, limit):
        """Позитивные тест-кейсы для проверки получения списка пород кошек в количестве, заданном в параметре запроса.
        Используется фикстура parametrize фрейм-ка pytest с верифицированными значениями. Валидации тестов успешны,
        если каждый ответ сервера содержит список пород кошек в количестве, соответствующим значению аргумента limit."""

        status, result = cf.get_list_of_cats_breeds(limit=limit)

        list_of_breeds = []
        for i in result["data"]:
            breed = result["data"][0]["breed"]
            list_of_breeds.append(breed)

        print(f"\n{list_of_breeds}\n")

        assert status == 200, 'Запрос отклонен'
        assert len(list_of_breeds) == limit, 'Количество пород в списке не соответствует заданному значению'






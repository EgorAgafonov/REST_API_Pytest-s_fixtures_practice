from api_cats import CatFacts
import pytest

cf = CatFacts()


class TestCatFacts:
    """"""
    @pytest.mark.one
    @pytest.mark.parametrize('limit', [1, 2, 3], ids=['one_breed', 'two_breeds', 'three_breeds'])
    def test_get_list_of_breeds_positive(self, limit):
        """Позитивные тест-кейсы для проверки получения списка пород кошек в количестве, заданном в параметре запроса.
        Используется фикстура parametrize фрейм-ка pytest с верифицированными значениями для последовательной проверки
        каждого запроса."""

        status, result = cf.get_list_of_cats_breeds(limit=limit)

        list_of_breeds = []
        for i in result["data"]:
            breed = result["data"][0]["breed"]
            list_of_breeds.append(breed)

        print(f"\n{list_of_breeds}\n")

        # assert status == 200, 'Запрос FAILED'
        # assert len(result.get('pets')) == limit, 'Количество пород в списке не соответствует заданному значению'
        # print(f"\nТестируемое значение filter = : '{filter}'")






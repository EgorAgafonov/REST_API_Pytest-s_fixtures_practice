from api import PetFriends
from conftest import *
import sys

pf = PetFriends()


class TestClass_PetFriends:
    """Коллекция авто-тестов для тестирования функции получения сведений о размещенных карточках питомцев REST API
    сервиса платформы PetFriends."""

    @pytest.mark.three
    @pytest.mark.get_info_valid
    @pytest.mark.parametrize('filter', ['', 'my_pets'], ids=['empty string', 'only my pets'])
    def test_getAllPets_valid_filter(self, get_api_key, filter):
        """Позитивный тест проверки запроса размещенных пользователем карточек питомцев. Используется фикстура
        get_api_key, как и в предыдущем тесте. В случае положительной авторизации на сайте, с помощью модуля api.py с
        классом атрибутов и методов PetFriends выполняется get-запрос на предоставление всех карточек питомцев,
        созданных пользователем, а также всех карточек, размещенных на сайте другими пользователями. С помощью фикстуры
        @pytest.mark.parametrize в параметрах запроса передаются поочередно все доступные значения фильтра - '' и
        'my_pets'. Валидация теста считается успешной в случае, если статус ответа сервера равен 200, а количество
        полученных карточек питомцев (элементов списка в json-словаре) в каждом случае больше 0."""

        status, result = pf.get_all_pets(auth_key=get_api_key, filter=filter)

        assert status == 200, 'Запрос выполнен неуспешно'
        assert len(result.get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'
        print(f"\nТестируемое значение filter = : '{filter}'")

    @pytest.mark.three
    @pytest.mark.get_info_invalid
    @pytest.mark.parametrize('filter', [strings_generator(255),
                                        strings_generator(1001),
                                        russian_chars(),
                                        russian_chars().upper(),
                                        chinese_chars(),
                                        special_chars(),
                                        digits()],
                             ids=['255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese chars',
                                  'specials', 'digits'])
    def test_getAllPets_invalid_filter(self, get_api_key, filter):
        """Негативный тест проверки запроса размещенных пользователем карточек питомцев. Используется фикстура
        get_api_key, как и в предыдущем тесте. В случае положительной авторизации на сайте, с помощью модуля api.py с
        классом атрибутов и методов PetFriends выполняется get-запрос на предоставление всех карточек питомцев,
        созданных пользователем. В параметрах запроса передаётся необходимое значение фильтра - 'my_pets'. Валидация
        теста считается успешной в случае, если статус ответа сервера равен 200, а количество полученных карточек
        питомцев (элементов списка в json-словаре) больше 0. Использование фикстуры get_api_key позволяет избежать
        многострочного кода в тестовом наборе (коллекции), делает код более лаконичным."""

        status, result = pf.get_all_pets(auth_key=get_api_key, filter=filter)

        if status == 200:
            raise Exception(f'Ошибка сервера, некорректный запрос успешно обработан! Код ответа - {status}')
        else:
            assert status != 200
            print(f'\nОжидаемый код ответа сервера: 500')
            print(f'Фактический код ответа сервера: {status}')
            print(f"Тестируемое значение filter = : '{filter}'")
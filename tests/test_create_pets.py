from api import PetFriends
from conftest import *
import sys

pf = PetFriends()


class TestClass_PetFriends:
    """Коллекция авто-тестов для тестирования функции создания карточек питомцев REST API сервиса платформы
    PetFriends."""

    @pytest.mark.one
    @pytest.mark.create_pet
    def test_create_pet_simple(self, get_api_key, name='Bruce', animal_type="bulldog", age=0.6):
        """Позитивный тест проверки размещения пользователем карточки питомца без фотографии. Для обязательной,
        предварительной авторизации пользователя на сайте перед размещением карточки c помощью библиотеки Pytest
        сначала инициализируется функция-фикстура get_api_key. В случае положительной авторизации на сайте (в
        фикстуре get_api_key реализована тестовая проверка на предмет валидации пользователя на сайте),
        с помощью модуля api.py с классом атрибутов и методов PetFriends выполняется post-запрос на размещение карточки
        с данными питомца без фото. В случае положительной авторизации на сайте, с помощью модуля api.py с
        классом атрибутов и методов PetFriends выполняется post-запрос на размещение карточки. Валидация теста
        считается успешной в случае если статус ответа сервера равен 200, а передаваемая в запросе кличка питомца
        содержится в json-ответе сервера."""

        status, result = pf.create_pet_simple(auth_key=get_api_key, name=name, animal_type=animal_type, age=age)

        assert status == 200, 'Запрос выполнен неуспешно'
        assert result['name'] == 'Bruce', 'Запрос неверный, карточка питомца не создана'

    @pytest.mark.two
    @pytest.mark.create_pet
    def test_create_pet_wth_photo(self, get_api_key, name='Tom', animal_type='yard-cat', age='2',
                                  pet_photo='images/cat1.jpg'):
        """Позитивный тест проверки размещения пользователем карточки питомца с фотографией. Используется фикстура
        get_api_key, как и в предыдущем тесте. В случае положительной авторизации на сайте, с помощью модуля api.py с
        классом атрибутов и методов PetFriends выполняется post-запрос на размещение карточки с фото. Валидация теста
        считается успешной в случае, если статус ответа сервера равен 200, а возвращаемое в ответе сервера значение
        ключа 'pet_photo' не пустое (т.е. содержит байтовое представление размещенного фото питомца)."""

        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        status, result = pf.create_pet_wth_foto(auth_key=get_api_key, name=name, animal_type=animal_type, age=age,
                                                pet_photo=pet_photo)

        assert status == 200, 'Запрос отклонен, ошибка параметров запроса.'
        assert result['pet_photo'] != '', 'Запрос отклонен, карточка питомца с фото не создана'

    # @pytest.mark.skip(reason='ВНИМАНИЕ! Тест генерирует единовременно 50 тест-кейсов(карточек питомцев), '
    #                          'исполнение в коллекции инициировать по необходимости.')
    @pytest.mark.parametrize("name", [russian_chars(),
                                      russian_chars().upper(),
                                      strings_generator(255),
                                      chinese_chars(),
                                      latin_chars()], ids=['cyrillic name', 'CYRILLIC NAME', '255 symbols name',
                                                           'chinese name', 'latin name'])
    @pytest.mark.parametrize("animal_type", [russian_chars(),
                                             russian_chars().upper(),
                                             strings_generator(255),
                                             chinese_chars(),
                                             latin_chars()],
                             ids=['cyrillic breed', 'CYRILLIC BREED', '255 symbols breed',
                                  'chinese breed', 'latin breed'])
    @pytest.mark.parametrize("age", ["1", 23.45, -1], ids=['string_age', 'float_age', 'negative_age'])
    def test_create_pet_simple_pairwise(self, get_api_key, name, animal_type, age):
        """Позитивный тест проверки размещения пользователем карточек питомцев без фотографии. С помощью фикстуры
        pytest.mark.parametrize тест генерирует карточки питомцев с заданными параметрами значений name, animal_type,
        age (прием строковых значений в различных форматах, целочисленных, дробных значений) в зависимости от
        поставленной задачи. Реализуется техника тестирования Pairwise. Ввиду отсутствия установленных ограничений на
        тип передаваемых данных, для теста достаточно положительного ответа сервера и создания карточек с указанными
        нами parametrize питомцев. В виде исключения добавлен вызов Exception в случае, если ответ сервера содержит
        отрицательное значение возраста питомца и статус-код 200. Валидация теста считается успешной если статус ответа
        сервера равен 200, а передаваемые в запросе параметры содержатся в json-ответе сервера."""

        status, result = pf.create_pet_simple(auth_key=get_api_key, name=name, animal_type=animal_type, age=age)

        if status == 200 and float(result['age']) <= 0:
            raise Exception("\nОбнаружена ошибка - возможность создания карточки питомца с отрицательным значением "
                            "возраста.\nЗанести баг в баг-трэкинговую систему и создать баг-репорт.")
        else:
            assert status == 200, 'Запрос выполнен неуспешно'
            assert result['name'] != '', 'Запрос неверный, поле "name" пустое, карточка питомца не создана'
            assert result['animal_type'] != '', 'Запрос неверный, поле "animal_type" пустое, ' \
                                                'карточка питомца не создана'
            assert result['age'] != '', 'Запрос неверный, поле "age" пустое, карточка питомца не создана'

        print(f"\nТестируемые значения:\nname: {name}, animal_type: {animal_type}, age: {age}.")

    # @pytest.mark.skip(reason='ВНИМАНИЕ! Тест генерирует единовременно 11 тест-кейсов(карточек питомцев), '
    #                          'исполнение в коллекции инициировать по необходимости.')
    @pytest.mark.parametrize("name", [''], ids=['empty'])
    @pytest.mark.parametrize("animal_type", [''], ids=['empty'])
    @pytest.mark.parametrize("age", ['', '-1', '0', '100', '1.5', '2147483647', '2147483648', special_chars(),
                                     russian_chars(), russian_chars().upper(), chinese_chars()],
                             ids=['empty', 'negative', 'zero', 'greater than max', 'float', 'int_max',
                                  'int_max + 1', 'specials', 'russian', 'RUSSIAN', 'chinese'])
    def test_create_pet_simple_negative(self, get_api_key, name, animal_type, age):
        """Негативный тест проверки размещения пользователем карточек питомцев без фотографии. Отличие от предыдущего
        теста в том, что в запросе формируются только невалидные параметры значений name, animal_type, age. Валидация
        негативного теста считается успешной, если статус ответа сервера не равен 200."""

        status, result = pf.create_pet_simple(auth_key=get_api_key, name=name, animal_type=animal_type, age=age)

        if status == 200:
            raise Exception('\nОбнаружена ошибка - возможность создания карточки питомца с невалидными значениями полей'
                            'name, animal_type, age.\nЗанести баг в баг-трэкинговую систему и создать баг-репорт.')

        assert status in range(400, 500)
        print(f"\nТестируемые значения:\nname: {name}, animal_type: {animal_type}, age: {age}.")

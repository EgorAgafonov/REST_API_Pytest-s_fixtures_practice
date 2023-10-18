from api import PetFriends
from conftest import *
import sys

pf = PetFriends()


class TestClass_PetFriends:
    """Коллекция авто-тестов для тестирования REST API сервиса платформы PetFriends. """

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

        return result

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
            raise Exception(f'Ошибка сервера, некорретный запрос успешно обработан! Код ответа - {status}')
        else:
            assert status != 200
            print(f'\nОжидаемый код ответа сервера: 500')
            print(f'Фактический код ответа сервера: {status}')
            print(f"Тестируемое значение filter = : '{filter}'")

    @pytest.mark.four
    @pytest.mark.delete_pet
    def test_delete_pet_id(self, get_api_key):
        """Позитивный тест проверки удаления карточки питомца из списка питомцев пользователя. Используется фикстура
        get_api_key, как и в предыдущем тесте. В случае положительной авторизации на сайте, с помощью модуля api.py с
        классом атрибутов и методов PetFriends выполняется delete-запрос на удаление карточки питомца по id-номеру.
        Валидация теста считается успешной в случае, если статус ответа сервера на запрос равен 200, а id-номер
        удаляемого питомца (его карточка) отсутствует в повторном get-запросе списка всех питомцев пользователя."""

        _, my_pets = pf.get_all_pets(auth_key=get_api_key, filter='my_pets')  # получаем список питомцев пользователя

        if len(my_pets[
                   'pets']) == 0:  # в случае, если у пользователя отсутствуют размещенные карточки питомцев, инициируем
            # post-запрос на добавление в профиль пользователя  карточки питомца с фото.

            pf.create_pet_wth_foto(auth_key=get_api_key, name='Charlie', animal_type='siamese', age='2',
                                   pet_photo='images/cat2.jpg')
            _, my_pets = pf.get_all_pets(auth_key=get_api_key,
                                         filter='my_pets')  # повторно запрашиваем список питомцев
            # пользователя.

        pet_id = my_pets['pets'][0][
            'id']  # получаем id-номер питомца из списка my_pets для осуществления delete-запроса.

        status = pf.delete_pet(auth_key=get_api_key, pet_id=pet_id)  # удаляем карточку питомца по id-номеру и получаем
        # статус ответа от сервера.

        _, my_pets = pf.get_all_pets(auth_key=get_api_key, filter='my_pets')  # повторно запрашиваем список питомцев
        # для проверки отсутствия удаленного питомца
        # в списке пользователя
        assert status == 200
        assert pet_id not in my_pets.values()

    # @pytest.mark.skip(reason='Метод запроса работает некорректно, выполнение теста отложено.')
    # @pytest.mark.skipif(sys.version_info > (3, 9), reason=f'Тест требует python версии 3.9'
    #                                                       f'или ниже, выполнение теста отложено.')
    # @min_python_310_required
    # @pytest.mark.xfail(sys.platform == 'win32', reason='Возможны сбои в работе и падение теста на платформе win32')
    # @pytest.mark.xfail(raises=UnboundLocalError, reason="В случае отсутствия карточки(чек) питомцев у пользователя"
    #                                                     "результат будет равен XFAIL (нечего удалять - "
    #                                                     "UnboundLocalError)!")
    @pytest.mark.five
    @pytest.mark.delete_pet
    def test_delete_all_pets(self, get_api_key):
        """Позитивный тест проверки удаления всех карточек питомцев из профиля пользователя. Используется фикстура
        get_api_key, как и в предыдущем тесте. В случае положительной авторизации на сайте, с помощью модуля api.py с
        классом атрибутов и методов PetFriends, выполняется delete-запрос на удаление карточки питомца по id-номеру.
        Валидация теста считается успешной в случае, если статус ответа сервера на delete-запрос равен 200,
        а возвращаемый сервером ответ на get-запрос с массивом размещенных пользователем питомцев является пустым(
        ключ 'pets' содержит пустой список словарей)."""

        status, result = pf.delete_all_my_pets(auth_key=get_api_key)

        assert status == 200
        assert result['pets'] == []

    # @pytest.mark.skip(reason='ВНИМАНИЕ! Тест генерирует единовременно 27 тест-кейсов(карточек питомцев), '
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
        age (прием строковых значений в различной кодировке, целочисленных или дробных(float) значений) в зависимости от
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

    @pytest.mark.parametrize("name", [''], ids=['empty'])
    @pytest.mark.parametrize("animal_type", [''], ids=['empty'])
    @pytest.mark.parametrize("age", ['', '-1', '0', '100', '1.5', '2147483647', '2147483648', special_chars(),
                                     russian_chars(), russian_chars().upper(), chinese_chars()],
                             ids=['empty', 'negative', 'zero', 'greater than max', 'float', 'int_max',
                                  'int_max + 1', 'specials', 'russian', 'RUSSIAN', 'chinese'])
    def test_add_new_pet_simple_negative(self, get_api_key, name, animal_type, age):
        """Негативный тест проверки размещения пользователем карточек питомцев без фотографии. Отличие от предыдущего
        теста в том, что в запросе формируются только невалидные параметры значений name, animal_type, age. Валидация
        негативного теста считается успешной, если статус ответа сервера не равен 200."""

        status, result = pf.create_pet_simple(auth_key=get_api_key, name=name, animal_type=animal_type, age=age)

        if status == 200:
            raise Exception('\nОбнаружена ошибка - возможность создания карточки питомца с невалидными значениями полей'
                            'name, animal_type, age.\nЗанести баг в баг-трэкинговую систему и создать баг-репорт.')

        assert status in range(400, 600)



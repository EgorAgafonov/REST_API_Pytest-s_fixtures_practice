from api import PetFriends
from conftest import *
import sys

pf = PetFriends()


class TestClass_PetFriends:
    """Коллекция авто-тестов для тестирования функции удаления карточек питомцев REST API сервиса платформы
    PetFriends."""

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
        а возвращаемый сервером ответ на get-запрос с массивом размещенных пользователем питомцев является пустым (ключ
        'pets' содержит пустой список словарей)."""

        status, result = pf.delete_all_my_pets(auth_key=get_api_key)

        assert status == 200
        assert result['pets'] == []

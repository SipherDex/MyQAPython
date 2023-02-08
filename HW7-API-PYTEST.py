import pytest
import requests

# Играемся с бесплатной апишкой для учебы CRUD
# Представим что есть у нас какой нибудь магазин животных например

# Обьявляем глобальные переменные для хранения айдишника животного и для ссылки на ресурс для удобоваримости кода,
# через фикстуры к сожалению не смог разобраться как это сделать, как я их только не тыкал, не вышло(((
pytest.idiwnik = ''
# Вставьте пожалуйста свою ссылочку и оставьте в конце /unicorns б иначе по дефолту установятся /unicorns
pytest.link = "https://crudcrud.com/api/68d79dfc333d4c55b37e77e21cf8c188/unicorns"


# Подсмотрел идею у индусов
class TestGlobal:

    def test_Create(self):
        new_animal = {"Animal": "Dog", "age": 3, "colour": "WHITE", "Name": "Alice", }
        post_request = requests.post(f"{pytest.link}/", json=new_animal)
        pytest.idiwnik = post_request.json().get("_id")
        assert post_request.status_code == 201
        assert pytest.idiwnik != ''

    def test_Read(self):
        read_request = requests.get(f"{pytest.link}/{pytest.idiwnik}")
        assert read_request.status_code == 200
        assert pytest.idiwnik in read_request.text

    def test_Update(self):
        update_animal_parameters = {"Animal": "COW", "age": 7, "colour": "BLACK", "Name": "BOB", }
        update_request = requests.put(f"{pytest.link}/{pytest.idiwnik}", json=update_animal_parameters)  #
        read_request = requests.get(
            f"{pytest.link}/{pytest.idiwnik}")  # Апдейтнуть то мы апдейтнули, но убеждаемся в том что новый результат отображается
        assert update_request.status_code == 200
        changed_data = read_request.json().get(
            "colour")  # что бы быть уверенным что животное применило изменение проверим его обновленный цвет
        assert changed_data == "BLACK"

    def test_Delete(self):
        delete_request = requests.delete(f"{pytest.link}/{pytest.idiwnik}")
        assert delete_request.status_code == 200  # Настройка сервера к сожалению не выдает ничего больше кроме кода 200 иначе добавил бы еще одну проверку

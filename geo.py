import requests


def get_atm_adress(adres):
    print(adres)
    geocoder_request = f"https://search-maps.yandex.ru/v1/?text=банкомат{adres[1]}а около {adres[0]}&type=biz&lang=ru_RU&apikey=54ce3239-5ca3-4ad0-8cd8-6618c07cb3c9"

    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()
        toponym_adress = json_response["features"][0]["properties"]["CompanyMetaData"]["address"]
        toponym_coord = json_response["features"][0]["geometry"]["coordinates"]

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        print(toponym_adress, toponym_coord)
        return toponym_adress, toponym_coord
    else:
        print("Ошибка выполнения запроса:")
        print("НЕт")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        return None


def get_coord(adres):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={adres}&format=json"

    # Выполняем запрос.
    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Полный адрес топонима:
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        # Координаты центра топонима:
        toponym_coodrinates = toponym["Point"]["pos"]
        # Печатаем извлечённые из ответа поля:
        return toponym_coodrinates
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        return None

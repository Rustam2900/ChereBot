import requests
import json

BASE_URL = 'http://localhost:8000/api/v1'


def create_user(username, name, user_id):
    url = f"{BASE_URL}/botusers/"

    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i['user_id'] == user_id:
            user_exist = True
            break
    if user_exist == False:
        requests.post(url=url, data={'username': username, 'name': name, 'user_id': user_id})
        return "Foydalanuvchi yaratildi:"
    else:
        return "Foydalanuvchi mavjud:"


def create_water(title, orders, latitude, longitude):
    url = f"{BASE_URL}/userwater/"
    response = requests.get(url=url).text
    data = json.loads(response)
    return requests.post(url=url, data={'title': title, 'orders': orders,
                                        'latitude': latitude, 'longitude': longitude})

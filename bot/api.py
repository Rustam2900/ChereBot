import requests
import json

BASE_URL = 'http://localhost:8000/api/v1'


def create_user(telegram_id, name, phone, latitude, longitude, language):
    url = f"{BASE_URL}/botusers/"

    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i['telegram_id'] == telegram_id:
            user_exist = True
            break
    if not user_exist:
        response = requests.post(url=url, data={
            'telegram_id': telegram_id,
            'name': name,
            'phone': phone,
            'latitude': latitude,
            'longitude': longitude,
            'language': language
        })
        if response.status_code == 201:
            return "Foydalanuvchi yaratildi:"
        else:
            return f"Xatolik yuz berdi: {response.text}"
    else:
        return "Foydalanuvchi mavjud:"


async def check_user_registration(telegram_id):
    url = f"{BASE_URL}/botusers/"
    response = requests.get(url=url).json()

    for user in response:
        if user['telegram_id'] == telegram_id:
            return True
    return False


def get_product():
    url = f"{BASE_URL}/product/"
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def get_operator():
    url = f"{BASE_URL}/operator/"
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

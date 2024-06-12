import requests
import json

BASE_URL = 'http://localhost:8000/api/v1'


def create_user(telegram_id, name, username, phone, latitude, longitude, language):
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
            'Username': username,
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

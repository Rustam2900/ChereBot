import requests
import json

BASE_URL = 'http://localhost:8000/api/v1'


def create_or_update_user(telegram_id, name, phone, latitude, longitude, language):
    url = f"{BASE_URL}/botusers/"

    # Get the user data
    response = requests.get(url=url).text
    data = json.loads(response)

    user_id = None
    for user in data:
        if user['telegram_id'] == telegram_id:
            user_id = user['id']
            break

    if user_id:
        # Update existing user
        update_url = f"{url}{user_id}/"
        response = requests.put(update_url, data={
            'name': name,
            'phone': phone,
            'latitude': latitude,
            'longitude': longitude,
            'language': language
        })
        if response.status_code == 200:
            return "Foydalanuvchi yangilandi."
        else:
            return f"Xatolik yuz berdi: {response.text}"
    else:
        # Create new user
        response = requests.post(url=url, data={
            'telegram_id': telegram_id,
            'name': name,
            'phone': phone,
            'latitude': latitude,
            'longitude': longitude,
            'language': language
        })
        if response.status_code == 201:
            return "Foydalanuvchi yaratildi."
        else:
            return f"Xatolik yuz berdi: {response.text}"


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


def create_order(product_name, amount):
    url = f"{BASE_URL}/order/"
    response = requests.post(url, data={
        'product_name': product_name,
        'amount': amount
    })

    if response.status_code == 201:
        return "Buyurtma yaratildi."
    else:
        return f"Xatolik yuz berdi: {response.text}"

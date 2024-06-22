import requests
import json
import aiohttp

BASE_URL = 'http://localhost:8000/api/v1'


def create_or_update_user(telegram_id, name, phone, language):
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


def create_order(user_id, product_name, amount, latitude, longitude):
    url = f"{BASE_URL}/order/"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "telegram_id": user_id,
        "product_name": product_name,
        "amount": amount,
        "latitude": latitude,
        "longitude": longitude
    }
    print(json.dumps(data))
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
    except Exception as e:
        print(e)

    if response.status_code == 201:  # 201 - Created
        return "Buyurtmangiz muvaffaqiyatli yaratildi!",
    else:
        return f"Buyurtma yaratishda xatolik yuz berdi: {response.status_code}"


async def fetch_user_orders(telegram_id):
    url = f"{BASE_URL}/order/?telegram_id={telegram_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None

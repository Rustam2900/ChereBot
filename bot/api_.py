import requests
import json
import aiohttp

BASE_URL = 'http://localhost:8000/api/v1'


def create_company(telegram_id, company_name, employee_number,
                   lifetime, company_employee_name, company_contact):
    url = f"{BASE_URL}/botcompany/"
    # Prepare data in JSON format
    data = {
        'telegram_id': telegram_id,
        'company_name': company_name,
        'employee_number': employee_number,
        'lifetime': lifetime,
        'company_employee_name': company_employee_name,
        'company_contact': company_contact

    }

    # Send POST request with JSON data
    response = requests.post(url=url, json=data)

    if response.status_code == 201:
        return "Foydalanuvchi yaratildi."
    else:
        return f"Xatolik yuz berdi: {response.status_code}, {response.json()}"


def create_user(telegram_id, name, contact,
                add_contact):
    url = f"{BASE_URL}/botusers/"

    # Prepare data in JSON format
    data = {
        'telegram_id': telegram_id,
        'name': name,
        'contact': contact,
        'add_contact': add_contact

    }

    # Send POST request with JSON data
    response = requests.post(url=url, json=data)

    if response.status_code == 201:
        return "Foydalanuvchi yaratildi."
    else:
        return f"Xatolik yuz berdi: {response.status_code}"


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def check_user_registration(session, telegram_id):
    url = f"{BASE_URL}/botusers/"
    response = await fetch(session, url)
    for user in response:
        if user['telegram_id'] == telegram_id:
            return True
    return False


async def check_company_registration(session, telegram_id):
    url = f"{BASE_URL}/botcompany/"
    response = await fetch(session, url)
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


def create_order_company(bot_company_id, product_name, amount, latitude, longitude):
    url = f"{BASE_URL}/order-company/"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "bot_company_id": bot_company_id,
        "product_name": product_name,
        "amount": amount,
        "latitude": latitude,
        "longitude": longitude
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
    except Exception as e:
        print(e)
        return f"Buyurtma yaratishda xatolik yuz berdi: {str(e)}"

    if response.status_code == 201:  # 201 - Created
        return "Buyurtmangiz muvaffaqiyatli yaratildi!"
    else:
        return f"Buyurtma yaratishda xatolik yuz berdi: {response.status_code}"


def create_order_user(bot_user_id, product_name, amount, latitude, longitude):
    url = f"{BASE_URL}/order-user/"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "bot_user_id": bot_user_id,
        "product_name": product_name,
        "amount": amount,
        "latitude": latitude,
        "longitude": longitude
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
    except Exception as e:
        print(e)
        return f"Buyurtma yaratishda xatolik yuz berdi: {str(e)}"

    if response.status_code == 201:  # 201 - Created
        return "Buyurtmangiz muvaffaqiyatli yaratildi!"
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


async def get_bot_company_id(telegram_id):
    url = f"{BASE_URL}/botcompany/{telegram_id}/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['bot_company_id', print("##############", data)]
        else:
            print(f"Failed to get bot_company_id: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching bot_company_id: {str(e)}")
        return None


async def get_bot_user_id(telegram_id):
    url = f"{BASE_URL}/botusers/{telegram_id}/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['bot_user_id']
        else:
            print(f"Failed to get bot_user_id: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching bot_user_id: {str(e)}")
        return None


def update_user_language(telegram_id, language):
    url = f"{BASE_URL}/botusers/{telegram_id}/"
    headers = {'Content-Type': 'application/json'}
    data = {
        "language": language
    }
    try:
        response = requests.patch(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json().get('message')
        else:
            return response.json().get('error')
    except Exception as e:
        print(e)
        return f"Xatolik yuz berdi: {str(e)}"


def get_user_language(telegram_id):
    url = f"{BASE_URL}/botusers/{telegram_id}/"
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('language', 'uz')
        else:
            return 'uz'
    except Exception as e:
        print(e)
        return 'uz'


def update_company_language(telegram_id, language):
    url = f"{BASE_URL}/botcompany/{telegram_id}/"
    headers = {'Content-Type': 'application/json'}
    data = {'language': language}
    try:
        response = requests.put(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception as e:
        print(f"Error updating company language: {e}")
        return False


def get_company_language(telegram_id):
    url = f"{BASE_URL}/botcompany/{telegram_id}/"
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data and 'language' in data:
                return data['language']
        return 'uz'  # Fallback to 'uz' if language is not set
    except Exception as e:
        print(f"Error fetching company language: {e}")
        return 'uz'  # Handle any exceptions by defaulting to 'uz'

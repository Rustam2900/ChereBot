import requests
import aiohttp

BASE_URL = 'http://localhost:8000/api/v1'


async def create_company(telegram_id, company_name, employee_number,
                         lifetime, company_employee_name, company_contact):
    url = f"{BASE_URL}/botcompany/{telegram_id}"

    data = {
        'telegram_id': telegram_id,
        'company_name': company_name,
        'employee_number': employee_number,
        'lifetime': lifetime,
        'company_employee_name': company_employee_name,
        'company_contact': company_contact
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json=data) as response:
            if response.status == 201:
                return "Foydalanuvchi yaratildi."
            else:
                return f"Xatolik yuz berdi: {response.status}"


async def create_user(telegram_id, name, contact, add_contact):
    url = f"{BASE_URL}/botuser/{telegram_id}"

    data = {
        'telegram_id': telegram_id,
        'name': name,
        'contact': contact,
        'add_contact': add_contact
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json=data) as response:
            if response.status == 201:
                return "Foydalanuvchi yaratildi."
            else:
                return f"Xatolik yuz berdi: {response.status}"


async def check_user_registration(session, telegram_id):
    url = f"{BASE_URL}/botuser/{telegram_id}/"
    async with session.get(url) as response:
        print(f"User registration check URL: {url}")
        print(f"User registration check response status: {response.status}")
        return response.status == 200


async def check_company_registration(session, telegram_id):
    url = f"{BASE_URL}/botcompany/{telegram_id}/"
    async with session.get(url) as response:
        print(f"Company registration check URL: {url}")
        print(f"Company registration check response status: {response.status}")
        return response.status == 200


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


async def create_order_company(bot_company_id, product_name, amount, latitude, longitude):
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
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status == 201:
                    return "Buyurtmangiz muvaffaqiyatli yaratildi!"
                else:
                    return f"Buyurtma yaratishda xatolik yuz berdi: {response.status}"
    except Exception as e:
        print(e)
        return f"Buyurtma yaratishda xatolik yuz berdi: {str(e)}"


async def create_order_user(bot_user_id, product_name, amount, latitude, longitude):
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
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status == 201:
                    return "Buyurtmangiz muvaffaqiyatli yaratildi!"
                else:
                    return f"Buyurtma yaratishda xatolik yuz berdi: {response.status}"
    except Exception as e:
        print(e)
        return f"Buyurtma yaratishda xatolik yuz berdi: {str(e)}"


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
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    print("##############", data)
                    return data['bot_company_id']
                else:
                    print(f"Failed to get bot_company_id: {response.status}")
                    return None
    except Exception as e:
        print(f"Error fetching bot_company_id: {str(e)}")
        return None


async def get_bot_user_id(telegram_id):
    url = f"{BASE_URL}/botusers/{telegram_id}/"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    print("##############", data)
                    return data['bot_user_id']
                else:
                    print(f"Failed to get bot_company_id: {response.status}")
                    return None
    except Exception as e:
        print(f"Error fetching bot_company_id: {str(e)}")
        return None

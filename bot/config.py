from dotenv import dotenv_values

envfile = dotenv_values(".env")
# admin_id = envfile['ADMIN_ID']
bot_token = envfile['BOT_TOKEN']

# lang_text = 'Select a language\n\nВыберите языкn\n\nTilni tanglang'
#
#
# def uz_text(message):
#     return f'👋Assalomu alaykum <b>{message.from_user.full_name}</b>\n\n🔹Sizga kerakli bo\'limni tanlang'
#
#
# def en_text(message):
#     return f'👋Hello, <b>{message.from_user.full_name}</b>\n\n🔹Choose the section you need'
#
#
# def ru_text(message):
#     return f'👋Здравствуйте, <b>{message.from_user.full_name}</b>\n\n🔹Выберите нужный вам раздел'




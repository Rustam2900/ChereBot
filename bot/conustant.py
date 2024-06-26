### - - - - - - - - - - MENYU - - - - - - - - - - ###
from bot.api_ import get_operator

y = get_operator()
MAIN_TEXT = "Assalom  botga xush kelibsiz "
SETTINGS = "⚙️ Sozlamalar"
MY_ORDERS = "📖 Mening buyurtmalarim"
OPERATOR = "📞 Operator bilan ulashish"
ORDERS = "🛒 Buyurtma berish"

### - - - - - - - - - - TEXT - - - - - - - - - - ###

OPERATOR_TEXT = (f"{y[0]['text']} \n\n"
                 f"number: {y[0]['operator_phone']}")
LOCATION = 'location yuborish'

BACK = "⬅️ Orqaga"
LANG_CHANGE = "🇺🇿🇷🇺🇬🇧 Tilni o‘zgartirish"

### - - - - - - - - TEXT RU - - - - - - - - - - ###
MAIN_TEXT_RU = "Привет и добро пожаловать в бот "
SETTINGS_RU = "⚙️ Настройки"
MY_ORDERS_RU = "📖 Мои заказы"
OPERATOR_RU = "📞 Поделитесь с оператором"
ORDERS_RU = "🛒 Разместить заказ"
LOCATION_RU = 'Отправить местоположение'
BACK_RU = "⬅️ Назад"
LANG_CHANGE_RU = "🇺🇿🇷🇺🇬🇧 Изменить язык"

### - - - - - - - - TEXT EN - - - - - - - - - - ###
MAIN_TEXT_EN = "Hello and welcome to the bot"
SETTINGS_EN = "⚙️ Settings"
MY_ORDERS_EN = "📖 My orders"
OPERATOR_EN = "📞 Share with the operator"
ORDERS_EN = "🛒 Share with the operator"
LOCATION_EN = 'Send location'
BACK_EN = "⬅️ Back"
LANG_CHANGE_EN = "🇺🇿🇷🇺🇬🇧 Change language"

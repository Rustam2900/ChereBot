### - - - - - - - - - - MENYU - - - - - - - - - - ###
from bot.api import get_operator

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
LOCATION_CHANGE = "location o'zgartirish"

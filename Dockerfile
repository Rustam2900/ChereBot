# Asosiy image sifatida Python 3.11 dan foydalanamiz
FROM python:3.11

# Ishchi katalogni belgilaymiz
WORKDIR /app

# Loyihaning kodlarini konteyner ichiga nusxalaymiz
COPY . /app

# Kerakli kutubxonalarni o'rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# Portni ochamiz (Django ilovasi uchun 8000-port)
EXPOSE 8000

# Ishga tushirish skriptini qo'shamiz
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Entrypoint skriptini ishga tushiramiz
ENTRYPOINT ["/entrypoint.sh"]


#!/bin/sh

# Django migratsiyalarini bajarish
RUN python manage.py migrate

# Django serverini ishga tushirish
RUN python manage.py runserver 0.0.0.0:8000 &

# Botni ishga tushirish
RUN python main.py

# Konteynerni ochiq tutish uchun
tail -f /dev/null

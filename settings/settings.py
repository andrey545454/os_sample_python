# файл с данными для работы бота с группой
import os
token = str(os.environ.get('token'))  # ключ доступа к сообществу
confirmation_token = str(os.environ.get('confirmation_token'))  # ключ для настройки сервера с callback api
RLApi_token= str(os.environ.get('RLApi_token'))  # ключ для доступа к rocket league stats api
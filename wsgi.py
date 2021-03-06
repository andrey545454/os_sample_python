# Мой файл для работы Flask приложения
from flask import Flask, request, json, render_template
import messageHandler
from stat_finder.datachecker import in_blacklist
from settings.BD import get_info
from settings.settings import token, confirmation_token

application = Flask(__name__)


# декорирование функции для работы с пост запросами
@application.route("/bot", methods=['POST'])
def proccessing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        # получаем информацию из чёрного списка
        mas = get_info('black')
        user_id = data['object']['from_id']
        # если пользователь в чёрном списке-игнорим
        if in_blacklist(str(user_id), mas):
            return 'ok'
        # иначе отвечаем
        else:
            messageHandler.create_answer(data['object'], token)
            return 'ok'


# по приколу сделал
@application.route("/")
def table():
    # масив данных из бд
    mas = get_info('bd')

    def sorting(mas):
        """сортировка по количеству команд отправленных пользователем"""
        return mas[-1]
    # делаем массив от большего значения команд до меньшего значения
    mas.sort(key=sorting, reverse=True)
    # рендерим страничку
    return render_template('start_page.html', mas=mas)


# запуск приложения
if __name__ == "__main__":
    application.run()

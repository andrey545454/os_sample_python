import command_system

def hello(token,user_id,stroka='',peer_id=''):
    message = 'Офф. группа бота(подписывайся): https://vk.com/club168452415(бот переходит на новый хостинг - ждите)'
    return message, ''

hello_command = command_system.Command()

hello_command.keys = ['!бот','!bot']
hello_command.description = 'Поприветствую тебя'
hello_command.process = hello
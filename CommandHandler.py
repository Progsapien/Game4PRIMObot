import telebot
from Command import Command
from CommandExecutor import CommandExecutor

class CommandHandler:

    def __init__(self, bot):
        if(type(bot) == telebot.TeleBot):
            self.__bot = bot

    def start_handle(self):

        @self.__bot.message_handler(commands=['start'])

        def handle_standard_command(message):

            command = Command()
            command.type = Command.CommandType.STANDARD_COMMAND
            command.message = message
            command.bot = self.__bot
            CommandExecutor.execute_command(command)

        self.__bot.polling(none_stop=True)




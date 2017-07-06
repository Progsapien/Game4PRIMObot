from enum import Enum
import telebot

class Command:

    def __init__(self):
        self.__type = ""

    class CommandType(Enum):
        STANDARD_COMMAND = 1
        BUTTON_COMMAND = 2
        WORD_COMMAND = 3

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if(type(value) == Command.CommandType):
            self.__type = value

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if (type(value) == telebot.types.Message):
            self.__message = value

    @property
    def bot(self):
        return self.__bot

    @bot.setter
    def bot(self, value):
        if (type(value) == telebot.TeleBot):
            self.__bot = value

    @property
    def callback(self):
        return self.__callback

    @callback.setter
    def callback(self, value):
            self.__callback = value

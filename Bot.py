import telebot

class Bot:

    def __init__(self, token):
        self.token = token
        self.__bot = self.__init_bot()

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, value):
        if(type(value) == str):
            self.__token = value

    @property
    def bot(self):
        return self.__bot

    def __init_bot(self):
        return telebot.TeleBot(self.token)
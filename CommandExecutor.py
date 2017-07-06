from Command import Command
from StandardCommandExecutor import *
import UserState

class CommandExecutor:

    @staticmethod
    def execute_command(command):

        if(command.type == Command.CommandType.STANDARD_COMMAND):
            CommandExecutor.standard_command(command)
        elif(command.type == Command.CommandType.BUTTON_COMMAND):
            CommandExecutor.button_command(command)
        elif(command.type == Command.CommandType.WORD_COMMAND):
            CommandExecutor.word_command(command)

    @staticmethod
    def standard_command(command):
        if(command.message.text == "/start"):
            StandardCommandExecutor.start_command_execute(command)

    @staticmethod
    def button_command(command):
        pass

    @staticmethod
    def word_command(command):
        if(UserState)


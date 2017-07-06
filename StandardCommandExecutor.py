import Answers

class StandardCommandExecutor:

    @staticmethod
    def start_command_execute(command):
        command.bot.send_message(command.message.from_user.id, Answers.start_command_answer())
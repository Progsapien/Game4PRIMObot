from Bot import Bot
from CommandHandler import CommandHandler

bot = Bot("350263518:AAHTcAESb1VKuAT3cgiks0PMNPSinWlAs2I")

handler = CommandHandler(bot.bot)
handler.start_handle()
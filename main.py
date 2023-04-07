import telebot

token = "6085834593:AAEzeDCjcS3ilz5ZVGryPnEHPwgu2omkTQQ"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')


bot.infinity_polling()

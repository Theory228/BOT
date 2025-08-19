import telebot
from telebot import types

bot = telebot.TeleBot('8361818903:AAFMECArY40OGAqKRaJUHPd3sfGMhEoJXOI')



#@Roman_Testoviy_Bot
#сам /\
#бот ||


@bot.message_handler(commands='start')
def ma(mes):
   markup = types.InlineKeyboardMarkup()
   btn1 = types.InlineKeyboardButton('нажми сюда', url="https://yandex.ru/video/preview/7548887151231436014")
   markup.row(btn1)
   bot.reply_to(mes, 'выбирай:', reply_markup=markup)




bot.polling(none_stop=True)
import telebot
from googletrans import Translator

# Bot tokeningizni shu yerga kiritamiz
bot = telebot.TeleBot("6232466271:AAE3AVTn9hgoG0j6ryjgJXfOHcSzw_dphzU")

translator = Translator()

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    try:
        # Xabarni ingliz tiliga tarjima qilamiz
        translated = translator.translate(message.text, dest='uz')
        bot.reply_to(message, translated.text)
    except Exception as e:
        bot.reply_to(message, 'Kechirasiz, xatolik yuz berdi: {}'.format(e))

bot.polling()
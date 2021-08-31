import random

import telebot

from src.conf import BOT_TOKEN, compliments, poetry

bot = telebot.TeleBot(BOT_TOKEN)

kris_id = 953399899
my_id = 733781138


@bot.message_handler(content_types=['text'], regexp='Комплимент')
def get_compliment_message(message):
    if message.from_user.id == my_id or message.from_user.id == kris_id:
        compliment = random.choice(compliments)
        bot.send_message(message.from_user.id, compliment)


@bot.message_handler(content_types=['text'], regexp='Стих')
def get_poem_message(message):
    if message.from_user.id == my_id or message.from_user.id == kris_id:
        poem = random.choice(poetry)
        bot.send_message(message.from_user.id, poem)


@bot.message_handler(content_types=['text'], regexp='Самая красивая')
def get_super_beautifully_message(message):
    if message.from_user.id == my_id or message.from_user.id == kris_id:
        bot.send_photo(message.from_user.id, open("./кристина.jpg", 'rb'))


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)

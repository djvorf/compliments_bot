import random

import telebot

from src.conf import BOT_TOKEN, MY_ID, KRIS_ID, compliments, poetry

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(content_types=['text'], regexp='Комплимент')
def get_compliment_message(message):
    if str(message.from_user.id) == MY_ID or message.from_user.id == KRIS_ID:
        compliment = random.choice(compliments)
        bot.send_message(message.from_user.id, compliment)


@bot.message_handler(content_types=['text'], regexp='Стих')
def get_poem_message(message):
    if str(message.from_user.id) == MY_ID or message.from_user.id == KRIS_ID:
        poem = random.choice(poetry)
        bot.send_message(message.from_user.id, poem)


@bot.message_handler(content_types=['text'], regexp='Самая красивая')
def get_super_beautifully_message(message):
    if str(message.from_user.id) == MY_ID or message.from_user.id == KRIS_ID:
        bot.send_photo(message.from_user.id, open("./кристина.jpg", 'rb'))


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)

import random
import telebot

TOKEN = 'ВАШ ТОКЕН'

bot = telebot.TeleBot(TOKEN, parse_mode=None)

def game_of_some_valuses(a):
    a1 = 'камень'
    a2 = 'ножницы'
    a3 = 'бумага'
    matr = [a1, a2, a3]
    ans = random.choice(matr)
    if a == a1 and ans == a3:
        return f'у меня {ans} ---- ПРОИГРЫШ'
    if a == a1 and ans == a2:
        return f'у меня {ans} ---- ПОБЕДА'
    if a == a2 and ans == a1:
        return f'у меня {ans} ---- ПРОИГРЫШ'
    if a == a2 and ans == a3:
        return f'у меня {ans} ---- ПОБЕДА'
    if a == a3 and ans == a2:
        return f'у меня {ans} ---- ПРОИГРЫШ'
    if a == a3 and ans == a1:
        return f'у меня {ans} ---- ПОБЕДА'
    if a == ans:
        return f'у меня {ans} ---- НИЧЬЯ'
    elif a not in matr:
        return 'ВВЕДИ НОРМАЛЬНО'


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'Сыграем в камень ножницы бумага? Нужно писать "камень", "ножницы", "бумага"')


@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    bot.reply_to(message, game_of_some_valuses(message.text))


bot.infinity_polling()

import telebot
from telebot import types
bot = telebot.TeleBot("1543078251:AAHCkuKqo_0cjDUJe-AxS5mK7ViTukwCeLY") 

city1 = ''

startmarkup = types.ReplyKeyboardMarkup()
startmarkup.add('New game', 'Join game')

currentUser = 0
users = []

# def nextUser(users):
#     if i < len(users):
#         return i + 1
#     else:
#         return 0
#     i += 1
def citycheck(city1, city2):
    if city1[-1] in 'ьъы':
        return city1[-2] == city2[0].lower()
    else:
        return city1[-1] == city2[0].lower()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome', reply_markup=startmarkup)

@bot.message_handler(func=lambda message: message.text == 'New game')
def new_game(message):
    global users
    users.append(message.chat.id)
    bot.reply_to(message, 'Введите первый город', reply_markup=None)

@bot.message_handler(func=lambda message: message.text == 'Join game')
def join_game(message):
    global users
    users.append(message.chat.id)
    bot.reply_to(message, 'Игра начата, ходит первый игрок', reply_markup=None)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global currentUser, users, city1
    if len(users) == 1:
        bot.send_message(message.chat.id, 'Не хватает игроков')
    else:
        if currentUser < len(users):
            if city1 == '':
                city1 = message.text
                currentUser += 1
                bot.send_message(users[currentUser], city1 + ':\nВведите следующий город')
            else:
                if citycheck(city1, message.text):
                    city1 = message.text
                    bot.send_message(users[currentUser + 1], city1 + ':\nВведите следующий город')
                    currentUser += 1
                else:
                    bot.send_message(users[currentUser], 'Введен не правильный город, повторите: ')
        else:
            currentUser = 0
            if citycheck(city1, message.text):
                city1 = message.text
                bot.send_message(users[currentUser + 1], city1 + ':\nВведите следующий город')
                currentUser += 1
            else:
                bot.send_message(users[currentUser], 'Введен не правильный город, повторите: ')
bot.polling()
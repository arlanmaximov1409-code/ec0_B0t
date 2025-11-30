
import telebot
bot = telebot.TeleBot(TOKEN)
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

@bot.message_handler(commands=['start'])
def start_send(message):
    bot.reply_to(message, f'Hello I am {bot.get_me().first_name}!, I am eco bot made for special tasks, available commands: /start, /ideas')

@bot.message_handler(commands=['ideas'])
def ideas_send(message):
    bot.send_message(message.chat.id, 'Here are some ideas that you can use to make our planet a little bit cleaner')
    bot.send_message(message.chat.id, '1) Try sorting your trash by Plastic, Glass, Food Wastes, Paper 2)Utilize batteries and other special wastes in special trash cans 3) Try making youself challenges, example: week without plastic stuff')

bot.message_handler(commands=['eco_poll'])
def eco_poll(message):
    bot.send_message(message.chat.id, 'Be honest please , do you utilize batteries and other special wastes in special trash cans?')
    keys = InlineKeyboardMarkup()
    keys.add(
        InlineKeyboardButton('Yes', callback_data='1'),
        InlineKeyboardButton('No', callback_data='2'))
    bot.send_message(message.chat.id, 'ANSWER', reply_markup=keys)
@bot.callback_query_handler(func=lambda x: True)
def send_answer(call):
    if call.data == '1':
        bot.send_message(call.from_user.id, 'Yay you are doing right!')
    else:
        bot.answer_callback_query(call.id, 'Are you serious right now? ', show_alert=True)



bot.polling()

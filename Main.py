import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types
import constants
import parsing

bot = telebot.TeleBot(constants.token)
upd = bot.get_updates()
def log(message, answer):
    print("\n")
    from datetime import datetime
    print(datetime.now())
    print("Message from {0} {1}. (id = {2}) \n Text: {3}".format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text))
    print(answer)


print('hello')
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row('FAQ', 'Error', 'Questions', 'Contacts')
FAQlist = parsing.parseFAQ()

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, 'Welcome', reply_markup=markup)

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "help")

#inline keyboard
@bot.message_handler(content_types=['text'])
def handle_text(message):
    keyboard = types.InlineKeyboardMarkup()
    if message.text == 'FAQ':
        i = 0
        while i < len(FAQlist):

            keyboard.add(InlineKeyboardButton(text=FAQlist[i][0],
                                              callback_data=i.__str__()))
            i += 1

    #start message - Please choose and next inline keyboard add
        bot.send_message(message.chat.id, text="FAQ:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="*" + FAQlist[int(call.data)][0] +
                               '*\n\n' + FAQlist[int(call.data)][1], parse_mode="Markdown")
       # bot.send_message(chat_id=call.message.chat.id, message_id=markdown, parse_mode="Markdown")
bot.polling(none_stop = True, interval = 0)

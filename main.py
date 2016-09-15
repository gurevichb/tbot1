import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, MessageEntity
from telebot import types
from constants import constants
import parsing

bot = telebot.TeleBot(constants.token)
update = bot.get_updates()
faq_list = None
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row(constants.faq_button, constants.error_button,
           constants.questions_button, constants.contacts_button)

@bot.message_handler(commands=['/start'])
def handle_start(message):
    bot.send_message(message.from_user.id, 'Welcome', reply_markup=markup)

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, 'help')

@bot.message_handler(commands=['contacts'])
def handle_text(message):
    print('hello')
    pass

@bot.message_handler(content_types=['text'])
def handle_text(message):

    if message.text == constants.faq_button:
        keyboard = InlineKeyboardMarkup()
        global faq_list
        faq_list = parsing.parse_faq()
        for record in faq_list:
            keyboard.add(InlineKeyboardButton(text=str(record[0]),
                                              callback_data=str(faq_list.index(record))))
        bot.send_message(message.chat.id, text=constants.faq_button, reply_markup=keyboard)

    if message.text == constants.contacts_button:
        contacts_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        contacts_keyboard.row(constants.contact_address_button,
                   constants.contact_map_button,
                   constants.contact_reach_button,
                   constants.contact_back_button)
        contacts_ = parsing.parse_contacts()




@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # * - текст жирным используется parse_mode='Markdown'
    record_index = int(call.data)
    question = '*' + faq_list[record_index][0] + '*' + '\n\n'
    answer = faq_list[record_index][1]
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=question + answer, parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)

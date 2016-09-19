import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types
from constants import Constants
import parsing
import logger

bot = telebot.TeleBot(Constants.token)
main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.row(Constants.faq_button, Constants.error_button,
                  Constants.questions_button, Constants.contacts_button)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, Constants.start_message, reply_markup=main_keyboard)
    logger.info(str(message.from_user.id) + ' ' + message.text)
    logger.info('from id: %d, name: %s text: %s' % (message.from_user.id, 'A', message.text))


def faq_handler(message):
    if message.text == Constants.faq_button:
        keyboard = InlineKeyboardMarkup()
        try:
            faq_list = parsing.parse_faq()
        except parsing.error.URLError:
            bot.send_message(message.chat.id, text='Нет доступа.')
            logger.warning('Is not access to site: ' + Constants.site_faq)
            return
        for record in faq_list:
            keyboard.add(InlineKeyboardButton(text=str(record[0]),
                                              callback_data=str(faq_list.index(record))))
        bot.send_message(message.chat.id, text=Constants.faq_button, reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            record_index = int(call.data)
            question = '*' + faq_list[record_index][0] + '*' + '\n\n'
            answer = faq_list[record_index][1]
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=question + answer, parse_mode='Markdown')


def contacts_handler(message):
    try:
        contacts_text = parsing.parse_contact()
        how_to_reach_text = parsing.parse_how_to_reach()
    except parsing.error.URLError:
        bot.send_message(message.chat.id, text=Constants.error_message)
        logger.warning('Is not access to site: ' + Constants.site_contacts + ' parsing cancelled')
        return

    if message.text == Constants.contacts_button:
        contacts_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        contacts_keyboard.row(Constants.contact_address_button,
                              Constants.contact_reach_button,
                              Constants.contact_back_button)
        bot.send_message(message.from_user.id, text=contacts_text,
                         reply_markup=contacts_keyboard, parse_mode='Markdown')

    if message.text == Constants.contact_address_button:
        bot.send_message(message.from_user.id, text=contacts_text, parse_mode='Markdown')
    if message.text == Constants.contact_reach_button:
        bot.send_message(message.from_user.id, text=how_to_reach_text, parse_mode='Markdown')
    if message.text == Constants.contact_back_button:
        handle_start(message)


def error_code_handler(message):
    if message.text == Constants.error_button:
        contacts_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        contacts_keyboard.row(Constants.contact_back_button)
        bot.send_message(message.from_user.id, text='Введите номер ошибки',
                         reply_markup=contacts_keyboard, parse_mode='Markdown')
        # ?


@bot.message_handler(content_types=['text'])
def handle_text(message):
    faq_handler(message)
    contacts_handler(message)
    error_code_handler(message)


def main():
    bot.polling()


if __name__ == "__main__":
    main()

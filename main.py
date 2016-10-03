import logging
import sys
import threading

from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardHide
from telegram.ext import (Updater, CommandHandler, RegexHandler,
                          ConversationHandler, CallbackQueryHandler)

import parsing
import tags
from constants import Constants
from updating import UpdateData

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

START, CONTACTS, FAQ, ERROR, QUESTION = range(5)
update_data = UpdateData()


def start(bot, update):
    main_keyboard = [[Constants.faq_button, Constants.error_button,
                      Constants.questions_button, Constants.contacts_button]]
    bot.send_message(update.message.chat_id, text=Constants.start_message,
                     reply_markup=ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True))
    logger.info('from id: %d, text: %s' % (update.message.from_user.id, update.message.text))
    return START


def faq_handler(bot, update):
    keyboard = [[]]
    faq_list = update_data.get_faq_list()
    for record in faq_list:
        keyboard.append([InlineKeyboardButton(text=str(record[0]),
                                              callback_data=str(faq_list.index(record)))])
    faq_markup = InlineKeyboardMarkup(keyboard)
    bot.sendMessage(update.message.chat_id, text=Constants.faq_button, reply_markup=faq_markup)


def callback_faq(bot, update):
    faq_list = update_data.get_faq_list()
    call = update.callback_query
    question_text = '*' + faq_list[int(call.data)][0] + '*\n\n'
    answer_text = faq_list[int(call.data)][1]
    bot.edit_message_text(text=question_text + answer_text,
                          chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          parse_mode='Markdown')


def error_code_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Введите код ошибки:',
                    reply_markup=ReplyKeyboardHide())

    return ERROR


def error_handler_cycle(bot, update):
    error_links = update_data.get_knowledge_error_links()
    list_of_names_and_links = parsing.search_in_page(update.message.text, error_links)
    inline_error_keyboard = [[]]
    if list_of_names_and_links and len(list_of_names_and_links) < 15:
        logger.info('Found: ' + str(len(list_of_names_and_links)))
        for record in list_of_names_and_links:
            inline_error_keyboard.append([InlineKeyboardButton(text=str(record[0]),
                                                               url=record[1])])
        links_markup = InlineKeyboardMarkup(inline_error_keyboard)

        bot.sendMessage(update.message.chat_id, text='Найдено:', reply_markup=links_markup, resize_keyboard=True)
        bot.send_message(update.message.chat_id, text='Повторить?',
                         reply_markup=ReplyKeyboardMarkup([['Повторить', 'Назад']], resize_keyboard=True))
    else:
        bot.send_message(update.message.chat_id, text='Не найдено, повторить?',
                         reply_markup=ReplyKeyboardMarkup([['Повторить', 'Назад']], resize_keyboard=True))

    return ERROR


def contacts_handler(bot, update):
    logger.info('contact_handler')
    contacts_text = update_data.get_contacts_text()
    contacts_keyboard = [[Constants.contact_address_button,
                          Constants.contact_reach_button,
                          Constants.contact_back_button]]
    bot.send_message(update.message.chat_id, text=contacts_text,
                     reply_markup=ReplyKeyboardMarkup(contacts_keyboard, resize_keyboard=True),
                     parse_mode='Markdown')
    return CONTACTS


def contacts_reach_handler(bot, update):
    logger.info('contact_reach_handler')
    contacts_how_reach = update_data.get_contacts_how_reach()
    contacts_keyboard = [[Constants.contact_address_button,
                          Constants.contact_reach_button,
                          Constants.contact_back_button]]
    bot.send_message(update.message.chat_id, text=contacts_how_reach,
                     reply_markup=ReplyKeyboardMarkup(contacts_keyboard, resize_keyboard=True),
                     parse_mode='Markdown')


def question_handler(bot, update):
    logger.info('question')
    bot.sendMessage(chat_id=update.message.chat_id, text='Введите вопрос:',
                    reply_markup=ReplyKeyboardHide())
    return QUESTION


def question_handler_cycle(bot, update):
    logger.info(update.message.text.split())
    links_with_tags = update_data.get_links_with_tags()
    try:
        inline_question_keyboard = [[]]
        for record in tags.get(update.message.text.split(), links_with_tags):
            name_article = str(str(record[0][-6:]) + ' ')
            inline_question_keyboard.append(
                [InlineKeyboardButton(text=str(name_article + str(record[1:])[1:-1]),
                                      url=record[0])])
        links_markup = InlineKeyboardMarkup(inline_question_keyboard)
        bot.send_message(update.message.chat_id, text='Повторить?',
                         reply_markup=ReplyKeyboardMarkup([['Повторить', 'Назад']], resize_keyboard=True))

        bot.sendMessage(update.message.chat_id, text='Найдено:', reply_markup=links_markup, resize_keyboard=False)
        logger.info(tags.get(update.message.text.split(), links_with_tags))
        return QUESTION
    except IndexError:
        bot.send_message(update.message.chat_id, text='Не найдено, повторить?',
                         reply_markup=ReplyKeyboardMarkup([['Повторить', 'Назад']], resize_keyboard=True))

    return QUESTION


def main(arg_update_time):
    updater = Updater(Constants.token)

    dp = updater.dispatcher

    t2 = threading.Thread(target=update_data.update, args=[int(arg_update_time)])
    t2.setDaemon(True)
    t2.start()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                      RegexHandler(Constants.faq_button, faq_handler),
                      CallbackQueryHandler(callback_faq),
                      RegexHandler(Constants.error_button, error_code_handler),
                      RegexHandler(Constants.contacts_button, contacts_handler),
                      RegexHandler(Constants.questions_button, question_handler), ],

        states={
            START: [RegexHandler('.{0,10}', start)],

            ERROR: [RegexHandler(Constants.contact_back_button, start),
                    RegexHandler('Повторить', error_code_handler),
                    RegexHandler('.{0,10}', error_handler_cycle)],
            CONTACTS: [RegexHandler(Constants.contact_back_button, start),
                       RegexHandler(Constants.contact_address_button, contacts_handler),
                       RegexHandler(Constants.contact_reach_button, contacts_reach_handler)],
            QUESTION: [RegexHandler(Constants.contact_back_button, start),
                       RegexHandler('Повторить', question_handler),
                       RegexHandler('.{0,10}', question_handler_cycle)]
        },
        allow_reentry=True,

        fallbacks=[RegexHandler('.{0,10}', start)]
    )
    dp.add_handler(conv_handler)
    updater.start_polling()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        update_time = 60 * 60 * 24
    else:
        update_time = sys.argv[1]

    logger.info('update time: ' + str(update_time))
    main(update_time)

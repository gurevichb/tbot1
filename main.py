from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardHide
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler, CallbackQueryHandler)
from constants import Constants
import logging
import parsing
import testing
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# TODO: thread.  parse_knowledge_links, parse_error_links
faq_list = parsing.parse_faq()
#
START, FAQ, ERROR = range(3)


def start(bot, update):
    main_keyboard = [[Constants.faq_button, Constants.error_button,
                      Constants.questions_button, Constants.contacts_button]]
    bot.send_message(update.message.chat_id, text=Constants.start_message,
                     reply_markup=ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True))
    logger.info('from id: %d, text: %s' % (update.message.from_user.id, update.message.text))


def faq_handler(bot, update):
    keyboard = [[]]
    for record in faq_list:
        keyboard.append([InlineKeyboardButton(text=str(record[0]),
                                              callback_data=str(faq_list.index(record)))])
    faq_markup = InlineKeyboardMarkup(keyboard)
    bot.sendMessage(update.message.chat_id, text=Constants.faq_button, reply_markup=faq_markup)


def callback_faq(bot, update):
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
    list_of_names_and_links = parsing.search_in_page(update.message.text)
    logger.info('Found: ' + str(list_of_names_and_links))
    inline_error_keyboard = [[]]
    if list_of_names_and_links:
        for record in list_of_names_and_links:
            inline_error_keyboard.append([InlineKeyboardButton(text=str(record[0]),
                                                               url=record[1])])
        links_markup = InlineKeyboardMarkup(inline_error_keyboard)
        bot.send_message(update.message.chat_id, text='Повторить?',
                         reply_markup=ReplyKeyboardMarkup([['Повторить', 'Назад']], resize_keyboard=True))
        bot.sendMessage(update.message.chat_id, text='Найдено:', reply_markup=links_markup)
    else:
        bot.send_message(update.message.chat_id, text='Не найдено, Повторить?',
                         reply_markup=ReplyKeyboardMarkup([['Повторить', 'Назад']], resize_keyboard=True))

    return ERROR


def main():
    updater = Updater(Constants.token)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                      RegexHandler('Вопрос-ответ', faq_handler),
                      CallbackQueryHandler(callback_faq),
                      RegexHandler('Ошибки', error_code_handler)],

        states={

            ERROR: [RegexHandler('Назад', start),
                    RegexHandler('Повторить', error_code_handler),
                    RegexHandler('.{0,10}', error_handler_cycle)]
        },
        allow_reentry=True,
    )
    dp.add_handler(conv_handler)
    updater.start_polling()


if __name__ == '__main__':
    main()

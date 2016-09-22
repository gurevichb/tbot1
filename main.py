#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
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
FAQ, ERROR = range(2)


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
    print('error_code_handler')
    bot.sendMessage(chat_id=update.message.chat_id, text='Введите код ошибки:')


    # for local_update in bot.getUpdates(offset=update, timeout=10):
    #     print('hello')
    #     chat_id = update.message.text
    #     update = update.update_id + 1
    #     if local_update.message:
    #         bot.sendMessage(chat_id=chat_id, text=update.message.text)

    return ERROR


def error_handler_cycle(bot, update):
    print(update.message.text)
    time.sleep(2)
    return ERROR


def error_handler_cycle_out(bot, update):
    print('from cycle_out')


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation." % user.first_name)
    bot.sendMessage(update.message.chat_id,
                    text='Bye! I hope we can talk again some day.')

    return ConversationHandler.END


def main():
    updater = Updater(Constants.token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                      RegexHandler('Вопрос-ответ', faq_handler),
                      CallbackQueryHandler(callback_faq),
                      RegexHandler('Ошибки', error_code_handler)],

        states={

            ERROR: [RegexHandler('.{0,10}', error_handler_cycle),
                    RegexHandler('Назад', start)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dp.add_handler(conv_handler)
    updater.start_polling()


if __name__ == '__main__':
    main()

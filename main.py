from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardHide
from telegram.ext import (Updater, CommandHandler, RegexHandler,
                          ConversationHandler, CallbackQueryHandler)
from constants import Constants
import logging
import parsing

from updating import UpdateData
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

CONTACTS, FAQ, ERROR = range(3)
update_data = UpdateData()
faq_list = update_data.get_faq_list()
contacts_text = update_data.get_contacts_text()
contacts_how_reach = update_data.get_contacts_how_reach()
error_links = update_data.get_knowledge_error_links()

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
        bot.send_message(update.message.chat_id, text='Не найдено, Повторить?',
                         reply_markup=ReplyKeyboardMarkup([['Повторить', 'Назад']], resize_keyboard=True))

    return ERROR


def contacts_handler(bot, update):
    logger.info('contact_handler')
    contacts_keyboard = [[Constants.contact_address_button,
                          Constants.contact_reach_button,
                          Constants.contact_back_button]]
    bot.send_message(update.message.chat_id, text=contacts_text,
                     reply_markup=ReplyKeyboardMarkup(contacts_keyboard, resize_keyboard=True),
                     parse_mode='Markdown')
    return CONTACTS


def contacts_reach_handler(bot, update):
    logger.info('contact_reach_handler')
    contacts_keyboard = [[Constants.contact_address_button,
                          Constants.contact_reach_button,
                          Constants.contact_back_button]]
    bot.send_message(update.message.chat_id, text=contacts_how_reach,
                     reply_markup=ReplyKeyboardMarkup(contacts_keyboard, resize_keyboard=True),
                     parse_mode='Markdown')


def main():
    updater = Updater(Constants.token)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                      RegexHandler('Вопрос-ответ', faq_handler),
                      CallbackQueryHandler(callback_faq),
                      RegexHandler(Constants.error_button, error_code_handler),
                      RegexHandler(Constants.contacts_button, contacts_handler)],

        states={

            ERROR: [RegexHandler('Назад', start),
                    RegexHandler('Повторить', error_code_handler),
                    RegexHandler('.{0,10}', error_handler_cycle)],
            CONTACTS: [RegexHandler(Constants.contact_back_button, start),
                       RegexHandler(Constants.contact_address_button, contacts_handler),
                       RegexHandler(Constants.contact_reach_button, contacts_reach_handler)]
        },
        allow_reentry=True,

        fallbacks=RegexHandler('.{0,10}', start)
    )
    dp.add_handler(conv_handler)
    updater.start_polling()


if __name__ == '__main__':
    main()

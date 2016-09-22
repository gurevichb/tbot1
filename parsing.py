import urllib
from urllib import request, error
import logger
from bs4 import BeautifulSoup
from constants import Constants
import re
import testing


def parse_faq():
    html = urllib.request.urlopen(Constants.site_faq).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('section', class_='slider_for_content view_list')
    faq_question_answer = []
    for row in table.find_all('dl'):
        faq_question_answer.append([row.find('span').text, row.find('p').text])
    return faq_question_answer


def parse_contact():
    html = urllib.request.urlopen(Constants.site_contacts).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_='contacts_info')
    address = ''
    for dl_block in table.find_all('dl'):
        address += '*' + dl_block.find('dt').text + '*' + '\n'
        tel_number = re.match('.*\d{3}-\d{2}-\d{2}.*', dl_block.find('dd').text)
        if tel_number is not None:
            address += tel_number.group() + '\n'
        for p_block in dl_block.find_all('p'):
            address += '\t' + p_block.text + '\n'
    return address


def parse_how_to_reach():
    html = urllib.request.urlopen(Constants.site_contacts).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_='contacts_path')
    reach_text = ''
    for li_block in table.find_all('li'):
        reach_text += '*' + li_block.find('h3').text.strip() + '*'
        reach_text += '\n'
        for p_block in li_block.find_all('p'):
            reach_text += p_block.text + '\n\n'
    return reach_text


def parse_knowledge_links():
    """Функция извлекает ссылки на статьи( напр. CP1001) с сайта developer.rutoken.ru/display/KB/.
    Должна обновляться с некоторой переодичностью.
    Обновляет список ссылок Constants.knowledge_pages.
    """
    Constants.knowledge_error_pages = []
    html = request.urlopen(Constants.site_knowledge_base).read()
    soup = BeautifulSoup(html, 'html.parser')
    for href in soup.find_all('span', class_='child-display'):
        Constants.knowledge_pages.append(Constants.site_knowledge_base + href.text.strip()[10:])
    logger.info(str(len(Constants.knowledge_pages)) + ' links to knowledge articles are updated')


def parse_error_links():
    """Функция выделяет те страницы, среди которых содержатся коды ошибок.
        Должна обновляться с некоторой переодичностью
        Обновляет список ссылок Constants.knowledge_error_pages
        """
    Constants.knowledge_error_pages = []
    for page in Constants.knowledge_pages:
        try:
            html = urllib.request.urlopen(page).read()
        except error.URLError:
            logger.warning('page isn\'t access: ' + page)
        if html is None:
            return
        html_page = BeautifulSoup(html, 'html.parser')
        if re.search('Код ошибки', html_page.text):
            Constants.knowledge_error_pages.append(page)
    logger.info(str(len(Constants.knowledge_error_pages)) +
                ' links on articles with an error code are added')


def search_in_page(error_code):
    """
    Из Constants.knowledge_error_pages по коду ошибки (или часть кода ошибки)
    выделяется код ошибки и ссылка на статью. Формируется список из списков [код ошибки, ссылка]
    """
    names_and_links = []
    list_of_names_and_links = []
    logger.info('Input regexp expr: ' + str(error_code))
    for link_with_error_page in testing.debug_error_links:
        try:
            html = urllib.request.urlopen(link_with_error_page).read()
        except error.URLError:
            logger.warning('page isn\'t access: ' + link_with_error_page)
            continue
        html_page = BeautifulSoup(html, 'html.parser')
        error_code_name = re.search('Код ошибки:?.{0,15}?' + error_code + '\d*?[\s:]', html_page.text)
        if error_code_name is not None:
            names_and_links.append(error_code_name.group(0)[0:-1])
            names_and_links.append(link_with_error_page)
            list_of_names_and_links.append(names_and_links)
        names_and_links = []
    return list_of_names_and_links

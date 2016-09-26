import urllib
from urllib import request, error
from bs4 import BeautifulSoup
from constants import Constants
import re
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

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
    knowledge_links = []
    html = request.urlopen(Constants.site_knowledge_base).read()
    soup = BeautifulSoup(html, 'html.parser')
    for href in soup.find_all('span', class_='child-display'):
        knowledge_links.append(Constants.site_knowledge_base + href.text.strip()[10:])
    logger.info(str(len(knowledge_links)) + ' links to knowledge articles are updated')
    return knowledge_links


def parse_error_links(knowledge_pages):
    """Функция выделяет те страницы, среди которых содержатся коды ошибок.
        Должна обновляться с некоторой переодичностью
        Обновляет список ссылок Constants.knowledge_error_pages
        """
    error_code_links = []
    for page in knowledge_pages:
        try:
            html = urllib.request.urlopen(page).read()
        except error.URLError:
            logger.info('page isn\'t access: ' + page)
        if html is None:
            return
        html_page = BeautifulSoup(html, 'html.parser')
        if re.search('Код ошибки', html_page.text):
            error_code_links.append(page)
    logger.info(str(len(error_code_links)) +
                ' links on articles with an error code are added')
    return error_code_links


def search_in_page(error_code, error_links):
    """
    Из Constants.knowledge_error_pages по коду ошибки (или часть кода ошибки)
    выделяется код ошибки и ссылка на статью. Формируется список из списков [код ошибки, ссылка]

    """
    names_and_links = []
    list_of_names_and_links = []
    logger.info('Input regexp expr: ' + str(error_code))
    for link_with_error_page in error_links:
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
    for list in list_of_names_and_links: logger.info(str(list))
    logger.info('Search is finished')
    return list_of_names_and_links


def search_tags(knowledge_pages):
    list_of_link_with_tags = []
    for url in knowledge_pages:
        link_with_tags = []
        try:
            html = urllib.request.urlopen(url).read()
        except error.HTTPError:
            logger.info('HTTP Error 404 in: ' + url)
            continue
        soup = BeautifulSoup(html, 'html.parser')
        link_with_tags.append(url)

        for tag in soup.find_all('a', class_='aui-label-split-main'):
            link_with_tags.append(tag.text)
        list_of_link_with_tags.append(link_with_tags)
    for link in list_of_link_with_tags:
        logger.info('add tags: \n' + str(link))
    return list_of_link_with_tags


priority1 = [] # Полное совпадение введенных тегов и тегов со страниц сайтов. Список таких сайтов
priority2 = [] # Частичное совпадение
def sort_tags(list_of_input_tags, link_with_tags):
    '''
    Принимает входящие теги и теги со страницы формирует списки priopity1, priority2
    '''
    list_of_fit_tag = [] # совпадающие теги
    for input_tag in list_of_input_tags:
        for out_tag in link_with_tags[1:]:
            if out_tag == input_tag:
                list_of_fit_tag.append(input_tag)
    if len(list_of_fit_tag) == 0:
        return
    if len(list_of_fit_tag) == len(link_with_tags[1:]):
        if len(list_of_fit_tag) == len(list_of_input_tags):
            priority1.append(link_with_tags[0]) # добавили ссылку полное совпадение тегов
        else:
            link_and_fit_tags = [link_with_tags[0]]
            link_and_fit_tags.extend(list_of_fit_tag)
            priority2.append(link_and_fit_tags)




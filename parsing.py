import urllib.request
from bs4 import BeautifulSoup
from constants import constants
import re


def parse_faq():
    html = urllib.request.urlopen(constants.site_faq).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('section', class_='slider_for_content view_list')
    faq_question_answer = []
    for row in table.find_all('dl'):
        faq_question_answer.append([row.find('span').text, row.find('p').text])
    return faq_question_answer


def parse_contact():
    html = urllib.request.urlopen(constants.site_contacts).read()
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
    html = urllib.request.urlopen(constants.site_contacts).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_='contacts_path')
    reach_text = ''
    for li_block in table.find_all('li'):
        reach_text += '*' + li_block.find('h3').text.strip() + '*'
        reach_text += '\n'
        for p_block in li_block.find_all('p'):
            reach_text += p_block.text + '\n\n'
    return reach_text

import urllib.request
from bs4 import BeautifulSoup
from constants import constants


def parse_faq():
    #TODO to check site
    html = urllib.request.urlopen(constants.site_faq).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('section', class_='slider_for_content view_list')
    faq_question_answer = []
    for row in table.find_all('dl'):
        faq_question_answer.append([row.find('span').text, row.find('p').text])
    return faq_question_answer

def parse_contacts():
    html = urllib.request.urlopen(constants.site_contacts).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_='contacts_info')
    address = []

    for dl_block_number, text_block in enumerate(table.find_all('dl')):
        content_address = []
        if(dl_block_number == 0):
            content_address.append(text_block.find('dt').text)
            if (text_block.find('p')):
                for sub2 in text_block.find_all('p'):
                    content_address.append(sub2.text)
            address.append(content_address)

        if (dl_block_number == 1):
            content_address.append(text_block.find('dt').text)
            if (text_block.find('dd')):
                for sub2 in text_block.find_all('dd'):
                    content_address.append(sub2.text)
            address.append(content_address)

        if (dl_block_number == 2):
            content_address.append(text_block.find('dt').text)
            if (text_block.find('p')):
                for sub2 in text_block.find_all('p'):
                    content_address.append(sub2.text)
            address.append(content_address)

        if (dl_block_number == 3):
            content_address.append(text_block.find('dt').text)
            if (text_block.find('p')):
                for sub2 in text_block.find_all('p'):
                    content_address.append(sub2.text)
            address.append(content_address)
    return address

def parse_how_to_reach():
    html = urllib.request.urlopen(constants.site_contacts).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_='contacts_path')
    s = ''
    s = s + table.find('h3').text + '\n'
    for p in table.find_all('p'):
        s = s + p.text + '\n'
    return s

#parse_how_to_reach()
#parse_contacts()

import urllib.request
from bs4 import BeautifulSoup
from constants import constants

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parseFAQ():
    #TODO to check site
    html = urllib.request.urlopen(constants.site).read()
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('section', class_='slider_for_content view_list')
    faq_question_answer = []
    for row in table.find_all('dl'):
        faq_question_answer.append([row.find('span').text, row.find('p').text])
    return faq_question_answer

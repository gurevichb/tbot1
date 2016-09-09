import urllib.request
from bs4 import BeautifulSoup
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parseFAQ():
    html = get_html('http://www.rutoken.ru/support/feedback/')
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('section', class_='slider_for_content view_list')
    FAQtext1 = []
    for row in table.find_all('dl'):
        FAQtext1.append([row.find('span').text, row.find('p').text])
    return FAQtext1

def main():
    test()
    print('test')

def test():
    '''
    print(parseFAQ())
    for i in parseFAQ():
        s = i.keys().__str__()
        print(s)
        print(i.values())

    #print(parseFAQ())
    for i in parseFAQ():
        print(i)
        print(i.index())
        print(i[0])
        print(i[1])
'''
    i = 0
    FAQlist = parseFAQ()
    while i < len(FAQlist):
            print(i)
            print(FAQlist[i][0])
            i = i + 1

if __name__ == '__main__':
    main()
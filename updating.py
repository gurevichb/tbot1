import threading
import time
import parsing
import testing

class UpdateData:
    __faq_list = []
    __contacts_text = []
    __contacts_how_reach = ''
    __knowledge_links = []
    __knowledge_error_links = []

    def __init__(self):

        self.update()

    def update(self):
        self.__faq_list = parsing.parse_faq()
        self.__contacts_text = parsing.parse_contact()
        self.__contacts_how_reach = parsing.parse_how_to_reach()
        self.__knowledge_links = parsing.parse_knowledge_links()
        # 20 seconds
        self.__knowledge_error_links = parsing.parse_error_links(self.__knowledge_links)
        #
        # self.__knowledge_error_links = testing.debug_error_links

    def get_faq_list(self):
        return self.__faq_list

    def get_contacts_text(self):
        return self.__contacts_text

    def get_contacts_how_reach(self):
        return self.__contacts_how_reach

    def get_knowledge_links(self):
        return self.__contacts_how_reach

    def get_knowledge_error_links(self):
        return self.__knowledge_error_links

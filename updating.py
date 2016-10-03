import time
import parsing
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class UpdateData:
    __faq_list = []
    __contacts_text = []
    __contacts_how_reach = ''
    __knowledge_links = []
    __knowledge_error_links = []
    __links_with_tags = []

    def update(self, update_time):
        while True:
            logger.info('updating has begun')
            self.__faq_list = parsing.parse_faq()
            self.__contacts_text = parsing.parse_contact()
            self.__contacts_how_reach = parsing.parse_how_to_reach()
            self.__knowledge_links = parsing.parse_knowledge_links()
            # 20 seconds
            self.__knowledge_error_links = parsing.parse_error_links(self.__knowledge_links)
            #
            self.__links_with_tags = parsing.search_tags(self.__knowledge_links)
            logger.info('updating has ended')
            time.sleep(update_time)

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

    def get_links_with_tags(self):
        return self.__links_with_tags
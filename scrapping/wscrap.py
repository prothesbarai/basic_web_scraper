from urllib.request import urlopen
from bs4 import BeautifulSoup

# Global variable declaration
pro_url = "https://prothesbarai.github.io/"  # Collect Data From Url
filepath = "output/pro.html"  # save collected url data location


class WebScraper:
    __url = ''
    __data = ''
    __wlog = None
    __soup = None

    def __init__(self, url, wlog):
        self.__url = url
        self.__wlog = wlog

    # Webpage read write method
    def retrieve_webpage(self):
        try:
            html = urlopen(self.__url)
        except Exception as e:
            self.__wlog.report(e)
        else:
            self.__data = html.read()
            if len(self.__data) > 0:
                print("Retrieved Successfully")

    def write_webpage_as_html(self, filepath=filepath, data=''):
        try:
            with open(filepath, 'wb') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self.__data)

        except Exception as e:
            self.__wlog.report(str(e))

    def read_webpage_as_html(self, filepath=filepath):
        try:
            with open(filepath) as fobj:
                self.__data = fobj.read()
        except Exception as e:
            self.__wlog.report(str(e))

    def change_url(self, url):
        self.__url = url

    def convert_data_to_bs4(self):
        self.__soup = BeautifulSoup(self.__data, 'html.parser')

    def parse_soup_to_simple_html(self):
        news_list = self.__soup.find_all('a')

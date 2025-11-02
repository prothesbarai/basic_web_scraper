from scrapping import wlog
from scrapping import wscrap

wlog.set_custom_log_info('error_log/error.log')
news_scrap = wscrap.WebScraper(wscrap.pro_url, wlog)
news_scrap.retrieve_webpage()
news_scrap.write_webpage_as_html()
news_scrap.read_webpage_as_html()
news_scrap.convert_data_to_bs4()
news_scrap.parse_soup_to_simple_html()

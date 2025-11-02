from scrapping.wscrap import WebScraper, pro_url

# Dummy Logger Class তৈরি করা
class DummyLogger:
    def report(self, msg):
        print("⚠️ Log:", msg)

# এখন WebScraper ক্লাস রান করো
if __name__ == "__main__":
    logger = DummyLogger()
    scraper = WebScraper(pro_url, logger)
    scraper.retrieve_webpage()
    scraper.write_webpage_as_html()

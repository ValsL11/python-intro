import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # Iteracja po cytatach
        for quote in response.css('div.quote'):
            # Pobranie tekstu cytatu i autora
            text = quote.css('span.text::text').get()
            author = quote.css('span small::text').get()

            # Wyświetlanie ładnie sformatowanych wyników
            print(f"-------------------------------")
            print(f"Cytat: {text}")
            print(f"Autor: {author}")
            print(f"-------------------------------")
import scrapy


class UnsplashSpider(scrapy.Spider):
    name = 'unsplash'
    start_urls = ['https://unsplash.com/categories']

    def parse(self, response):
        categories = response.css('a[title^="View all"]');
        for category in categories:
            category_url = response.urljoin(category.attrib['href'])
            yield scrapy.Request(category_url, callback=self.parse_category_page)

    def parse_category_page(self, response):
        images = response.css('a[aria-label="Download photo"]')
    for image in images:
        item = UnsplashImageItem()
        item['image_url'] = response.urljoin(image.attrib['href'])
        item['image_title'] = image.attrib['download']
        item['image_category'] = response.css('h1::text').get()
        yield item
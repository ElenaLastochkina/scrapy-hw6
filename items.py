import scrapy


class UnsplashImageItem(scrapy.Item):
    image_url = scrapy.Field()
    image_title = scrapy.Field()
    image_category = scrapy.Field()
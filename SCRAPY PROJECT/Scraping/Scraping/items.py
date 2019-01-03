import scrapy


class MemberItem(scrapy.Item):
    job_title = scrapy.Field()
    exp_req = scrapy.Field()
    loc = scrapy.Field()
    com_name = scrapy.Field()
    link = scrapy.Field()
    keyskills = scrapy.Field()
    jd = scrapy.Field()
    salary = scrapy.Field()

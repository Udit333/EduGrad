import scrapy
from Scraping.items import MemberItem
from scrapy.loader import ItemLoader


class MemberDetails(scrapy.Spider):
    name = 'GetDetails'

    start_urls = ['https://www.naukri.com/data-analytics-jobs-in-delhi/index.html',
                  'https://www.naukri.com/data-analytics-jobs-in-delhi-1',
                  'https://www.naukri.com/data-analytics-jobs-in-delhi-2',
                  'https://www.naukri.com/data-analytics-jobs-in-delhi-3'
                  'https://www.naukri.com/data-analytics-jobs-in-delhi-4',
                  'https://www.naukri.com/data-analytics-jobs-in-delhi-5',
                  'https://www.naukri.com/data-analytics-jobs-in-delhi-6']

    def parse(self, response):

        m = response.css('div.row')

        for mem in m:
            m_loader = ItemLoader(MemberItem(), selector=mem)
            m_loader.add_css('job_title', 'span.content > ul > li.desig::text')
            m_loader.add_css('exp_req', 'span.exp::text')
            m_loader.add_css('loc', 'span.loc > span::text')
            m_loader.add_css('com_name', 'span.orgRating > span.org::text')
            m_loader.add_css('link', 'a::attr(href)')
            m_loader.add_css('jd', 'span.desc::text')
            m_loader.add_css('keyskills', 'div.more > div.desc > span.skill::text')
            m_loader.add_css('salary', 'div.other_details > span.salary::text')

            yield m_loader.load_item()

import scrapy
from scrapy import Spider
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

link = "https://www.webmd.com/"

'''
This porject uses scrapy is made to parse reviews from the webMD database
It reads a drugList.txt and goes through the txt file prepending the link
    https://www.webmd.com/drugs/2/search?type=drugs&query=
    
The crawler then checks for more than one page and will parse accordingly, moving onto the next page if needed

*** Possible Improvments: For some reason the two for loops in the function parseReviews cannot
    be shortened to just 1 and have a if statement outside, more research is needed
    
    If a webMD query doesn't exist, it will not parse it and as of now
     there isn't a way of sending which queries failed

To run this code please refer to the file instructionsForScrapy.txt
This cannot be easily run with a main.py file

'''

class webMDSpider(Spider):
    name = "webMD_Reviews"
    drugNames = []

    # URLS to be parsed
    start_urls = []

    # Link to be appended to the begging of the name
    startingLink = 'https://www.webmd.com/drugs/2/search?type=drugs&query='

    with open('/Users/alexchen/Desktop/Coding/Python/personalCrawling/webmdScraper_personal/webmdScraperMain/drugNames.txt') as f:
        drugNames = f.readlines()


    for i in drugNames:
        # Fill url list with the above starting link and name of drugs from the txt
        start_urls.append(startingLink + i.replace("\n", ''))

    #create a hashset so any duplicates will not be parsed
    pyHashSet = set()
    pages = 0

    # Go to each link
    def parse(self, response):
        for link in response.css('div.drugs-exact-search-list a::attr(href)').getall():
            yield response.follow(link, callback = self.parse_tab)

    # Go to Review tabs
    def parse_tab(self, response):
        tabList = response.css('ul.auto-tabs a::attr(href)').getall()
        yield response.follow(tabList[6], callback= self.parseReviews)

    # Parse reviews, also check if the review pages has more than 1 page
    def parseReviews(self, response):

        pages = int(response.css('li.page-item ::text').getall()[-1])

        reviews = response.css('p.description-text::text').getall()
        longReviews = response.css('p.description-text').css('span.showSec::text').getall()
        remainReviews = response.css('p.description-text').css('span.hiddenSec::text').getall()

        drugName = response.css('h1.drug-name').css('a::text').get().rstrip().lstrip()
        if drugName in self.pyHashSet:
            yield
        else:
            self.pyHashSet.add(drugName)

            for r in reviews:
                yield {
                    'Drug name': drugName,
                    'description': r,
                }
            counter = 0
            for i in longReviews:
                yield {
                    'Drug name': drugName,
                    'description': i + remainReviews[counter]

                }
                counter += 1
        if pages > 1:
            nextPage = response.css('li.page-item a::attr(href)').getall()[1]
            current =2
            while current <= pages:
                split = '&next_page'
                res = nextPage.partition(split)[0]

                nextLink = response.request.url + res
                nextLink = nextLink[:-1] + str(current)
                print("Link: "+ nextLink)

                yield response.follow(nextLink, callback=self.parseMultiplePages)
                current += 1




    # If it has multiple pages, response will be parse here
    def parseMultiplePages(self, response):

        reviews = response.css('p.description-text::text').getall()
        longReviews = response.css('p.description-text').css('span.showSec::text').getall()
        remainReviews = response.css('p.description-text').css('span.hiddenSec::text').getall()

        for r in reviews:
            yield {
                'Drug name': response.css('h1.drug-name').css('a::text').get().rstrip().lstrip(),
                'description': r,
            }
        counter = 0
        for i in longReviews:
            yield {
                'Drug name': response.css('h1.drug-name').css('a::text').get().rstrip().lstrip(),
                'description': i + remainReviews[counter]

            }
            counter += 1

# def main():
#     settings = get_project_settings()
#     process = CrawlerProcess(settings)
#     process.crawl(webMDSpider)
#     process.start()
#
# main()


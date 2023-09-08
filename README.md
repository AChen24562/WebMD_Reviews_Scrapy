# WebMD_Reviews_Scrapy

Built in Collaboration with ssr01357 (Yeawon Lee for her master's thesis) 
The purpose of this code was to scrape WebMD for a specific set of drugs and their side affects


Tested on python version 3.9
1) Create Environment on version python version 3.9
2) pip install or conda install Scrapy
    https://docs.scrapy.org/en/latest/intro/install.html
3) Open Terminal
    cd into the directory prior to main, where this txt file is, and more importantly where the
    .cfg file is
    Ex: For me the directory is: C:\Users\alex\Desktop\Coding\pythonProject\personalCrawling\webmdScraper
4) Run: scrapy crawl webmd_Test -O webmd.csv
        webmd_Test is name of the spider in the spiders folder, spiders are used to crawl
        -O signifies what type of file to export the crawled data, from what I see supports
        .csv .json .txt .xls

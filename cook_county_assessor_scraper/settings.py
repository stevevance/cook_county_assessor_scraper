# -*- coding: utf-8 -*-

# Scrapy settings for cook_county_pin_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cook_county_assessor'

SPIDER_MODULES = ['cook_county_assessor_scraper.spiders']
NEWSPIDER_MODULE = 'v.spiders'
DOWNLOAD_DELAY = 0.006
CONCURRENT_REQUESTS = 36
MEMDEBUG_ENABLED = True
DEFAULT_REQUEST_HEADERS = {
    'Referer': 'http://www.cookcountyassessor.com/'
}
DOWNLOAD_HANDLERS = {'s3': None}
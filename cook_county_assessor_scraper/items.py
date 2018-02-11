# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Property(scrapy.Item):
    pin = scrapy.Field()
    
    property_tax_year = scrapy.Field()
    taxcode = scrapy.Field()
    neighborhood = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    township = scrapy.Field()

    lot_size = scrapy.Field()
    building_size = scrapy.Field()
    property_class = scrapy.Field()
    age = scrapy.Field()
    
    land_value = scrapy.Field()
    building_value = scrapy.Field()
    total_value = scrapy.Field()
    
    est_market_value_current = scrapy.Field()
    est_market_value_previous = scrapy.Field()
    
    residential_type = scrapy.Field()
    property_use = scrapy.Field()
    apartments = scrapy.Field()
    exterior_const = scrapy.Field()
    baths_full = scrapy.Field()
    baths_half = scrapy.Field()
    basement = scrapy.Field()
    attic = scrapy.Field()
    central_air = scrapy.Field()
    fireplaces = scrapy.Field()
    garage = scrapy.Field()
    
    land_value_firstpass = scrapy.Field()
    building_value_firstpass = scrapy.Field()
    total_value_firstpass = scrapy.Field()
    
    land_value_certified = scrapy.Field()
    building_value_certified = scrapy.Field()
    total_value_certified = scrapy.Field()
    
    values = scrapy.Field()
    
    assessment_pass = scrapy.Field()
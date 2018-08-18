# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CSVFeedSpider
from collections import OrderedDict
from cook_county_assessor_scraper.items import Property

class PropertyinfoSpider(CSVFeedSpider):
    headers = ['pin']
    name = "assessor"
    allowed_domains = ["cookcountyassessor.com"]
    start_urls = [
	    "http://chicagocityscape.com/scrapy/batch1.csv"
	    "http://chicagocityscape.com/scrapy/batch2.csv"
    ]
    
    state = OrderedDict()

    def parse_row(self, response, row):
        pin = row['pin']
        return scrapy.Request('http://www.cookcountyassessor.com/Property.aspx?mode=details&pin='+pin, callback=self.parse_pin)

    def extract_with_prefix(self, response, suffix, inner_part=''):
        ext = response.xpath('//span[@id="ctl00_phArticle_ctlPropertyDetails_{}"]{}/text()'.format(suffix, inner_part))
        if len(ext) == 1:
            return ext[0].extract()
        else:
            return None

    def parse_pin(self, response):
        if self.extract_with_prefix(response, 'resultsNotFoundPanel'):
            yield None

        item = Property()

        item['property_tax_year'] = self.extract_with_prefix(response, 'lblPropInfoCurYear')
        if item['property_tax_year']:
            item['property_tax_year'] = int(item['property_tax_year'][-4:])
            
        item['taxcode'] = self.extract_with_prefix(response, 'lblPropInfoTaxcode')
        item['neighborhood'] = self.extract_with_prefix(response, 'lblPropInfoNBHD')

        item['pin'] = self.extract_with_prefix(response, 'lblPropInfoPIN')
        item['address'] = self.extract_with_prefix(response, 'lblPropInfoAddress')
        item['city'] = self.extract_with_prefix(response, 'lblPropInfoCity')
#         item['zip_code'] = self.extract_with_prefix(response, 'propertyZip')
        item['township'] = self.extract_with_prefix(response, 'lblPropInfoTownship')

        item['lot_size'] = self.extract_with_prefix(response, 'lblPropInfoSqFt')
        if item['lot_size']:
            item['lot_size'] = int(item['lot_size'].replace(',', ''))

        item['building_size'] = self.extract_with_prefix(response, 'lblPropCharBldgSqFt')
        if item['building_size'] and item['building_size'].find(",") >= 0:
            item['building_size'] = int(item['building_size'].replace(',', ''))
        else:
            item['building_size'] = None

        property_class_description = self.extract_with_prefix(response, 'lblPropCharDesc')
        if property_class_description:
            property_class_description = self.extract_with_prefix(response, 'lblPropCharDesc')
        else:
            property_class_description = None

        item['property_class'] = {
            'class': self.extract_with_prefix(response, 'lblPropInfoClassification'),
            'description': property_class_description
        }
        age = self.extract_with_prefix(response, 'lblPropCharAge')
        if(age and age.isdigit()):
            item['age'] = int(age)
        else:
            item['age'] = None
        
        
        item['residential_type'] = self.extract_with_prefix(response, 'lblPropCharResType')
        item['property_use'] = self.extract_with_prefix(response, 'lblPropCharUse')
        item['apartments'] = self.extract_with_prefix(response, 'lblPropCharApts')
        
        item['exterior_const'] = self.extract_with_prefix(response, 'lblPropCharExtConst')
        item['baths_full'] = self.extract_with_prefix(response, 'lblPropCharFullBaths')
        item['baths_half'] = self.extract_with_prefix(response, 'lblPropCharHalfBaths')
        item['basement'] = self.extract_with_prefix(response, 'lblPropCharBasement')
        item['attic'] = self.extract_with_prefix(response, 'lblPropCharAttic')
        item['central_air'] = self.extract_with_prefix(response, 'lblPropCharCentAir')
        item['fireplaces'] = self.extract_with_prefix(response, 'lblPropCharFrpl')
        item['garage'] = self.extract_with_prefix(response, 'lblPropCharGarage')
        
#         item['land_value_firstpass'] = self.extract_with_prefix(response, 'lblAsdValLandFirstPass')
#         item['building_value_firstpass'] = self.extract_with_prefix(response, 'lblAsdValBldgFirstPass')
#         item['total_value_firstpass'] = self.extract_with_prefix(response, 'lblAsdValTotalFirstPass')
#         
#         item['land_value_certified'] = self.extract_with_prefix(response, 'lblAsdValLandCertified')
#         item['building_value_certified'] = self.extract_with_prefix(response, 'lblAsdValBldgCertified')
#         item['total_value_certified'] = self.extract_with_prefix(response, 'lblAsdValTotalCertified')
        
        
        # market values
        est_market_value_current = self.extract_with_prefix(response, 'lblPropCharMktValCurrYear')
        if est_market_value_current and est_market_value_current.replace(',', '').replace('$', '').isdigit():
            est_market_value_current = int(self.extract_with_prefix(response, 'lblPropCharMktValCurrYear').replace(',', '').replace('$', ''))
        else:
            est_market_value_current = None
            
        est_market_value_previous = self.extract_with_prefix(response, 'lblPropCharMktValCurrYear')
        if est_market_value_previous and est_market_value_previous.replace(',', '').replace('$', '').isdigit():
            est_market_value_previous = int(self.extract_with_prefix(response, 'lblPropCharMktValPrevYear').replace(',', '').replace('$', ''))
        else:
            est_market_value_previous = None
            
        # land and building values
        land_value_firstpass = self.extract_with_prefix(response, 'lblAsdValLandFirstPass')
        if land_value_firstpass:
            land_value_firstpass = int(self.extract_with_prefix(response, 'lblAsdValLandFirstPass').replace(',', ''))
        else:
            land_value_firstpass = None
        
        building_value_firstpass = self.extract_with_prefix(response, 'lblAsdValBldgFirstPass')
        if building_value_firstpass:
            building_value_firstpass = int(self.extract_with_prefix(response, 'lblAsdValBldgFirstPass').replace(',', ''))
        else:
            building_value_firstpass = None
        
        total_value_firstpass = self.extract_with_prefix(response, 'lblAsdValTotalFirstPass')
        if total_value_firstpass:
            total_value_firstpass = int(self.extract_with_prefix(response, 'lblAsdValTotalFirstPass').replace(',', ''))
        else:
            total_value_firstpass = None
            
        land_value_certified = self.extract_with_prefix(response, 'lblAsdValLandCertified')
        if land_value_certified:
            land_value_certified =  int(self.extract_with_prefix(response, 'lblAsdValLandCertified').replace(',', ''))
        else:
            land_value_certified = None
            
        building_value_certified = self.extract_with_prefix(response, 'lblAsdValBldgCertified')
        if building_value_certified:
            building_value_certified = int(self.extract_with_prefix(response, 'lblAsdValBldgCertified').replace(',', ''))
        else:
            building_value_certified = None
            
        total_value_certified = self.extract_with_prefix(response, 'lblAsdValTotalCertified')
        if total_value_certified:
            total_value_certified = int(self.extract_with_prefix(response, 'lblAsdValTotalCertified').replace(',', ''))
        else:
            total_value_certified = None
        
        item['values'] = {
	        'land_value_firstpass': land_value_firstpass,
	        'building_value_firstpass': building_value_firstpass,
	        'total_value_firstpass': total_value_firstpass,
	        'land_value_certified': land_value_certified,
	        'building_value_certified': building_value_certified,
	        'total_value_certified': total_value_certified,
	        'est_market_value_current': est_market_value_current,
	        'est_market_value_previous': est_market_value_previous
        }
        
#         'est_market_value_current': int(self.extract_with_prefix(response, 'lblPropCharMktValCurrYear').replace(',', '').replace('$', '')),
# 	    'est_market_value_previous': int(self.extract_with_prefix(response, 'lblPropCharMktValPrevYear').replace(',', '').replace('$', ''))
        
#         item['est_market_value_current'] = self.extract_with_prefix(response, 'lblPropCharMktValCurrYear')
#         item['est_market_value_previous'] = self.extract_with_prefix(response, 'lblPropCharMktValPrevYear')
        item['assessment_pass'] = self.extract_with_prefix(response, 'lblPropCharAsmtPass')

        yield item

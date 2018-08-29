cook_county_assessor_scraper
=======================

Scrapes the Cook County assessor's office PIN page and dumps data in a more useful format.

Setup and Running
-----------------

```python
# Install scrapy (preferably in a virtual environment)
mkvirtualenv --no-site-packages cook_county_assessor_scraper
pip install scrapy
# Clone the git repo
git clone git@github.com:stevevance/cook_county_assessor_scraper.git
# Update the list of PINs you want to scrape by changing the file on line 12 in cook_county_assessor_scraper/spiders/propertyinfo.py
# Run the scraper
cd cook_county_assessor_scraper
scrapy crawl propertyinfo -o properties.json -t jsonlines -L INFO
# The output will be in properties.json
```

Check in on the status with `telnet localhost 6023` and then `est()`. Use `exit()` to exit [Scrapy's Telnet console](https://doc.scrapy.org/en/latest/topics/telnetconsole.html).
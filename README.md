# Scrapy Tag Crawler

A web crawler using Scrapy Framework(Python)

## Getting Started

### Scrapy
https://docs.scrapy.org/en/latest/intro/install.html

For uploading files to amazon s3, we need to install some packages that didn't come by default with Scrapy
```
pip install pillow
pip intall boto
```

### sqlalchemy
http://docs.sqlalchemy.org/en/latest/intro.html#installation-guide

Don't forget to update database info in models/base.py

## Run
cd to top directory
```
scrapy crawl tags
```

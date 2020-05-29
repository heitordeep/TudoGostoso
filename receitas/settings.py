# -*- coding: utf-8 -*-

# Scrapy settings for receitas project
from decouple import config

BOT_NAME = 'receitas'

SPIDER_MODULES = ['receitas.spiders']
NEWSPIDER_MODULE = 'receitas.spiders'
FEED_EXPORT_ENCODING = 'utf-8'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'receitas'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 0.25

# Configure item pipelines
ITEM_PIPELINES = {
    'receitas.pipelines.ReceitasPipeline': 0,
}

# MongoDB

MONGO_URL = config('URL')
MONGO_DB = config('DATABASE')

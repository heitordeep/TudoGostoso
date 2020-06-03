# Scrapy settings for receitas project

from decouple import config

BOT_NAME = 'recipes'

SPIDER_MODULES = ['recipes.spiders']
NEWSPIDER_MODULE = 'recipes.spiders'
FEED_EXPORT_ENCODING = 'utf-8'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'recipes'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 0.35

# Configure item pipelines
ITEM_PIPELINES = {
    'recipes.pipelines.MongodbPipeline': 0,
}

# MongoDB

MONGO_URL = config('URL')
MONGO_DB = config('DATABASE')

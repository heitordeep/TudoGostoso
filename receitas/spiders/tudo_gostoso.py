# -*- coding: utf-8 -*-
from scrapy import Request, Spider


class TudoGostosoSpider(Spider):
    name = 'tudo_gostoso'
    default_domain = 'https://www.tudogostoso.com.br'
    start_urls = [
        'https://www.tudogostoso.com.br/busca?q=vegano',
        'https://www.tudogostoso.com.br/receitas-vegetarianas',
    ]

    def parse(self, response):
        link_recipe = response.css(
            'div.recipe-card-with-hover a::attr(href)'
        ).getall()

        yield from response.follow_all(
            link_recipe, self.parse_vegan_and_veggie
        )

        pagination = response.css('.next::attr(href)').get()
        yield response.follow(f'{self.default_domain}{pagination}', self.parse)

    def parse_vegan_and_veggie(self, response):
        title = response.css('.recipe-title h1::text').get().strip()
        image = response.css('.pic::attr(src)').getall()
        preparation = (
            response.css('.dt-duration::text').get().strip().replace('\n', ' ')
        )
        favorite = response.css('.like .num::text').get().strip()
        author = response.css('.author-name span::text').get().strip()
        ingredients = response.css('.p-ingredient::text').getall()
        method_of_preparation = response.css(
            '.e-instructions span::text'
        ).getall()

        if len(method_of_preparation) == 0 or len(ingredients) == 0:
            ingredients = response.css('.p-ingredient p::text').getall()
            method_of_preparation = response.css(
                '.e-instructions p::text'
            ).getall()

        yield {
            'title': title,
            'image': image,
            'preparation': preparation,
            'ingredients': ingredients,
            'method_of_preparation': method_of_preparation,
            'author': author,
            'favorite': favorite,
            'url': response.url,
        }

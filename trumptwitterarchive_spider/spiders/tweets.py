# -*- coding: utf-8 -*-
import json
import scrapy


class TweetsSpider(scrapy.Spider):
    name = 'tweets'
    allowed_domains = ['trumptwitterarchive.com']
    start_urls = ['http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2017.json']

    def parse(self, response):
        jsonresponse = json.loads(response.body)

        for tweet in jsonresponse:
            yield {'created_at': tweet['created_at'],
                   'favorite_count': tweet['favorite_count'],
                   'id_str': tweet['id_str'],
                   'in_reply_to_user_id_str': tweet['in_reply_to_user_id_str'],
                   'is_retweet': tweet['is_retweet'],
                   'retweet_count': tweet['retweet_count'],
                   'source': tweet['source'],
                   'text': tweet['text']}

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os

import boto3
# from feedgen.feed import FeedGenerator
import tweepy

auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])


def run_local():
    fetch_tweets()


def fetch_tweets():
    api = tweepy.API(auth)
    # s3 = boto3.resource('s3')
    # bucket = s3.Bucket('w2s.ssr')
    items = []
    for tweet in api.user_timeline('jeremyphoward', count=50):
        print("{t.author.name}(@{t.author.screen_name})  {t.text}".format(t=tweet))


def add_feed_entry(fg, tweet):
    fe = fg.add_entry()
    fe.id(tweet['url'])
    fe

def generate_feed():
    fg = FeedGenerator()
    fg.id('http://lernfunk.de/media/654321')
    fg.title('My twitter timeline')
    fg.logo('https://abs.twimg.com/favicons/favicon.ico')





if __name__ == '__main__':
    if os.environ.get('SSR_LOCAL'):
        run_local()

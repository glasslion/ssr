# -*- coding: utf-8 -*-
import os

import boto3
import tweepy

auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])


def main():
    api = tweepy.API(auth)
    public_tweets = api.home_timeline()
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('w2s.ssr')
    for tweet in public_tweets:
        print tweet.text

if __name__ == '__main__':
    main()

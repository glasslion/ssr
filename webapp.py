# -*- coding: utf-8 -*-
from flask import Flask, request

from werkzeug.contrib.atom import AtomFeed


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!", 200

@app.route('/recent.atom')
def recent_feed():
    feed = AtomFeed('Recent Articles',
                    feed_url=request.url, url=request.url_root)
    articles = Article.query.order_by(Article.pub_date.desc()) \
                      .limit(15).all()
    for article in articles:
        feed.add(article.title, unicode(article.rendered_text),
                 content_type='html',
                 author=article.author.name,
                 url=make_external(article.url),
                 updated=article.last_update,
                 published=article.published)
    return feed.get_response()


# We only need this for local development.
if __name__ == '__main__':
    app.run()

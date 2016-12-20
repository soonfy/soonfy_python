#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'crawl douban movie list data.'

__author__ = 'soonfy'

from douban_spider import spider_nologin

class MovieSpider(object):
  """
  douban movie spider
  category: movie, book, music
  """
  def __init__(self, userid, category):
    self.userid = userid
    self.category = category

  def crawl_do(self):
    """
    正在看得
    """
    movie_do = 'https://%s.douban.com/people/%s/do' % (self.category, self.userid)
    print(movie_do)
    opener = spider_nologin()
    body = opener.open(movie_do).read()
    # print(body.decode('utf-8'))
    return body

  def crawl_wish(self):
    """
    希望看得
    """
    movie_wish = 'https://%s.douban.com/people/%s/wish' % (self.category, self.userid)
    print(movie_wish)
    opener = spider_nologin()
    body = opener.open(movie_wish).read()
    # print(body.decode('utf-8'))
    return body

  def crawl_collect(self):
    """
    看过得
    """
    movie_collect = 'https://%s.douban.com/people/%s/collect' % (self.category, self.userid)
    print(movie_collect)
    opener = spider_nologin()
    body = opener.open(movie_collect).read()
    # print(body.decode('utf-8'))
    return body

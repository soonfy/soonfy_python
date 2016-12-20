#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'movie spider class.'

__author__ = 'soonfy'

# modules
from bs4 import BeautifulSoup

class MovieSpider(object):
  """
  douban movie spider
  category: movie, book, music
  """
  def __init__(self, userid, opener, category = 'movie'):
    self.userid = userid
    self.opener = opener
    self.category = category
    self.category_do = 'https://%s.douban.com/people/%s/do' % (category, userid)
    self.category_wish = 'https://%s.douban.com/people/%s/wish' % (category, userid)
    self.category_collect = 'https://%s.douban.com/people/%s/collect' % (category, userid)

  def crawl_do(self):
    """
    正在看得
    """
    opener, category_do = self.opener, self.category_do
    print(category_do)
    body = opener.open(category_do).read()
    soup = BeautifulSoup(body, 'html.parser')
    return soup

  def crawl_wish(self):
    """
    希望看得
    """
    opener, category_wish = self.opener, self.category_wish
    print(category_wish)
    body = opener.open(category_wish).read()
    soup = BeautifulSoup(body, 'html.parser')
    return soup

  def crawl_collect(self):
    """
    看过得
    """
    opener, category_collect = self.opener, self.category_collect
    print(category_collect)
    body = opener.open(category_collect).read()
    soup = BeautifulSoup(body, 'html.parser')
    return soup

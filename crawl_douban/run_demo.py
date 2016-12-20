#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider start run demo.'

__author__ = 'soonfy'

# modules
from bs4 import BeautifulSoup

from spider_middleware.douban_spider import spider_nologin
from douban_movie.parse_movie import get_summary, get_score

# demo parse_movie
body = spider_nologin().open('https://movie.douban.com/subject/25900819/?tag=%E7%83%AD%E9%97%A8&from=gaia')
soup = BeautifulSoup(body, 'html.parser')
summary = get_summary(soup)
print(summary)

score, people, stars = get_score(soup)
print(score)
print(people)
print(stars)

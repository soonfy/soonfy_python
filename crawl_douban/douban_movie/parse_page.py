#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'parse douban page data page.'

__author__ = 'soonfy'

from bs4 import BeautifulSoup
import re

def get_movie(soup):
  """
  get data from douban user-movie html  
  ex: https://movie.douban.com/people/67492098/wish  
  """
  tag_divs = soup.find_all('div', class_='item')
  movies = []
  movie_urls = []
  user_movie = soup.h1.string
  for tag in tag_divs:
    tag_a = tag.find('li', class_='title').find('a')
    movie_url = tag_a['href']
    movie_name = tag_a.find('em').string
    tag_span = tag.find('span', class_='date')
    movie_date = None
    movie_rate = None
    if tag_span:
      movie_date = tag_span.string
    tag_rate = tag.find('span', class_=re.compile('rating\d-t'))
    if tag_rate:
      movie_rate = tag_rate['class']
    movie = '%s\t%s\t%s\t%s\t%s' % (user_movie, movie_name, movie_url, movie_date, movie_rate)
    movies.append(movie)
    movie_urls.append(movie_url)
  print(movie_urls)
  return movies, movie_urls

def get_next(soup):
  """
  get next url from douban movie html
  ex: https://movie.douban.com/people/67492098/wish
  """
  tag_span = soup.find('span', class_='next')
  tag_a = None
  if tag_span:
    tag_a = tag_span.find('a')
  url = None
  if tag_a:
    url = tag_a['href']
  return url

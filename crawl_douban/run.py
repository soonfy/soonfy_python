#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider start run.'

__author__ = 'soonfy'

import os
import time
import random
from fs import file_ready

# crawl ua
# from middleware import update_ua, get_cookie, use_cookie
# 相对主程序执行路径
# ua_file = os.path.abspath(r'./spider_douban/ua.txt')

# print('running spider...')
# uas = update_ua()
# print('crawl ua over...')
# print('start write...')

# if file_ready(ua_file):
#   ua_str = '\r\n'.join(uas)
#   file_obj = open(ua_file, 'w')
#   file_obj.write(ua_str)
#   file_obj.close()
#   print('ua已写入文件...')

# crawl douban cookie
# print('start get cookie...')
# get_cookie()
# use_cookie()
# print('over...')

# crawl douban user
# print('start crawl user data...')
# from douban_user.crawl_user import get_users
# from douban_spider import spider_login

# request = spider_login()
# user_all = []
# users = get_users(request, '67492098')
# for user in users:
#   user_all.append(user)
#   time.sleep(random.choice(range(1, 10)))
#   _users = get_users(request, user)
#   for _user in _users:
#     user_all.append(_user)

# users_file = os.path.abspath(r'./spider_douban/douban_user/users.txt')
# if file_ready(users_file):
#   ua_str = '\r\n'.join(user_all)
#   file_obj = open(users_file, 'w')
#   file_obj.write(ua_str)
#   file_obj.close()
#   print('users已写入文件...')
# print('user data save success...')


# crawl douban movie
from douban_movie.crawl_movie import MovieSpider
from douban_movie.parse_page import get_movie, get_next
from douban_spider import spider_nologin

userfile = os.path.abspath('./spider_douban/douban_user/users.txt')
# print(open(userfile).read())
users = open(userfile).read().split()
# print(users)

for user in users:
  # collect
  time.sleep(random.choice(range(1, 10)))
  movie_spider = MovieSpider(user, 'movie')
  body = movie_spider.crawl_collect()
  movie_tuple = get_movie(body)
  user_movie = movie_tuple[0]
  movies = movie_tuple[1]
  user_movie_file = os.path.abspath(r'./spider_douban/douban_movie/user_movies/%s_%s.txt' % (user, 'movie'))
  movie_str = '\r\n'.join(user_movie) + '\r\n'
  file_obj = open(user_movie_file, 'a')
  file_obj.write(movie_str)
  file_obj.close()
  movies_file = os.path.abspath(r'./spider_douban/douban_movie/movies.txt')
  movie_str = '\r\n'.join(movies) + '\r\n'
  file_obj = open(movies_file, 'a')
  file_obj.write(movie_str)
  file_obj.close()
  print('movies save success...')
  url_next = get_next(body)
  while url_next:
    time.sleep(random.choice(range(1, 10)))
    body = spider_nologin().open(url_next).read()
    movie_tuple = get_movie(body)
    user_movie = movie_tuple[0]
    movies = movie_tuple[1]
    user_movie_file = os.path.abspath(r'./spider_douban/douban_movie/user_movies/%s_%s.txt' % (user, 'movie'))
    movie_str = '\r\n'.join(user_movie) + '\r\n'
    file_obj = open(user_movie_file, 'a')
    file_obj.write(movie_str)
    file_obj.close()
    movies_file = os.path.abspath(r'./spider_douban/douban_movie/movies.txt')
    movie_str = '\r\n'.join(movies) + '\r\n'
    file_obj = open(movies_file, 'a')
    file_obj.write(movie_str)
    file_obj.close()
    url_next = get_next(body)
    print('movies save success...')
  print('all collect movies saved...')
  # do
  time.sleep(random.choice(range(1, 10)))
  body = movie_spider.crawl_do()
  movie_tuple = get_movie(body)
  user_movie = movie_tuple[0]
  movies = movie_tuple[1]
  user_movie_file = os.path.abspath(r'./spider_douban/douban_movie/user_movies/%s_%s.txt' % (user, 'movie'))
  movie_str = '\r\n'.join(user_movie) + '\r\n'
  file_obj = open(user_movie_file, 'a')
  file_obj.write(movie_str)
  file_obj.close()
  movies_file = os.path.abspath(r'./spider_douban/douban_movie/movies.txt')
  movie_str = '\r\n'.join(movies) + '\r\n'
  file_obj = open(movies_file, 'a')
  file_obj.write(movie_str)
  file_obj.close()
  print('movies save success...')
  url_next = get_next(body)
  while url_next:
    time.sleep(random.choice(range(1, 10)))
    body = spider_nologin().open(url_next).read()
    movie_tuple = get_movie(body)
    user_movie = movie_tuple[0]
    movies = movie_tuple[1]
    user_movie_file = os.path.abspath(r'./spider_douban/douban_movie/user_movies/%s_%s.txt' % (user, 'movie'))
    movie_str = '\r\n'.join(user_movie) + '\r\n'
    file_obj = open(user_movie_file, 'a')
    file_obj.write(movie_str)
    file_obj.close()
    movies_file = os.path.abspath(r'./spider_douban/douban_movie/movies.txt')
    movie_str = '\r\n'.join(movies) + '\r\n'
    file_obj = open(movies_file, 'a')
    file_obj.write(movie_str)
    file_obj.close()
    url_next = get_next(body)
    print('movies save success...')
  print('all do movies saved...')
  # wish
  time.sleep(random.choice(range(1, 10)))
  body = movie_spider.crawl_wish()
  movie_tuple = get_movie(body)
  user_movie = movie_tuple[0]
  movies = movie_tuple[1]
  user_movie_file = os.path.abspath(r'./spider_douban/douban_movie/user_movies/%s_%s.txt' % (user, 'movie'))
  movie_str = '\r\n'.join(user_movie) + '\r\n'
  file_obj = open(user_movie_file, 'a')
  file_obj.write(movie_str)
  file_obj.close()
  movies_file = os.path.abspath(r'./spider_douban/douban_movie/movies.txt')
  movie_str = '\r\n'.join(movies) + '\r\n'
  file_obj = open(movies_file, 'a')
  file_obj.write(movie_str)
  file_obj.close()
  print('movies save success...')
  url_next = get_next(body)
  while url_next:
    time.sleep(random.choice(range(1, 10)))
    body = spider_nologin().open(url_next).read()
    movie_tuple = get_movie(body)
    user_movie = movie_tuple[0]
    movies = movie_tuple[1]
    user_movie_file = os.path.abspath(r'./spider_douban/douban_movie/user_movies/%s_%s.txt' % (user, 'movie'))
    movie_str = '\r\n'.join(user_movie) + '\r\n'
    file_obj = open(user_movie_file, 'a')
    file_obj.write(movie_str)
    file_obj.close()
    movies_file = os.path.abspath(r'./spider_douban/douban_movie/movies.txt')
    movie_str = '\r\n'.join(movies) + '\r\n'
    file_obj = open(movies_file, 'a')
    file_obj.write(movie_str)
    file_obj.close()
    url_next = get_next(body)
    print('movies save success...')
  print('all wish movies saved...')
print('all users movies saved...')
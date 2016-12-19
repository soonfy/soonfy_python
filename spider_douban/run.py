#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider start run.'

__author__ = 'soonfy'

import os
# from openpyxl import Workbook

from middleware import update_ua, get_cookie, use_cookie
from fs import file_ready

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

print('start get cookie...')
# get_cookie()
# use_cookie()
print('over...')

from douban_user.crawl_user import login, get_users

request = login()
user_all = []
users = get_users(request, '67492098')
for user in users:
  user_all.append(user)
  _users = get_users(request, user)
  for _user in _users:
    user_all.append(_user)

users_file = os.path.abspath(r'./spider_douban/douban_user/users.txt')
if file_ready(users_file):
  ua_str = '\r\n'.join(user_all)
  file_obj = open(users_file, 'w')
  file_obj.write(ua_str)
  file_obj.close()
  print('users已写入文件...')
print('user data save success...')

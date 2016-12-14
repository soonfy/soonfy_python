#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider start run.'

__author__ = 'soonfy'

import os
# from openpyxl import Workbook

from middleware import update_ua, get_cookie
from fs import file_ready

# 相对主程序执行路径
ua_file = os.path.abspath(r'./spider_douban/ua.txt')

print('running spider...')
# print(get_ua())
uas = update_ua()
print('crawl ua over...')
print('start write...')

if file_ready(ua_file):
  ua_str = '\r\n'.join(uas)
  file_obj = open(ua_file, 'w')
  file_obj.write(ua_str)
  file_obj.close()
  print('ua已写入文件...')

print('start get cookie...')
get_cookie()
print('over...')
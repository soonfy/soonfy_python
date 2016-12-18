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
get_cookie()
print('over...')

# print('get data...')
# from urllib import request
# url = 'https://www.douban.com/people/67492098/'
# url = '115.182.201.7:443/people/67492098/contacts'
# _user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/54.0.2840.100 Safari/537.36'
# header = {
#   'User-Agent': _user_agent,
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#   'Accept-encoding': 'gzip, deflate, sdch, br',
#   'Accept-Language': 'en-US,en;q=0.8',
#   'Cache-Control': 'max-age=0',
#   'Connection': 'keep-alive',
#   'Upgrade-Insecure-Requests': '1',
#   'Referer': 'https://www.douban.com/accounts/login?redir=https%3A//www.douban.com/people/67492098/contacts',
#   'Host': 'www.douban.com',
#   'Cookie': 'll="108288"; bid=ymuW60Cc8Yg; ps=y; ue="soonfy@163.com"; dbcl2="155042704:Zuhg/BfjypM"; ck=vWvq; push_noty_num=0; push_doumail_num=0; _pk_id.100001.8cb4=bc1d67d9992e154f.1482047650.1.1482050321.1482047650.; _pk_ses.100001.8cb4=*; __utma=30149280.192823874.1482047651.1482047651.1482047651.1; __utmb=30149280.9.10.1482047651; __utmc=30149280; __utmz=30149280.1482047651.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.15504; ap=1'
# }
# req = request.Request(url)
# res = request.urlopen(req).read().decode('utf-8')
# print(res)
# print('get data over...')

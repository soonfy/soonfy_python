#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello')

name = input('name')
print(name)
print('your name is %s, age is %d.' %(name, 18))

print(10.25 / 5)
print(12 / 5)
print(10 / 5)
print(12.25 // 5)
print(12 // 5)
print(12.25 % 5)
print(12 % 5)

if name == 'sf':
  print('right')
else:
  print('wrong')

# import os
# print('process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#   print('child (%s) start, parent is (%s)...' % (os.getpid(), os.getppid()))
# else:
#   print('parent (%s) create child (%s)...' % (os.getpid(), pid))

import re
# 匹配字符串
print(re.match(r'\w{2}\-\d{3}', 'sf-001'))
# 切分字符串
print(re.split(r'\s+', 'sf  0 01'))
# 分组
m = re.match(r'(\w{2})\-(\d{3})', 'sf-001')
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))
# 贪婪/非贪婪
print(re.match(r'(\d+)(0*)', '10200').groups())
print(re.match(r'(\d+?)(0*)', '10200').groups())
print(re.match(r'^(\d+?)(0*)$', '10200').groups())

from datetime import datetime
# 当前时间
now = datetime.now()
print(now)
# 指定时间
dt = datetime(2016, 11, 11, 11, 11, 11)
print(dt)
# 时间戳
dts = dt.timestamp()
print(dts)
# 时间戳转日期
dt = datetime.fromtimestamp(dts)
print(dt)
# str转日期
dt = datetime.strptime('2016-02-02 02:02:02', '%Y-%m-%d %H:%M:%S')
print(dt)
# 日期转str
dt = now.strftime('%Y-%m-%d %H:%M:%S')
print(dt)
# 日期+-
from datetime import timedelta
print(now + timedelta(hours = 10))
print(now - timedelta(days = 1))
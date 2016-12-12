#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'file comment.'

__author__ = 'soonfy'

print('npm test.')

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

user = {
  'name': 'sf',
  'age': 18
}

print(user['name'])
print('bir' in user)
print(user.get('bir'))
# user.pop('age')
print(user.get('age'))
bir = 'bir'
user.get('age', 16)
print(user)

nums = set([1, 2, 4, 2])
print(nums)
nums.add(3)
nums.remove(2)
nos = set([3, 2, 5])
print(nums & nos)
print(nums | nos)

print(list(range(1, 20)))
print([x for x in range(1, 20)])
print([x * x for x in range(1, 20) if x % 2 == 0])
print([x + y for x in range(1, 5) for y in range(6, 10)])

ge = (x for x in range(1, 20))
print(next(ge))
for x in ge:
  print(x)

def func(x):
  return x * x
ge = map(func, [x for x in range(1, 5)])
print(list(ge))
print(sorted([1, 2, -3, 4]))
print(sorted([1, 2, -3, 4], key = abs))
print(sorted([1, 2, -3, 4], key = abs, reverse = True))

def log(func):
  def wrapper(*args, **kw):
    print('start running %s.' % func.__name__)
    func(*args, **kw)
    print('end running %s.' % func.__name__)
  return wrapper

@log
def func():
  print('2016')
func()

class Student(object):
  def __init__(self, name, score, email):
    self.name = name
    self.score = score
    self.__email = email
  def log(self):
    print('%s %s %s' % (self.name, self.score, self.__email))
  def get(self):
    return self.__email
  def set(self, email):
    self.__email = email

sf = Student('sf', 18, '@com')
sf.log()
print(sf.name)
sf.set('@.com')
print(sf.get())

class SenStu(Student):
  def log(self):
    print('%s %s' % (self.name, self.score))

sf = SenStu('sf', 18, '@com')
sf.log()
print(getattr(sf, 'email', 404))

print(type(1))
print(type('sf'))
print(type(True))
print(type([1, 2]))
print(type((1, 2)))
print(type({'name': 'sf'}))
print(type(set()))
print(type(None))
print(dir('sf'))

class User(object):
  name = 'sf'

sf = User()
qw = User()
sf.name = 'qw'
print(sf.name)
print(qw.name)

class Student(object):
  @property
  def score(self):
    return self._score
  
  @score.setter
  def score(self, value):
    self._score = value

sf = Student()
sf.score = 18
print(sf.score)

try:
  print('try:')
  no = 10/0
except Exception as e:
  print('except:')
  print(e)
finally:
  print('finally:')
print('end:')

file = open('package.json', 'r')
print(file.read())
file.close()

with open('package.json', 'r') as file:
  print(file.read())

file = open('package.json', 'r')
print(file.read(100))
print(file.readline())
print(file.readlines())
file.close()

import os
print(os.name)
print(os.uname())
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.join('.', 'package.json'))
os.mkdir('/home/soonfy/personal/python/demo')
os.rmdir('/home/soonfy/personal/python/demo')
print(os.path.split('/home/soonfy/personal/python/package.json'))
print(os.path.splitext('/home/soonfy/personal/python/package.json'))
os.rename('demo.txt', 'demo.md')
os.remove('demo.md')

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

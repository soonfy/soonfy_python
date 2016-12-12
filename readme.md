# python  

## 基本输入输出  

  1. print(str1, str2)  

  2. imput(information)  

## 基本数据类型  

  1. number  
  ```
  10.25/5 => 2.05
  12/5 => 2.4
  10/5 => 2.0
  12.25//5 => 2.0
  12//5 => 2
  12.25%5 => 2.25
  12%5 => 2
  ```

  2. string  
  ```
  'this is a text.'
  "this's a text."
  'this\'s a text.'
  '''line 1.
  line 2.
  line 3.'''
  r'this\'s is a text.' => r表示不转义字符串
  'your name is %s, age is %d.' %('sf', 18)
  'percent is %d%%.' %(18) => %%转义%
  ```

  3. boolean  
  ```
  True
  False
  True and False
  True or False
  not False
  ```

  4. none  
  ```
  None
  ```

  5. list  
  ```
  names = ['sf', 'qw']
  len(names)
  names[0]
  names[-1]
  names.append('sq')
  names.insert(1, 'sq')
  names.pop()
  names.pop(1)
  arr = ['sf', 18, True, ['sf', 'qw']]
  ```

  6. tuple  
  不能修改的数组
  ```
  names = ('sf', 'qw')
  ```

  7. if-elif-else  
  ```
  name = 'sf'
  if name == 'sf':
    print('sf')
  else:
    print('wrong')
  ```

  8. for-in/while  
  ```
  names = ['sf', 'qw']
  for name in names:
    print(name)
  num = 100
  sum = 0
  while num > 0:
    sum += num
    num--
  print(sum)
  ```

## 进程,线程  

```
import os
print('process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
  print('child (%s) start, parent is (%s)...' % (os.getpid(), os.getppid()))
else:
  print('parent (%s) create child (%s)...' % (os.getpid(), pid))
```

## 正则表达式  
```
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
```

## 内建模块  

  1. 日期时间  
  ```
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
  ```

  2. 
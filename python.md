# python  

## 高级特性  

  1. 切片  
  string, tuple也支持切片  
  ```
  nos = [1, 2, 3, 4, 5]
  nos[1:3] => 2, 3
  nos[-2:-1] => 4
  nos[:2] => 1, 2
  nos[-2:] => 4, 5
  nos[:4:2] => 1, 3
  nos[::3] => 1, 4
  ```

  2. 迭代  
  可遍历对象都支持迭代  
  ```
  for no in [1, 2, 3]:
    print(no)
  for key in {'name': 'sf', 'age': 18}:
    print(key)
  for value in {'name': 'sf', 'age': 18}:
    print(value)
  for x, y in [(1, 2), (2, 4)]:
    print(x, y)
  ```

  3. 列表生成式  
  ```
  list(range(1, 20))
  [x for x in range(1, 20)]
  [x * x for x in range(1, 20)]
  [x * x for x in range(1, 20) if x % 2 == 0]
  [x + y for x in range(1, 5) for y in range(6, 10)]
  ```

  4. 生成器  
  算法
  ```
  列表
  ge = (x for x in range(1, 20))
  for x in ge:
    print(x)
  函数
  def ge(max):
    n, a, b = 0, 0, 1
    while n < max:
      yield b
      a, b = b, a + b
      n = n + 1
    return 'done'
  ```

  5. map/reduce  
  map: 第一个参数是函数，第二个参数是可遍历对象，返回值是迭代器。  
  reduce: 第一个参数是函数，第二个参数是可遍历对象。ruduce(f, [a, b, c]) => f(f(a, b), c)  
  ```
  def func(x):
    return x * x
  ge = map(func, [x for x in range(1, 5)])
  list(ge)
  ```

  6. filter  
  filter: 第一个参数是函数，第二个参数是可遍历对象，返回值是迭代器。  
  ```
  def func(x):
    return x % 2 == 0
  ge = filter(func, [x for x in range(1, 5)])
  list(ge)
  ```

  7. sorted  
  sorted: 第一个参数是可遍历对象，第二个参数是排序规则，第三个参数是反转。  
  ```
  sorted([1, 2, -3, 4])
  sorted([1, 2, -3, 4], key = abs)
  sorted([1, 2, -3, 4], key = abs, reverse = True)
  ```

  8. lambda  
  匿名函数
  ```
  map(lambda x: x * x, [1, 2, 3])
  ```

  9. 装饰器  
  函数的_\_name_\_属性返回函数名称。  
  实际运行的不是装饰器紧接的func函数，是装饰器内部封装的wrapper函数。  
  ```
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
  ```

  10. 第三方模块  
  图片处理 => PIL/Pillow  
  mysql => mysql-connector-python  
  科学计算 => numpy  
  文本模板 => Jinja2  

  11. class  
  ```
  class Student(object):
    def __init__(self, name, age, score):
      self.name = name
      self.__age = age
      self.score = score
    def get(self):
      return self.__age
    def set(self, age):
      self.__age = age
    def log(self):
      print('%s %s %s' % (self.name, self.__age, self.score))

  sf = Student('sf', 18)

  class SubStu(Student):
    def log(self):
      print('%s %s %s' % (self.name, self.__age, self.score)) => error,无法获得父类内部属性__age
  ```

  12. 判断对象类型  
  int, str, bool, list, tuple, dict, set, NoneType  
  ```
  基本类型
  type(123)
  类
  isinstance(sf, Student)
  对象的属性和方法
  dir('sf')
  类的属性和方法
  hasattr(sf, 'name')
  getattr(sf, 'name')
  getattr(sf, 'name', 404) =>404是不存在name属性的缺省值
  setattr(sf, 'age', 18)
  ```

  13. 限制类的属性  
  ```
  class Student(object):
    __slots__ = ('name', 'age')
  ```

  14. @property  
  把类的方法转换为类的属性  
  ```
  class Student(object):
    @property
    def score(self):
      return self.score
    
    @score.setter
    def score(self, value):
      self._score = value
  ```

  15. 定制类  
  ```
  __str__设置用户返回字符串
  __repr__设置调试返回字符串
  class Student(object):
    def __init__(self, name):
      self.name = name
    def __str__(self):
      return 'object name is %s.' % self.name
    __repr__ = __str__

  __iter__和__next__遍历
  __getitem__,__setitem__,__delitem__根据下标处理元素
  ```

  16. 调试  
  print()打印  
  assert()断言  
  logging()日志  
  -m pdb调试器  
  pdb.set_trace()断点  
  IDE

  17. 文件读写  
  打开文件 => 读到内存/写入文件 => 关闭文件  
  read(size), readline(), readlines()  
  如果文件很小，read()一次性读取最方便  
  如果不能确定文件大小，反复调用read(size)最方便  
  如果是配置文件，调用readlines()最方便  
  ```
  file = open('package.json', 'r', encoding = 'gbk', errors = 'ignore')
  file.read()
  file.close()
  with自带关闭
  with open('package.json', 'r') as file:
    file.read()
  ```

  18. 序列化  

    * 文件序列化  
    python => pickle.dumps() ==> pickle.dump() => file  
    file => open => pickle.loads() => python  
    
    * JSON序列化  
    python => json.dumps() => json_str  
    json_str => json.loads() => pathon  

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

  2. 集合  
  ```
  from collections import namedtuple
  # 自定义tuple对象
  Point = namedtuple('Point', ['x', 'y'])
  p = Point(1, 2)
  print(p.x, p.y)
  from collections import deque
  # 双向队列
  que = deque([1, 2, 3])
  que.append(4)
  que.appendleft(0)
  print(que)
  from collections import defaultdict
  # dict默认值
  dd = defaultdict(lambda: 'N/A')
  dd['x'] = 1
  print(dd['x'], dd['y'])
  from collections import OrderedDict
  # dict排序
  d = OrderedDict([('b', 1), ('c', 2), ('a', 3)])
  print(d)
  print(list(d.keys()))
  from collections import Counter
  c = Counter()
  for ch in 'helloelse':
    c[ch] = c[ch] + 1
  print(c)
  ```
  
  3. base64  
  二进制转换字符串  
  ```
  import base64
  base64.b64.encode()
  base64.b64decode()
  ```

  4. struct  
  字节转换二进制  
  ```
  import struct
  struct.pack()
  struct.unpack()
  ```

  5. hashlib  
  摘要算法  
  ```
  import hashlib
  md = hashlib.md5()
  md.update('soonfy'.encode('utf-8'))
  print(md.hexdigest())
  sha = hashlib.sha1()
  sha.update('soonfy'.encode('utf-8'))
  print(sha.hexdigest())
  ```

  6. itertools  
  迭代函数  
  ```
  import itertools
  natu = itertools.count(1, 2)
  # for no in natu:
  #   print(no)

  cs = itertools.cycle('abcd')
  # for ch in cs:
  #   print(ch)

  re = itertools.repeat('abc', 3)
  for ch in re:
    print(ch)

  for ch in itertools.chain('abc', 'xyz'):
    print(ch)

  for key, group in itertools.groupby('AAaabbBBccaa'):
    print(key, list(group))

  for key, group in itertools.groupby('AAaabbBBccaa', lambda c: c.upper()):
    print(key, list(group))
  ```

  7. contextlib  
  上下文  

  8. XML  
  解析XML  

  9. HTMLParser  
  解析HTML  

  10. urllib  
  请求url  

## 第三方模块  

  1. PIL(python2)/pillow(python3)  
  图片处理  

  2. virtualenv  
  虚拟运行环境  

  3. tkinter  
  图形界面  

  4. 网络编程  

    * tcp  
    socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    socket.connect() => 参数是tuple(ip, port)
    socket.send() => 参数是字节
    ```
    # tcp编程
    # client: 创建socket => 建立链接 => 发送请求 => 接受数据 => 关闭链接
    # server: 创建socket => 绑定ip:port => 监听请求 => 新建进程/线程 => 关闭链接
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.sina.com.cn', 80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    buff = []
    while True:
      d = s.recv(1024)
      if(d):
        buff.append(d)
      else:
        break
    data = b''.join(buff)
    s.close()
    header, html = data.split(b'\r\n\r\n', 1)
    # print(html)
    print(header)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))
    for data in [b'sf', b'qw', b'zx']:
      s.send(data)
      print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()
    ```

    * udp  
    socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ```
    # udp编程
    # client: 创建socket => 发送数据 => 接受数据 => 关闭socket
    # server: 创建socket => 绑定ip:port => 监听请求 => 新建进程/线程 => 关闭链接
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'sf', b'qw']:
      s.sendto(data, ('127.0.0.1', 9999))
      print(s.recv(1024).decode('utf-8'))
    s.close()
    ```

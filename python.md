# python  

## dict, set  

1. dict  
```
user = {
  'name': 'sf',
  'age': 18
}
user['name']
'bir' in user => False
user.get('bir') => None
user.get('bir', 2) =>不能使用？
user.pop('age')
```

2. set  
```
nums = set([1, 2, 4, 2])
nums.add(3)
nums.remove(1)
nos = set([3, 0])
nums & nos
nums | nos
```

## function  
*args是可变参数，args接收的是一个tuple；  
**kw是关键字参数，kw接收的是一个dict。  
```
函数
def max_sf(a, b):
  return a, b
默认参数
def max_sf(a, b = 0):
  return a, b
可选参数
def max_sf(*nos):
  return *nos
关键词参数
def max_sf(**nos):
  return **nos
命名关键词参数
def max_sf(a, b, *, c)
  return a, b, c
```

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


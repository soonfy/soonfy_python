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


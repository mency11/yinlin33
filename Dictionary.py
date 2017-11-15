Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
>>> print "dict['Name']: ", dict['Name']
dict['Name']:  Zara
>>> print "dict['Age']: ", dict['Age']
dict['Age']:  7
>>> print "dict['Class']: ", dict['Class']
dict['Class']:  First
>>> print "dict['Alice']: ", dict['Alice']
dict['Alice']: 

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print "dict['Alice']: ", dict['Alice']
KeyError: 'Alice'
>>> dict['Age'] = 8
>>> dict['School'] = "DPS School"
>>> print "dict['Age']: ", dict['Age']
dict['Age']:  8
>>> print "dict['School']: ", dict['School']
dict['School']:  DPS School
>>> del dict['Name']
>>> print "dict['Name']: ", dict['Name']
dict['Name']: 

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print "dict['Name']: ", dict['Name']
KeyError: 'Name'
>>> dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
>>> print "dict['Name']: ", dict['Name']
dict['Name']:  Manni
>>> dict = {['Name']: 'Zara', 'Age': 7}

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    dict = {['Name']: 'Zara', 'Age': 7}
TypeError: unhashable type: 'list'
>>> dict1 = {'Name': 'Zara', 'Age': 7}
>>> dict2 = {'Name': 'Mahnaz', 'Age': 27}
>>> dict3 = {'Name': 'Abid', 'Age': 27}
>>> dict4 = {'Name': 'Zara', 'Age': 7}
>>> 
KeyboardInterrupt
>>> cmp (dict1, dict2)
-1
>>> cmp (dict2, dict3)
1
>>> cmp (dict1, dict4)
0
>>> dict = {'Name': 'Zara', 'Age': 7}
>>> len (dict)
2
>>> str (dict)
"{'Age': 7, 'Name': 'Zara'}"
>>> type (dict)
<type 'dict'>
>>> dict.clear()
>>> len(dict)
0
>>> dict1 = {'Name': 'Zara', 'Age': 7}
>>> dict2 = dict1.copy()
>>> str(dict2)
"{'Age': 7, 'Name': 'Zara'}"
>>> seq = ('name', 'age', 'sex')
>>> dict = dict.fromkeys(seq)
>>> str(dict)
"{'age': None, 'name': None, 'sex': None}"
>>> dict = dict.fromkeys(seq, 10)
>>>  str(dict)
 
  File "<pyshell#34>", line 2
    str(dict)
    ^
IndentationError: unexpected indent
>>> str(dict)
"{'age': 10, 'name': 10, 'sex': 10}"
>>> dict = {'Name': 'Zara', 'Age': 27}
>>> dict.get('Age')
27
>>> dict.get('Sex')
>>> dict.has_key('Age')
True
>>> dict.has_key('Sex')
False
>>> dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
>>> dict.items()
[('Google', 'www.google.com'), ('taobao', 'www.taobao.com'), ('Runoob', 'www.runoob.com')]
>>> for key,values in  dict.items():
	print key,values

Google www.google.com
taobao www.taobao.com
Runoob www.runoob.com
>>> dict.keys()
['Google', 'taobao', 'Runoob']
>>> dict.setdefault('Runoob')
'www.runoob.com'
>>> dict = {'Name': 'Zara', 'Age': 7}
>>> dict2 = {'Sex': 'female' }
>>> dict.update(dict2)
>>> print "Value : %s" %  dict
Value : {'Age': 7, 'Name': 'Zara', 'Sex': 'female'}
>>> dict.values()
[7, 'Zara', 'female']
>>> site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
>>> pop_obj=site.pop('name')
>>> print pop_obj
菜鸟教程
>>> pop_obj=site.popitem()
>>> print(pop_obj)
('url', 'www.runoob.com')
>>> print(site)
{'alexa': 10000}
>>> 

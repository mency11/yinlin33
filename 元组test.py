Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1 = ('physics', 'chemistry', 1997, 2000)
>>> tup1[0]
'physics'
>>> list_test = ['a','b','c']
>>> list_test.append('d')
>>> list_test
['a', 'b', 'c', 'd']
>>> tup3 = "a", "b", "c", "d"
>>> tup3
('a', 'b', 'c', 'd')
>>> tup1 = (12, 34.56)
>>> tup2 = ('abc', 'xyz')
>>> tup3 = tup1 + tup2
>>> print tup3
(12, 34.56, 'abc', 'xyz')
>>> tup = ('physics', 'chemistry', 1997, 2000)
>>> print tup
('physics', 'chemistry', 1997, 2000)
>>> del tup
>>> print tup

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print tup
NameError: name 'tup' is not defined
>>> len(tup1)
2
>>> len(tup2)
2
>>> len(tup3)
4
>>> tup1 * 2
(12, 34.56, 12, 34.56)
>>> 3 in (1,2,3)
True
>>> for 3 in (1,2,,3):
	
SyntaxError: invalid syntax
>>> for x in (1,2,3):
	print x

1
2
3
>>> L = ('spam', 'Spam', 'SPAM!')
>>> L[2]
'SPAM!'
>>> L[-2]
'Spam'
>>> L[1:]
('Spam', 'SPAM!')
>>> print 'abc', -4.24e93, 18+6.6j, 'xyz'
abc -4.24e+93 (18+6.6j) xyz
>>> x, y = 1, 2
>>> print "Value of x , y : ", x,y
Value of x , y :  1 2
>>> tuple1 = (1,2,3,4,5)
>>> tuple2 = (3,4)
>>> cmp(tuple1,tuple2)
-1
>>> len(tuple1)
5
>>> max(tuple2)
4
>>> min(tuple1)
1
>>> list1 = [1, 2, 3, 4, 5 ]
>>> tuple(list1)
(1, 2, 3, 4, 5)
>>> 

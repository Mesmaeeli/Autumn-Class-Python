Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s5.py ==
>>> func(3)
9
>>> import func
>>> tavan2(4)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tavan2(4)
NameError: name 'tavan2' is not defined
>>> func.tavan2(2)
4
>>> func.tavan3(4)
64
>>> func.jazr(16)
4.0
>>> func.pi
3.14
>>> 
=============================== RESTART: Shell ===============================
>>> func(3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    func(3)
NameError: name 'func' is not defined
>>> from func import tavan2
>>> tavan2(4)
16
>>> 
=============================== RESTART: Shell ===============================
>>> from m1 import func
>>> from m2 import func
>>> func(4)
64
>>> 
=============================== RESTART: Shell ===============================
>>> import m1
>>> import m2
>>> m1.func(2)
4
>>> m2.func(2)
8
>>> 
=============================== RESTART: Shell ===============================
>>> import func as fc
>>> fc.tavan2(2)
4
>>> 
=============================== RESTART: Shell ===============================
>>> from m1 import func
>>> m1.func(3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    m1.func(3)
NameError: name 'm1' is not defined
>>> def f(a,b):
	if a > 10:
		return a
	if b < 10:
		return b

	
>>> f(11,3)
11
>>> f(9,3)
3
>>> def f(a,b):
	if a > 10:
		return a
		if b < 10:
			return b

		
>>> 
=============================== RESTART: Shell ===============================
>>> import os
>>> os.getcwd()
'C:\\Users\\esmae\\AppData\\Local\\Programs\\Python\\Python36'
>>> import m1
>>> os.chdir('C:\Users\esmae')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir('C:\\Users\\esmae')
>>> os.getcwd()
'C:\\Users\\esmae'
>>> import math
>>> 
=============================== RESTART: Shell ===============================
>>> import math
>>> math.sin(0)
0.0
>>> math.cos(0)
1.0
>>> math.sin(90)
0.8939966636005579
>>> import math,os,tkinter
>>> 
=============================== RESTART: Shell ===============================
>>> from math import sin,cos
>>> sin(0)
0.0
>>> cos(0)
1.0
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11-s5.py ==
yek adad vared konidyek
adad ro be sorat argham vared konid12
144
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11-s5.py ==
yek adad vared konid12
ejraye bedune khata
144
>>> def func():
	print('salam')

	
>>> func(12)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    func(12)
TypeError: func() takes 0 positional arguments but 1 was given
>>> func()
salam
>>> class People:
	name = ''
	id_number = 0

	
>>> p1 = People()
>>> type(p1)
<class '__main__.People'>
>>> str1 = 'salam'
>>> type(str1)
<class 'str'>
>>> print(p1.name)

>>> print(p1.id_number)
0
>>> p1.name
''
>>> p1.name = 'ali'
>>> p1.name
'ali'
>>> p1.id_number = 129
>>> p1.id_number
129
>>> p2 = People()
>>> type(p2)
<class '__main__.People'>
>>> p2.name
''
>>> p2.id_number
0
>>> p2.name = 'hasan'
>>> p2.id_number = 120
>>> p2
<__main__.People object at 0x0000026E5D546940>
>>> p1
<__main__.People object at 0x0000026E5D4EC6A0>
>>> l1 = [5,3,5]
>>> l1
[5, 3, 5]
>>> l1
[5, 3, 5]
>>> p1
<__main__.People object at 0x0000026E5D4EC6A0>
>>> print(p1)
<__main__.People object at 0x0000026E5D4EC6A0>
>>> hasattr(p1,'name')
True
>>> hasattr(p2,'age')
False
>>> getattr(p1,'name')
'ali'
>>> getattr(p2,'id_number')
120
>>> setattr(p1,'name','mohammad')
>>> p1
<__main__.People object at 0x0000026E5D4EC6A0>
>>> p1.name
'mohammad'
>>> delattr(p1,'name')
>>> p1.name
''
>>> p1.age = 30
>>> p1.age
30
>>> p2.age
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    p2.age
AttributeError: 'People' object has no attribute 'age'
>>> setattr(p2,'age',40)
>>> p2.age
40
>>> p2.name
'hasan'
>>> delattr(p2,'name')
>>> p2.name
''
>>> delattr(p2,'age')
>>> p2.age
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    p2.age
AttributeError: 'People' object has no attribute 'age'
>>> class coordinate:
	x = 0
	y = 0

	
>>> coord1 = coordinate()
>>> coord1.x
0
>>> coord1.y
0
>>> coord1 = 3
>>> coord1 = coordinate()
>>> coord1.x = 3
>>> coord1.y = 4
>>> def func(obj):
	return x ** 2 + y ** 2

>>> func(coord1)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    func(coord1)
  File "<pyshell#117>", line 2, in func
    return x ** 2 + y ** 2
NameError: name 'x' is not defined
>>> def func(obj):
	return (coord1.x ** 2 + coord1.y ** 2)**0.5

>>> func(coord1)
5.0
>>> func(5)
5.0
>>> func('int')
5.0
>>> 
=============================== RESTART: Shell ===============================
>>> class coordinate:
	x = 0
	y = 0

	
>>> coord1 = coordinate()
>>> coord1.x = 3
>>> coord1.y = 4
>>> def func(obj):
	return x ** 2 + y ** 2

>>> func(coord1)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    func(coord1)
  File "<pyshell#130>", line 2, in func
    return x ** 2 + y ** 2
NameError: name 'x' is not defined
>>> def func(obj):
	return (coord1.x ** 2 + coord1.y ** 2)**0.5

>>> func(coord1)
5.0
>>> func(5)
5.0
>>> def func(obj):
	return (obj.x ** 2 + obj.y ** 2)**0.5

>>> func(coord1)
5.0
>>> func(3)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    func(3)
  File "<pyshell#137>", line 2, in func
    return (obj.x ** 2 + obj.y ** 2)**0.5
AttributeError: 'int' object has no attribute 'x'
>>> int('salam')
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    int('salam')
ValueError: invalid literal for int() with base 10: 'salam'
>>> def func1(arg):
	return arg ** 2

>>> func1(3)
9
>>> def fasele(p1,p2):
	return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)** 0.5

>>> coord2 = coordinate()
>>> coord2.x = 12
>>> coord2.y = 5
>>> fasele(coord1,coord2)
9.055385138137417
>>> fasele(coord1,coord1)
0.0
>>> fasele(coord1,12)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    fasele(coord1,12)
  File "<pyshell#147>", line 2, in fasele
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)** 0.5
AttributeError: 'int' object has no attribute 'x'
>>> t1 = (12,5)
>>> t2 = (4,7)
>>> t1[0]
12
>>> t2[0]
4
>>> p1.x
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    p1.x
NameError: name 'p1' is not defined
>>> coord1.x
3
>>> coord2.x
12
>>> l1 = [4,5,6]
>>> l1.append(4)
>>> s1 = {4,5,6,8}
>>> s1.add(5)
>>> class coordinate:
	x = 0
	y = 0
	def fasele_az(obj):
		return (obj.x ** 2 + obj.y ** 2)**0.5

	
>>> 
=============================== RESTART: Shell ===============================
>>> class coordinate:
	x = 0
	y = 0
	def fasele_az(obj):
		return (obj.x ** 2 + obj.y ** 2)**0.5

	
>>> p1 = coordinate()
>>> p1.x
0
>>> p1.y
0
>>> p1.x = 3
>>> p1.y = 4
>>> p1.fasele_az()
5.0
>>> def func(arg):
	return arg ** 2

>>> l1 = [5,6,8]
>>> p1.fasele_az()
5.0
>>> p2 = coordintae()
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    p2 = coordintae()
NameError: name 'coordintae' is not defined
>>> p2 = coordinate()
>>> p2.x = 12
>>> p2.y = 13
>>> p2.fasele_az()
17.69180601295413
>>> class coordinate:
	x = 0
	y = 0
	def fasele_az(obj):
		return (obj.x ** 2 + obj.y ** 2)**0.5
	def show():
		print('x in noghte: ',x,'y in noghte: ',y)

		
>>> p2 = coordinate()
>>> p2.x = 12
>>> p2.y = 13
>>> p2.show()
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    p2.show()
TypeError: show() takes 0 positional arguments but 1 was given
>>> class coordinate:
	x = 0
	y = 0
	def fasele_az(self):
		return (self.x ** 2 + self.y ** 2)**0.5
	def show(self):
		print('x in noghte: ',x,'y in noghte: ',y)

		
>>> p2 = coordinate()
>>> p2.x = 12
>>> p2.y = 13
>>> p2.show()
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    p2.show()
  File "<pyshell#197>", line 7, in show
    print('x in noghte: ',x,'y in noghte: ',y)
NameError: name 'x' is not defined
>>> class coordinate:
	x = 0
	y = 0
	def fasele_az(self):
		return (self.x ** 2 + self.y ** 2)**0.5
	def show(self):
		print('x in noghte: ',self.x,'y in noghte: ',self.y)

		
>>> p2 = coordinate()
>>> p2.x = 12
>>> p2.y = 13
>>> p2.show()
x in noghte:  12 y in noghte:  13
>>> 3 + 2j ** 2
(-1+0j)
>>> class coordinate:
	def __init__(self, arg1,arg2):
		self.x = arg1
		self.y = arg2
		
	def fasele_az(self):
		return (self.x ** 2 + self.y ** 2)**0.5
	def show(self):
		print('x in noghte: ',self.x,'y in noghte: ',self.y)

		
>>> p3 = coordinate()
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    p3 = coordinate()
TypeError: __init__() missing 2 required positional arguments: 'arg1' and 'arg2'
>>> p3 = coordinate(3,4)
>>> p3.x
3
>>> p3.y
4
>>> class coordinate:
	def __init__(self, arg1 = 0,arg2 = 0):
		self.x = arg1
		self.y = arg2

	def fasele_az(self):
		return (self.x ** 2 + self.y ** 2)**0.5
	def show(self):
		print('x in noghte: ',self.x,'y in noghte: ',self.y)

		
>>> 
>>> p4 = coordinate(3)
>>> p4.x
3
>>> p4.y
0
>>> l1 = [4,67,2]
>>> l2 = [6,10,5,18]
>>> l1 + l2
[4, 67, 2, 6, 10, 5, 18]
>>> 45 + 32
77
>>> def ezafe(obj1,obj2):
	return (obj1.x + obj2.x,obj1.y + obj2.y)

>>> p4.x
3
>>> p4.y
0
>>> p5 = coordinate(10,6)
>>> ezafe(p4,p5)
(13, 6)
>>> class coordinate:
	def __init__(self, arg1 = 0,arg2 = 0):
		self.x = arg1
		self.y = arg2

	def fasele_az(self):
		return (self.x ** 2 + self.y ** 2)**0.5
	def show(self):
		print('x in noghte: ',self.x,'y in noghte: ',self.y)
	def ezafe(self,other):
		return (self.x + other.x,self.y + other.y)

	
>>> p5 = coordinate(10,6)
>>> p4 = coordinate(5,3)
>>> p5.ezafe(p4)
(15, 9)
>>> class coordinate:
	def __init__(self, arg1 = 0,arg2 = 0):
		self.x = arg1
		self.y = arg2

	def fasele_az(self):
		return (self.x ** 2 + self.y ** 2)**0.5
	def show(self):
		print('x in noghte: ',self.x,'y in noghte: ',self.y)
	def ezafe3(self,other1,other2):
		return (self.x + other1.x + other2.x,self.y + other1.y + other2.y)

	
>>> p5 = coordinate(10,6)
>>> p4 = coordinate(5,3)
>>> p5.ezafe3(p4,p5)
(25, 15)
>>> p5 + p4
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    p5 + p4
TypeError: unsupported operand type(s) for +: 'coordinate' and 'coordinate'
>>> str1 = 'salam'
>>> str2 = 'hi'
>>> str1 * str2
Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    str1 * str2
TypeError: can't multiply sequence by non-int of type 'str'
>>> class coordinate:
	def __init__(self, arg1 = 0,arg2 = 0):
		self.x = arg1
		self.y = arg2

	def fasele_az(self):
		return (self.x ** 2 + self.y ** 2)**0.5
	def show(self):
		print('x in noghte: ',self.x,'y in noghte: ',self.y)
	def ezafe3(self,other1,other2):
		return (self.x + other1.x + other2.x,self.y + other1.y + other2.y)
	def __add__(self,other):
		return (self.x + other.x,self.y + other.y)

	
>>> p5 = coordinate(10,6)
>>> p4 = coordinate(5,3)
>>> p5 + p4
(15, 9)
>>> class coordinate:
	def __init__(self, arg1 = 0,arg2 = 0):
		self.x = arg1
		self.y = arg2

	def fasele_az(self):
		return (self.x ** 2 + self.y ** 2)**0.5
	def show(self):
		print('x in noghte: ',self.x,'y in noghte: ',self.y)
	def ezafe3(self,other1,other2):
		return (self.x + other1.x + other2.x,self.y + other1.y + other2.y)
	def __add__(self,other):
		X = self.x + other.x
		Y = self.y + other.y
		if X > 10:
			X -= 10
			Y += 1
		return (X,Y)

	
>>> p5 = coordinate(10,6)
>>> p4 = coordinate(5,3)
>>> p4 + p5
(5, 10)
>>> print(p4)
<__main__.coordinate object at 0x00000229D26D5FD0>
>>> p4
<__main__.coordinate object at 0x00000229D26D5FD0>
>>> str1 = 'salam'
>>> print(str1)
salam
>>> str1
'salam'
>>> class coordinate:
	def __init__(self, arg1 = 0,arg2 = 0):
		self.x = arg1
		self.y = arg2

	def fasele_az(self):
		return (self.x ** 2 + self.y ** 2)**0.5
	def show(self):
		print('x in noghte: ',self.x,'y in noghte: ',self.y)
	def ezafe3(self,other1,other2):
		return (self.x + other1.x + other2.x,self.y + other1.y + other2.y)
	def __add__(self,other):
		X = self.x + other.x
		Y = self.y + other.y
		if X > 10:
			X -= 10
			Y += 1
		return (X,Y)
	def __str__(self):
		return (str(self.x)+':'+str(self.y))

	
>>> p4 = coordinate(5,3)
>>> print(p4)
5:3
>>> print(p4)
5:3
>>> p4
<__main__.coordinate object at 0x00000229D26D5C88>
>>> class coordinate:
	def __init__(self, arg1 = 0,arg2 = 0):
		self.x = arg1
		self.y = arg2

	def fasele_az(self):
		return (self.x ** 2 + self.y ** 2)**0.5
	def show(self):
		print('x in noghte: ',self.x,'y in noghte: ',self.y)
	def ezafe3(self,other1,other2):
		return (self.x + other1.x + other2.x,self.y + other1.y + other2.y)
	def __add__(self,other):
		X = self.x + other.x
		Y = self.y + other.y
		if X > 10:
			X -= 10
			Y += 1
		return (X,Y)
	def __str__(self):
		return (str(self.x)+':'+str(self.y))
	def __repr__(self):
		return (str(self.x)+':'+str(self.y))

	
>>> p4 = coordinate(5,3)
>>> print(p4)
5:3
>>> p4
5:3
>>> p4.show()
x in noghte:  5 y in noghte:  3
>>> print(p4)
5:3
>>> p4
5:3
>>> 
= RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/class_s5.py =
>>> p4 = coordinate(3,4)
>>> p5 = coordinate(5,10)
>>> p4 + p5
(8, 14)
>>> p4.show()
x in noghte:  3 y in noghte:  4
>>> 
= RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/class_s5.py =
(8, 14)
x in noghte:  3 y in noghte:  4
>>> 
= RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/class_s5.py =
(8, 14)
x in noghte:  3 y in noghte:  4
3:4
>>> class coordinate:
	def __init__(self, arg1 = 0,arg2 = 0):
		self.x = arg1
		self.y = arg2

	def fasele_az(self):
		return (self.x ** 2 + self.y ** 2)**0.5
	def show(self):
		print('x in noghte: ',self.x,'y in noghte: ',self.y)
	def ezafe3(self,other1,other2):
		return (self.x + other1.x + other2.x,self.y + other1.y + other2.y)
	def __add__(self,other):
		X = self.x + other.x
		Y = self.y + other.y
		if X > 10:
			X -= 10
			Y += 1
		return (X,Y)
	def __str__(self):
		return (str(self.x)+':'+str(self.y))
	def __repr__(self):
		return (str(self.x)+':'+str(self.y))
	def __sub__(self,other):
		return (self.x - other.x, self.y - other.y)

	
>>> p4 = coordinate(3,4)
>>> p5 = coordinate(5,10)
>>> p5 - p4
(2, 6)
>>> p4 = coordinate(3,4)
>>> p4.x
3
>>> p4.y
4
>>> 

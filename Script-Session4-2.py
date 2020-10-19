Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = {3,2,6,9}
>>> b = {5,38,1}
>>> a.isdisjoint()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.isdisjoint()
TypeError: isdisjoint() takes exactly one argument (0 given)
>>> a.isdisjoint(b)
True
>>> A = {}
>>> type(A)
<class 'dict'>
>>> B = set()
>>> B
set()
>>> type(B)
<class 'set'>
>>> str1 = 'salam man {} hastam'
>>> str1
'salam man {} hastam'
>>> str1.format('mohammad')
'salam man mohammad hastam'
>>> str2 = 'man {} sen daram saken {} hastam'
>>> str2.format(25,'tehran')
'man 25 sen daram saken tehran hastam'
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(10,1)
range(10, 1)
>>> list(range(10,1))
[]
>>> list(range(10,1,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2]
>>> point = [(1,5),(4,9),(10,6),(2,0)]
>>> for sub in point:
	print(sub)

	
(1, 5)
(4, 9)
(10, 6)
(2, 0)
>>> for sub in point:
	print('x: ',sub[0])
	print('y: ',sub[1])

	
x:  1
y:  5
x:  4
y:  9
x:  10
y:  6
x:  2
y:  0
>>> for subx,suby in point:
	print(subx,suby)

	
1 5
4 9
10 6
2 0
>>> point
[(1, 5), (4, 9), (10, 6), (2, 0)]
>>> for subx,suby,subz in point:
	print(subx,suby)

	
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    for subx,suby,subz in point:
ValueError: not enough values to unpack (expected 3, got 2)
>>> point = [(1,5),(4,9),(10,5,6),(2,0)]
>>> 
>>> for subx,suby in point:
	print(subx,suby)

	
1 5
4 9
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    for subx,suby in point:
ValueError: too many values to unpack (expected 2)
>>> for sub in reversed(point):
	print(sub)

	
(2, 0)
(10, 5, 6)
(4, 9)
(1, 5)
>>> for sub in enumerate(point):
	print(sub)

	
(0, (1, 5))
(1, (4, 9))
(2, (10, 5, 6))
(3, (2, 0))
>>> point
[(1, 5), (4, 9), (10, 5, 6), (2, 0)]
>>> x = [4,8,9]
>>> y = [0,12,3]
>>> zip(x,y)
<zip object at 0x000001797687FF08>
>>> list(zip(x,y))
[(4, 0), (8, 12), (9, 3)]
>>> for sub in zip(x,y):
	print(sub)

	
(4, 0)
(8, 12)
(9, 3)
>>> z = [9,76,100]
>>> list(zip(x,y,z))
[(4, 0, 9), (8, 12, 76), (9, 3, 100)]
>>> z = [5,2,19,100]
>>> list(zip(x,y,z))
[(4, 0, 5), (8, 12, 2), (9, 3, 19)]
>>> point = [1,5,4,9,10,6,2]
>>> for sub in point:
	if sub % 2 == 0:
		print(sub)

		
4
10
6
2
>>> point = [6,8,10,3,8,0]
>>> for sub in point:
	if sub % 2 != 0:
		break
	print(sub)

	
6
8
10
>>> str1 = salam man mohammad hastam'
SyntaxError: invalid syntax
>>> str1 = 'salam man mohammad hastam'
>>> index = 0
>>> while index < len(str1):
	if str1[index] == 'h':
		break
	print(str1[index])
	index += 1

	
s
a
l
a
m
 
m
a
n
 
m
o
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
19 passed
13 passed
20 passed
12 passed
18 passed
20 passed
done
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
19 passed
13 passed
20 passed
12 passed
18 passed
20 passed
done
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
19 passed
13 passed
failed
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py", line 15, in <module>
    if grade(index) < 10:
TypeError: 'list' object is not callable
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
19 passed
13 passed
20 passed
12 passed
18 passed
20 passed
done
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
19 passed
13 passed
failed
>>> str1
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    str1
NameError: name 'str1' is not defined
>>> str1 = 'man mohammad hastam'
>>> for sub in str1:
	if sub == 'h':
		continue
	print(sub)

	
m
a
n
 
m
o
a
m
m
a
d
 
a
s
t
a
m
>>> index = 0
>>> while index < len(str1):
	if str1[index] == 'a':
		continue
	print(str1[index])
	index += 1

	
m
Traceback (most recent call last):
  File "<pyshell#86>", line 3, in <module>
    continue
KeyboardInterrupt
>>> while index < len(str1):
	if str1[index] == 'a':
		index += 1
		continue
	print(str1[index])
	index += 1

	
n
 
m
o
h
m
m
d
 
h
s
t
m
>>> index = 0
>>> while index < len(str1):
	if str1[index] == 'a':
		index += 1
		continue
	print(str1[index])
	index += 1

	
m
n
 
m
o
h
m
m
d
 
h
s
t
m
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
19 passed
13 passed
failed
12 passed
18 passed
20 passed
done
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
19 passed
13 passed
failed
12 passed
18 passed
20 passed
done
>>> grade
[19, 13, 9, 12, 18, 20]
>>> for i in grade:
	pass

>>> for i in grade:
	continue

>>> def func():
	""" In tabe argoman nemigire faghat salam chap mikone """
	print('salam')

	
>>> func()
salam
>>> def func1():
	return('salam')

>>> func1()
'salam'
>>> result = func()
salam
>>> result
>>> result
>>> type(result)
<class 'NoneType'>
>>> result = func1()
>>> result
'salam'
>>> def zarb(num1,num2):
	return(num1*num2)

>>> zarb(5,3)
15
>>> zarb('salam',2)
'salamsalam'
>>> zarb('salam','ali')
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    zarb('salam','ali')
  File "<pyshell#130>", line 2, in zarb
    return(num1*num2)
TypeError: can't multiply sequence by non-int of type 'str'
>>> zarb(12,2,3)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    zarb(12,2,3)
TypeError: zarb() takes 2 positional arguments but 3 were given
>>> zarb(1)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    zarb(1)
TypeError: zarb() missing 1 required positional argument: 'num2'
>>> def zojyafard(Num):
	if Num % 2 == 0:
		return('zoj')
	else:
		return('fard')

	
>>> zojyafard(12)
'zoj'
>>> zojyafard(15)
'fard'
>>> def zojyafard(Num):
	if Num % 2 == 0:
		return('zoj')
	return('fard')

>>> zojyafard(12)
'zoj'
>>> zojyafard(15)
'fard'
>>> def zojyafard(Num):
	if Num % 2 == 0:
		return 'zoj'
	return 'fard'

>>> zojyafard(12)
'zoj'
>>> zojyafard(15)
'fard'
>>> def bakhshpaziribar2va3(Num):
	if Num % 2 == 0:
		if Num % 3 == 0:
			return ('bakhsh 2','bakhsh 3')
		return 'bakhsh 2'
	else:
		if Num % 3 == 0:
			return 'bakhsh 3'
	return 'hichkodum'

>>> bakhshpaziribar2va3(9)
'bakhsh 3'
>>> bakhshpaziribar2va3(4)
'bakhsh 2'
>>> bakhshpaziribar2va3(6)
('bakhsh 2', 'bakhsh 3')
>>> bakhshpaziribar2va3(7)
'hichkodum'
>>> def twice(obj):
	print(obj,obj)

	
>>> twice('salam')
salam salam
>>> twice(12)
12 12
>>> def prime(Num):
	for sub in range(2,Num):
		if Num % sub == 0:
			return 'aval nist'
		return 'aval'

	
>>> prime(8)
'aval nist'
>>> prime(5)
'aval'
>>> def prime(Num):
	for sub in range(2,Num):
		if Num % sub == 0:
			return False
		return True

	
>>> prime(13)
True
>>> zarb(12,14)
168
>>> zarb(num2 = 14,num1 = 12)
168
>>> 
>>> def func(num1, num2 = 0):
	return num1 ** num 2
SyntaxError: invalid syntax
>>> def func(num1, num2 = 0):
	return num1 ** num2

>>> func(2,3)
8
>>> func(2)
1
>>> def func(num1 = 1, num2 = 0):
	return num1 ** num2

>>> func()
1
>>> func(num1 = 5)
1
>>> adad = 5
>>> func(adad,3)
125
>>> def jam(obj):
	result:
	for i in obj:
		
SyntaxError: invalid syntax
>>> def jam(obj):
	result = 0
	for i in obj:
		result += i
	return result

>>> jam([12,4,2,6,83,3])
110
>>> def jam(*arg):
	print('done')

	
>>> jam(12,4,6)
done
>>> jam(4)
done
>>> jam()
done
>>> jam(4,4,4,4,4,4,4,4)
done
>>> print('s')
s
>>> print('s','a','m')
s a m
>>> def jam(*arg):
	print(arg)

	
>>> jam()
()
>>> jam(1)
(1,)
>>> jam(12,3,4,6,8)
(12, 3, 4, 6, 8)
>>> obj1 = (1)
>>> obj2 = (1,2)
>>> obj3 = (1,)
>>> type(obj)
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    type(obj)
NameError: name 'obj' is not defined
>>> type(obj1)
<class 'int'>
>>> def jam(*arg):
	result = 0
	for sub in arg:
		result += sub
	return result

>>> jam()
0
>>> jam(12)
12
>>> jam(12,2)
14
>>> jam(5,5,5,5,5)
25
>>> def jam(*arg,Num):
	result = 0
	for sub in arg:
		result += sub
	return result * Num

>>> jam(5,5,2)
Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    jam(5,5,2)
TypeError: jam() missing 1 required keyword-only argument: 'Num'
>>> jam(5,5,Num = 2)
20
>>> def jam(*arg):
	result = 0
	for sub in arg[:-1]:
		result += sub
	return result * arg[-1]

>>> jam(5,5,2)
20
>>> def jam(*arg, *arg1):
	
SyntaxError: invalid syntax
>>> def func(Num):
	if Num >= 0:
		return Num
	return Num ** 2

>>> func(4)
4
>>> func(-5)
25
>>> def func(Num)L
SyntaxError: invalid syntax
>>> def func(Num):
	result = 1
	while Num > 1:
		result *= Num
		Num -= 1
	return result

>>> func(5)
120
>>> func(3)
6
>>> def func(Num):
	if Num == 1:
		return 1
	else:
		return Num * func(Num -1)

	
>>> func(3)
6
>>> func(5)
120
>>> def func(Num):
	return Num * func(Num -1)

>>> func(4)
Traceback (most recent call last):
  File "<pyshell#279>", line 1, in <module>
    func(4)
  File "<pyshell#278>", line 2, in func
    return Num * func(Num -1)
  File "<pyshell#278>", line 2, in func
    return Num * func(Num -1)
  File "<pyshell#278>", line 2, in func
    return Num * func(Num -1)
  [Previous line repeated 991 more times]
RecursionError: maximum recursion depth exceeded
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
>>> func(5)
120
>>> (lambda x : x**2)(4)
16
>>> (lambda x , y : x ** y)(2,3)
8
>>> l1 = [3,4,6,4,8,0]
>>> def func(x):
	return x**2

>>> func(3)
9
>>> map(func,l1)
<map object at 0x000001B5640AD5C0>
>>> list(map(func,l1))
[9, 16, 36, 16, 64, 0]
>>> list(map(lambda x:x**3,l1))
[27, 64, 216, 64, 512, 0]
>>> t1 = (5,3,6,8)
>>> tuple(map(lambda x:x**3,t1))
(125, 27, 216, 512)
>>> l1 = [5,2,5,7,5,2,24,12,4,9,0]
>>> def func(x):
	return x % 2 == 0

>>> func(4)
True
>>> func(5)
False
>>> filter(func,l1)
<filter object at 0x000001B5640998D0>
>>> list(filter(func,l1))
[2, 2, 24, 12, 4, 0]
>>> list(filter(lambda x : x % 3 == 0, l1))
[24, 12, 9, 0]
>>> def func(Num):
	return Num**2

>>> func('salam')
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    func('salam')
  File "<pyshell#305>", line 2, in func
    return Num**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> Num = 10
>>> isinstance(Num,'int')
Traceback (most recent call last):
  File "<pyshell#308>", line 1, in <module>
    isinstance(Num,'int')
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> isinstance(Num,'str')
Traceback (most recent call last):
  File "<pyshell#309>", line 1, in <module>
    isinstance(Num,'str')
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> isinstance(Num,int)
True
>>> def func(Num):
	if isinstance(Num,int):
		return Num**2
	else:
		print('vorudi na motabar')

		
>>> func(5)
25
>>> func('salam')
vorudi na motabar
>>> def func1(Num1,Num2):
	return Num1/Num2

>>> func1(12,4)
3.0
>>> func1(12,0)
Traceback (most recent call last):
  File "<pyshell#321>", line 1, in <module>
    func1(12,0)
  File "<pyshell#319>", line 2, in func1
    return Num1/Num2
ZeroDivisionError: division by zero
>>> def func1(Num1,Num2):
	assert Num2 != 0
	return Num1/Num2

>>> func1(12,4)
3.0
>>> func1(12,0)
Traceback (most recent call last):
  File "<pyshell#325>", line 1, in <module>
    func1(12,0)
  File "<pyshell#323>", line 2, in func1
    assert Num2 != 0
AssertionError
>>> def func1(Num1,Num2):
	assert Num2 != 0 "Num2 hatman mokhalef sefr bayad bashad"
	return Num1/Num2
SyntaxError: invalid syntax
>>> 
>>> def func1(Num1,Num2):
	assert Num2 != 0,"Num2 hatman mokhalef sefr bayad bashad"
	return Num1/Num2

>>> func1(12,0)
Traceback (most recent call last):
  File "<pyshell#330>", line 1, in <module>
    func1(12,0)
  File "<pyshell#329>", line 2, in func1
    assert Num2 != 0,"Num2 hatman mokhalef sefr bayad bashad"
AssertionError: Num2 hatman mokhalef sefr bayad bashad
>>> def julian_date(d,m,y):
	months = [31,28,31,30,31,30,31,31,30,31,30,31]
	result = 0
	if isinstance(d,int) and isinstance(m,int) and isinstance(y,int):
		if y % 400 or (y % 4 == 0 and y % 100 != 0):
			months[1] = 29
		result = sum(months[:m-1]) + d
		return result

	
>>> julian_date(1,3,2000)
60
>>> def julian_date(d,m,y):
	months = [31,28,31,30,31,30,31,31,30,31,30,31]
	result = 0
	if isinstance(d,int) and isinstance(m,int) and isinstance(y,int):
		if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
			months[1] = 29
		result = sum(months[:m-1]) + d
		return result

	
>>> 
>>> julian_date(1,3,2000)
61
>>> julian_date(1,3,2001)
60
>>> julian_date(1,3,2400)
61
>>> julian_date(1,3,2100)
60
>>> julian_date('s','m',2000)
>>> def julian_date(d,m,y):
	months = [31,28,31,30,31,30,31,31,30,31,30,31]
	result = 0
	if isinstance(d,int) and isinstance(m,int) and isinstance(y,int):
		if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
			months[1] = 29
		result = sum(months[:m-1]) + d
		return result
	return 'vorudi na motabar'

>>> julian_date('s','m',2000)
'vorudi na motabar'
>>> assert 10 > 0
>>> assert 10 < 0
Traceback (most recent call last):
  File "<pyshell#355>", line 1, in <module>
    assert 10 < 0
AssertionError
>>> try:
	Num1 = 10
	Num2 = 5
	Num3 = 0
	print(Num1 / Num2)
except:
	print('be khata khordim')

	
2.0
>>> try:
	Num1 = 10
	Num2 = 5
	Num3 = 0
	print(Num1 / Num3)
except:
	print('be khata khordim')

	
be khata khordim
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
adad aval ro vared konid: 3
adad dovvom ro vared konid: 0
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py", line 39, in <module>
    print(Num1 /Num2)
ZeroDivisionError: division by zero
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
adad aval ro vared konid: 3
adad dovvom ro vared konid: 0
khata khordim
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
adad aval ro vared konid: 12
adad dovvom ro vared konid: 0
khata khordim
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
adad aval ro vared konid: 12
adad dovvom ro vared konid: 3
4.0
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py", line 40, in <module>
    print(Num3)
NameError: name 'Num3' is not defined
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
adad aval ro vared konid: 12
adad dovvom ro vared konid: 3
4.0
moteghayer nashenakhte
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
>>> julian_date(60,3,2000)
120
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s4.py ==
>>> julian_date(60,3,2000)
ruz kamtar az 31 bashad29
>>> 

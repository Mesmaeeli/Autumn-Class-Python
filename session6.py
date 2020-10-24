Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3 & 5
1
>>> 3 | 5
7
>>> 
>>> 3 | 12
15
>>> 3 ^ 12
15
>>> 3 ^ 5
6
>>> Num = 10
>>> while Num > 0:
	print('salam')

	
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    print('salam')
KeyboardInterrupt
>>> 2 > 0
True
>>> 2 > 0
True
>>> l1 = [4,3,5,7,83]
>>> import numpy
>>> 
=============================== RESTART: Shell ===============================
>>> import numpy as np
>>> a1 = np.array([4,5,2,7,8])
>>> type(a1)
<class 'numpy.ndarray'>
>>> print(a1)
[4 5 2 7 8]
>>> a1.dtype
dtype('int32')
>>> a1.shape
(5,)
>>> a1.ndim
1
>>> a2 = np.array([9,0,1,2,12])
>>> l1 = [1,2,3,4,6]
>>> l2 = [6,3,5,7,112]
>>> a1
array([4, 5, 2, 7, 8])
>>> a2
array([ 9,  0,  1,  2, 12])
>>> l1
[1, 2, 3, 4, 6]
>>> l2
[6, 3, 5, 7, 112]
>>> l1 + l2
[1, 2, 3, 4, 6, 6, 3, 5, 7, 112]
>>> a1 + a2
array([13,  5,  3,  9, 20])
>>> l1 * l2
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    l1 * l2
TypeError: can't multiply sequence by non-int of type 'list'
>>> a1 * a2
array([36,  0,  2, 14, 96])
>>> l1 * 3
[1, 2, 3, 4, 6, 1, 2, 3, 4, 6, 1, 2, 3, 4, 6]
>>> a1 * 3
array([12, 15,  6, 21, 24])
>>> a1
array([4, 5, 2, 7, 8])
>>> a1[0]
4
>>> id(a1)
1997373868672
>>> a1[0] = 10
>>> a1
array([10,  5,  2,  7,  8])
>>> id(a1)
1997373868672
>>> a1[:3]
array([10,  5,  2])
>>> a1[3:-1]
array([7])
>>> a1.fill(12)
>>> a1
array([12, 12, 12, 12, 12])
>>> a1[:] = 3
>>> a1
array([3, 3, 3, 3, 3])
>>> a1.dtype
dtype('int32')
>>> a1.fill(10.6)
>>> a1
array([10, 10, 10, 10, 10])
>>> a1[2] = 13.4
>>> a1
array([10, 10, 13, 10, 10])
>>> a1[::2]
array([10, 13, 10])
>>> a3 = np.array([[ [3,4,9] , [12,1,0] ])
		  
SyntaxError: invalid syntax
>>> a3 = np.array([ [3,4,9] , [12,1,0] ])
		  
>>> a3
		  
array([[ 3,  4,  9],
       [12,  1,  0]])
>>> l3 = [ [3,4,9] , [12,1,0] ]
		  
>>> l3
		  
[[3, 4, 9], [12, 1, 0]]
>>> a3 * 2
		  
array([[ 6,  8, 18],
       [24,  2,  0]])
>>> l3 * 2
		  
[[3, 4, 9], [12, 1, 0], [3, 4, 9], [12, 1, 0]]
>>> a3.shape
		  
(2, 3)
>>> a3.ndim
		  
2
>>> a3.size
		  
6
>>> a3
		  
array([[ 3,  4,  9],
       [12,  1,  0]])
>>> a3[0][1]
		  
4
>>> a3[0,1]
		  
4
>>> l3
		  
[[3, 4, 9], [12, 1, 0]]
>>> l3[0][1]
		  
4
>>> l3[0,1]
		  
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    l3[0,1]
TypeError: list indices must be integers or slices, not tuple
>>> 

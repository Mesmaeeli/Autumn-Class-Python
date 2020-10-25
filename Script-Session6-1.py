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
>>> a4 = np.array([1.1,2.3,3.14])
		  
>>> a4
		  
array([1.1 , 2.3 , 3.14])
>>> a4.dtype
		  
dtype('float64')
>>> a5 = np.array([5,2,6,3,6,1,2,4,7])
		  
>>> index = [4,3,5,0]
		  
>>> a5[index]
		  
array([6, 3, 1, 5])
>>> index = [True,False,False,True,False,True,False,True,True]
		  
>>> a5[index]
		  
array([5, 3, 1, 4, 7])
>>> a5 < 4
		  
array([False,  True, False,  True, False,  True,  True, False, False])
>>> a5[a5 < 5]
		  
array([2, 3, 1, 2, 4])
>>> l1
		  
[1, 2, 3, 4, 6]
>>> l1 > 3
		  
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    l1 > 3
TypeError: '>' not supported between instances of 'list' and 'int'
>>> a5 < 4
		  
array([False,  True, False,  True, False,  True,  True, False, False])
>>> a = np.array([[2,3,5],[6,9,10]])
		  
>>> a
		  
array([[ 2,  3,  5],
       [ 6,  9, 10]])
>>> a.reshape(3,2)
		  
array([[ 2,  3],
       [ 5,  6],
       [ 9, 10]])
>>> a.reshape(1,6)
		  
array([[ 2,  3,  5,  6,  9, 10]])
>>> a.reshape(4,5)
		  
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.reshape(4,5)
ValueError: cannot reshape array of size 6 into shape (4,5)
>>> A
		  
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    A
NameError: name 'A' is not defined
>>> a
		  
array([[ 2,  3,  5],
       [ 6,  9, 10]])
>>> a.transpose()
		  
array([[ 2,  6],
       [ 3,  9],
       [ 5, 10]])
>>> a
		  
array([[ 2,  3,  5],
       [ 6,  9, 10]])
>>> a.T
		  
array([[ 2,  6],
       [ 3,  9],
       [ 5, 10]])
>>> a
		  
array([[ 2,  3,  5],
       [ 6,  9, 10]])
>>> a[a>3,[1,2]]
		  
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a[a>3,[1,2]]
IndexError: too many indices for array
>>> a>3
		  
array([[False, False,  True],
       [ True,  True,  True]])
>>> b1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
		  
>>> b1
		  
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> b1[(0,1,2),(0,1,2)]
		  
array([1, 5, 9])
>>> i = (0,1,2)
		  
>>> b1[i,i]
		  
array([1, 5, 9])
>>> b1.diagonal()
		  
array([1, 5, 9])
>>> b1.diagonal(offset = 1)
		  
array([2, 6])
>>> b1.diagonal(offset = -1)
		  
array([4, 8])
>>> b1.diagonal(offset = 2)
		  
array([3])
>>> b1.diagonal(offset = -2)
		  
array([7])
>>> b1.diagonal(offset = 5)
		  
array([], dtype=int32)
>>> b1.diagonal(offset = -5)
		  
array([], dtype=int32)
>>> a1 = np.array([5,4,6,8],dtype = 'float16')
		  
>>> a1
		  
array([5., 4., 6., 8.], dtype=float16)
>>> a1.astype('int32')
		  
array([5, 4, 6, 8])
>>> l1
		  
[1, 2, 3, 4, 6]
>>> sum(l1)
		  
16
>>> b1
		  
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np.sum(b1)
		  
45
>>> np.sum(b1,axis = 0)
		  
array([12, 15, 18])
>>> np.sum(b1,axis = 1)
		  
array([ 6, 15, 24])
>>> z1 = np.array([ [[1,2,3],[4,5,6],[7,8,9]], [[10,11,12],[13,14,15],[16,17,18]]  ])
		  
>>> z1
		  
array([[[ 1,  2,  3],
        [ 4,  5,  6],
        [ 7,  8,  9]],

       [[10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]]])
>>> z1.shape
		  
(2, 3, 3)
>>> z1.ndim
		  
3
>>> z1.size
		  
18
>>> np.sum(z1)
		  
171
>>> np.sum(z1,axis = 0)
		  
array([[11, 13, 15],
       [17, 19, 21],
       [23, 25, 27]])
>>> np.sum(z1,axis = 1)
		  
array([[12, 15, 18],
       [39, 42, 45]])
>>> z1
		  
array([[[ 1,  2,  3],
        [ 4,  5,  6],
        [ 7,  8,  9]],

       [[10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]]])
>>> np.sum(z1,axis = 2)
		  
array([[ 6, 15, 24],
       [33, 42, 51]])
>>> np.sum(z1,axis = -1)
		  
array([[ 6, 15, 24],
       [33, 42, 51]])
>>> b1
		  
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np.sum(b1,axis = -1)
		  
array([ 6, 15, 24])
>>> min(l1)
		  
1
>>> max(l1)
		  
6
>>> b1
		  
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np.min(b1)
		  
1
>>> np.min(b1,axis = -1)
		  
array([1, 4, 7])
>>> np.max(b1,axis = -2)
		  
array([7, 8, 9])
>>> z1
		  
array([[[ 1,  2,  3],
        [ 4,  5,  6],
        [ 7,  8,  9]],

       [[10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]]])
>>> np.max(z1,axis = -3)
		  
array([[10, 11, 12],
       [13, 14, 15],
       [16, 17, 18]])
>>> np.mean(b1)
		  
5.0
>>> np.mean(b1,axis = -1)
		  
array([2., 5., 8.])
>>> b1
		  
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np.var(b1,axis = -2)
		  
array([6., 6., 6.])
>>> np.std(b1,axis = -1)
		  
array([0.81649658, 0.81649658, 0.81649658])
>>> x1 = np.array([1.2,2.3,5.5,6.5,7.8])
		  
>>> np.round(x1)
		  
array([1., 2., 6., 6., 8.])
>>> x1
		  
array([1.2, 2.3, 5.5, 6.5, 7.8])
>>> x2 = np.array([1.5,1.5,2.5])
		  
>>> np.round(x2)
		  
array([2., 2., 2.])
>>> x3 = np.array([1.24,2.35,2.45,8.5])
		  
>>> np.round(x3,decimals = 1)
		  
array([1.2, 2.4, 2.4, 8.5])
>>> np.round(x2,decimals = 1)
		  
array([1.5, 1.5, 2.5])
>>> np.arange(0,10)
		  
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a = np.arange(0,100).reshape(10,10)
		  
>>> a
		  
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
       [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
       [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
       [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
       [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
       [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]])
>>> a = np.arange(0,12).reshape(2,2,3)
		  
>>> a
		  
array([[[ 0,  1,  2],
        [ 3,  4,  5]],

       [[ 6,  7,  8],
        [ 9, 10, 11]]])
>>> np.ones((2,3),dtype = 'float16')
		  
array([[1., 1., 1.],
       [1., 1., 1.]], dtype=float16)
>>> np.zeros((4,4))
		  
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> np.identity(5)
		  
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
>>> np.linspace(0,10,50)
		  
array([ 0.        ,  0.20408163,  0.40816327,  0.6122449 ,  0.81632653,
        1.02040816,  1.2244898 ,  1.42857143,  1.63265306,  1.83673469,
        2.04081633,  2.24489796,  2.44897959,  2.65306122,  2.85714286,
        3.06122449,  3.26530612,  3.46938776,  3.67346939,  3.87755102,
        4.08163265,  4.28571429,  4.48979592,  4.69387755,  4.89795918,
        5.10204082,  5.30612245,  5.51020408,  5.71428571,  5.91836735,
        6.12244898,  6.32653061,  6.53061224,  6.73469388,  6.93877551,
        7.14285714,  7.34693878,  7.55102041,  7.75510204,  7.95918367,
        8.16326531,  8.36734694,  8.57142857,  8.7755102 ,  8.97959184,
        9.18367347,  9.3877551 ,  9.59183673,  9.79591837, 10.        ])
>>> np.linspace(0,1,5)
		  
array([0.  , 0.25, 0.5 , 0.75, 1.  ])
>>> np.logspace(0,1,5)
		  
array([ 1.        ,  1.77827941,  3.16227766,  5.62341325, 10.        ])
>>> np.logspace(0,1,5,base = 2)
		  
array([1.        , 1.18920712, 1.41421356, 1.68179283, 2.        ])
>>> np.random.randint()
		  
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    np.random.randint()
  File "mtrand.pyx", line 910, in mtrand.RandomState.randint
TypeError: randint() takes at least 1 positional argument (0 given)
>>> np.random.randint(1)
		  
0
>>> np.random.randint(10)
		  
3
>>> np.random.randint(10)
		  
2
>>> np.random.randn(4)
		  
array([-1.1113167 , -0.84452278, -1.1995909 ,  1.74269269])
>>> np.pi
		  
3.141592653589793
>>> np.e
		  
2.718281828459045
>>> x = np.linspace(0,2 * np.pi, 10)
		  
>>> x
		  
array([0.        , 0.6981317 , 1.3962634 , 2.0943951 , 2.7925268 ,
       3.4906585 , 4.1887902 , 4.88692191, 5.58505361, 6.28318531])
>>> x * 2
		  
array([ 0.        ,  1.3962634 ,  2.7925268 ,  4.1887902 ,  5.58505361,
        6.98131701,  8.37758041,  9.77384381, 11.17010721, 12.56637061])
>>> y = np.sin(x)
		  
>>> y
		  
array([ 0.00000000e+00,  6.42787610e-01,  9.84807753e-01,  8.66025404e-01,
        3.42020143e-01, -3.42020143e-01, -8.66025404e-01, -9.84807753e-01,
       -6.42787610e-01, -2.44929360e-16])
>>> import matplotlib.pyplot as plt
		  
>>> plt.plot(x,y)
		  
[<matplotlib.lines.Line2D object at 0x000001D11EC163C8>]
>>> plt.show()
		  
>>> x = np.linspace(0,2 * np.pi, 100)
		  
>>> y = np.sin(x)
		  
>>> plt.plot(x,y)
		  
[<matplotlib.lines.Line2D object at 0x000001D11EF9A978>]
>>> plt.show()
		  
>>> plt.plot(np.cos(x))
		  
[<matplotlib.lines.Line2D object at 0x000001D11F140F60>]
>>> plt.show()
		  
>>> plt.plot(x,np.sin(x),x,np.cos(x))
		  
[<matplotlib.lines.Line2D object at 0x000001D11F2E6F60>, <matplotlib.lines.Line2D object at 0x000001D11F2F0128>]
>>> plt.show()
		  
>>> plt.plot(x,np.sin(x),'r-^')
		  
[<matplotlib.lines.Line2D object at 0x000001D11F492550>]
>>> plt.show()
		  
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s6.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s6.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s6.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s6.py ==
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s6.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s6.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s6.py ==

=============================== RESTART: Shell ===============================
>>> 
=============================== RESTART: Shell ===============================
>>> __name__
		  
'__main__'
>>> import m1
		  
>>> 
==== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\m1.py ====
>>> func(3)
		  
__main__
9
>>> import m1
		  
>>> m1.func(3)
		  
m1
9
>>> 

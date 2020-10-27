Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==
>>> p1 = (23,45)
>>> i,j = p1
>>> i
23
>>> j
45
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py", line 20, in <module>
    axes[2,1].plt(x,y1)
AttributeError: 'AxesSubplot' object has no attribute 'plt'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py ==
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11-s7.py", line 36, in <module>
    plt.plot(x, y)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\pyplot.py", line 2811, in plot
    is not None else {}), **kwargs)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\axes\_axes.py", line 1611, in plot
    for line in self._get_lines(*args, **kwargs):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\axes\_base.py", line 393, in _grab_next_args
    yield from self._plot_args(this, kwargs)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\axes\_base.py", line 370, in _plot_args
    x, y = self._xy_from_xy(x, y)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\axes\_base.py", line 231, in _xy_from_xy
    "have shapes {} and {}".format(x.shape, y.shape))
ValueError: x and y must have same first dimension, but have shapes (5,) and (6,)
>>> x = np.linspace(0,10,10)
>>> x
array([ 0.        ,  1.11111111,  2.22222222,  3.33333333,  4.44444444,
        5.55555556,  6.66666667,  7.77777778,  8.88888889, 10.        ])
>>> np.e ** (-x/10)
array([1.        , 0.89483932, 0.8007374 , 0.71653131, 0.64118039,
       0.57375342, 0.51341712, 0.45942582, 0.41111229, 0.36787944])
>>> np.power(np.e , -x/10)
array([1.        , 0.89483932, 0.8007374 , 0.71653131, 0.64118039,
       0.57375342, 0.51341712, 0.45942582, 0.41111229, 0.36787944])
>>> np.e ** -x/10
array([1.00000000e-01, 3.29192988e-02, 1.08368023e-02, 3.56739933e-03,
       1.17436285e-03, 3.86592014e-04, 1.27263380e-04, 4.18942123e-05,
       1.37912809e-05, 4.53999298e-06])
>>> theta = np.linspace(0,np.pi * 2,10)
>>> r = 0.8 + np.cos(theta)
>>> D =
SyntaxError: invalid syntax
>>> R = (60/180)*np.pi
>>> np.cos(R)
0.5000000000000001
>>> 

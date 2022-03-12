""" Numpy """
# It is a library available in python for scientific computing.
# how to create a numpy array
import numpy as np
a = np.array([1, 2, 3])
print(a)    # prints a single dimensional array
b = np.array([(1, 2, 3), (4, 5, 6)])
print(b)  # two dimensional array

""" numpy vs list - less memory, fast, convenient"""
# occupies less space
import numpy as np
import sys

S = range(1000)
print(sys.getsizeof(5)*len(S))  # shows the memory occupied by list

D = np.arange(1000)
print(D.size*D.itemsize)    # shows memory occupied by  numpy array

# faster and more convenient
import numpy as np
import time
import sys

SIZE = 1000000

L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()

# calculating the  result of the lists
result = [(x, y) for x, y in zip(L1, L2)]
print((time.time() - start)*1000)

start = time.time()

# calculating the result of np array
result = A1 + A2  # shows convenience because it does not need looping
print((time.time() - start)*1000)

""" Numpy operations  """
import numpy as np
a = np.array([(1, 2, 3), (2, 3, 4)])
print(a.ndim)  # prints the dimension
print(a.itemsize)  # prints the bytes size
print(a.dtype)  # prints the data type
print(a.size)  # prints size of array - number of elements
print(a.shape) # rows and columns

# reshaping- changing the number of rows and columns
a = np.array([(1, 2, 3, 4), (3, 4, 5, 6)])  # 2 rows and 4 columns
print(a)
# converting to 4 rows and 2 columns
a = a.reshape(4, 2)
print(a)

# slicing - extracting particular lists of elements from your array
a = np.array([(1, 2, 3, 4), (3, 4, 5, 6), (7, 8, 9, 10)])
print(a[0, 2])
print(a[0:2, 3])
print(a[0:, 3])   # prints from both rows

import numpy as np
a = np.linspace(1, 3, 5)  # prints the 5 values that are equally spaced between 1 and 3
b = np.linspace(1, 3, 10)  # prints 10 values between 1 to 3
print(a)
print(b)

import numpy as np
a = np.array([1, 2, 3])
print(a.max())  # maximum value
print(a.min())  # minimum value
print(a.sum())

# axis concept - rows are called axis one and columns are called axis zero
import numpy as np
a = np.array([(0, 4, 8), (10, 20, 30)])
print(a.sum(axis=0))
print(a.sum(axis=1))

# finding the square root
a = np.array([(4, 16, 64), (9, 49, 81)])
print(np.sqrt(a))
print(np.std(a))  # printing the standard deviation

# matrix addition,subtraction and multiplication
import numpy as np
a = np.array([(1, 2, 3), (4, 5, 6)])
b = np.array([(1, 2, 3), (4, 5, 6)])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# vertical stacking and horizontal stacking
import numpy as np
a = np.array([(1, 2, 3), (4, 5, 6)])
b = np.array([(1, 2, 3), (4, 5, 6)])
print(np.vstack((a, b)))
print(np.hstack((a, b)))
print(a.ravel())  # convert np.array into a single column

""" numpy special functions - sine and cosine function """
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

# cosine function
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 3*np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.show()

# log and exponential functions
import numpy as np
import matplotlib.pyplot as plt
a = np.array([1, 2, 3])
print(np.exp(a))
print(np.log10(a))  # not writing based 10 will give the natural log which is based to e


""" Scipy """
# It is a library used to solve scientific and mathematical problems. Built on numpy.
# Allows manipulation and visualizing
# sub-packages in scipy:

# cluster- clustering algorithms
# constants - physical and mathematical constants
# fftpack - fast fourier transform routines
# integrate - integration and ODE solvers
# interpolate- interpolation and smoothing splines
# io - input and output
# linalg - linear algebra
# ndimage - N dimensional image processing
# odr - orthogonal image processing
# optimize - optimization and route finding routines
# signal - signal processing
# sparse - sparse matrices and associated routines
# spatial -spatial data structures and algorithims
# special - special functions
# stat - statistical distributions and functions

from scipy import cluster
help(cluster)

""" special functions """
# exponential functions
from scipy import special
a = special.exp10(2) # computes 10 power x
b = special.exp2(3)
print(a)
print(b)

# trigonometric functions
c = special.sindg(90)  # returns sin value of 90 degrees
b = special.cosdg(90)
print(c)
print(b)

# Integration function
# quad - calculates the integral of a function which has one variable
# dblquad function calculates double integral of a function which has two variables

from scipy import integrate, special
f = lambda x: special.exp10(x)
i = integrate.quad(f, 0, 1)
print(i)

# Example 2
# Define the function; $f(x) = e^{-x**2} - this can be done using the lambda expression
import scipy.integrate
from numpy import exp
f = lambda x: exp(-x**2)
# f is the name of the function to be integrated whereas a and b are the lower and upper limits
i = scipy.integrate.quad(f, 0, 1)
print(i)

# double integration - consists of two real variables
from scipy import integrate
f = lambda x, y: x*y**2
e = lambda x: 1
g = lambda x: -1
# func is the name of the function to be integrated ,a and b are lower and upper limits of the variable while
# f and g are the names of the functions that define the the lower and the upper limits of the y variable
print(integrate.dblquad(f, 0, 2, e, g))

# Example 2
# $$\int_{0}^{1/2} dy \int_{0}^{\sqrt{1-4y^2}} 16xy \:dx$$
import scipy.integrate
from math import sqrt
f = lambda x, y: 16*x*y
g = lambda x: 0
h = lambda y: sqrt(1-4*y**2)
i = scipy.integrate.dblquad(f, 0, 0.5, g, h)
print(i)

# Fourier Transformations
# fourier analysis is  a method that deals with expressing  a function as a sum of periodic components
# and recovering the signal from those components
# the fft and ifft functions can  be used t return the discrete fourier transformation of a real/complex sequence
from scipy.fftpack import fft,ifft
import numpy as np
x = np.array([1, 2, 3, 4])
y = fft(x)
z = ifft(x)     # the reverse fourier transform of x
print(y)
print(z)

# Linear Algebra
from scipy import linalg
a = np.array([(1, 2), (3, 4)])
b = linalg.inv(a)  # computing the inverse of a
print(b)

# Interpolating Functions - constructing new data points within a set of known data points
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
x = np.arange(5, 20)
y = np.exp(x/3.0)
f = interpolate.interp1d(x, y)  # making use of the interp 1d function to find x1 and y1 which range between x and y
x1 = np.arange(6, 12)
y1 = f(x1)  # use interpolation function returned by 'interp1d'
plt.plot(x, y, 'o', x1, y1, '-')
plt.show()  # x1 and y1 have been computed between x and y


# 1 - D interpolation (interp1d)
# interp1d class in scipy is  a convenient  to create a function based on fixed data points
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 10, num=41, endpoint=True)
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()

""" More examples """
# drawing data points
import numpy as np
import matplotlib.pyplot as plt
x =np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)
plt.plot(x, y, 's')
plt.show()

# creating a function based on the fixed data points
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
x =np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)
# the third variable kind represents the type of interpolation technique:
# 'Linear', 'Nearest', 'Zero', 'Slinear', 'Quadratic', 'Cubic' are a few techniques of interpolation.
f1 = interp1d(x, y, kind='linear')
f2 = interp1d(x, y, kind='cubic')
x_new = np.linspace(0, 4, 30)
plt.plot(x, y, 'o', x_new, f1(x_new), '-', x_new, f2(x_new), '--')
plt.legend(['data', 'linear', 'cubic', 'nearest'], loc='best')
plt.show()

""" Example 3"""
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)
f1 = interp1d(x, y, kind='nearest')
f2 = interp1d(x, y, kind='previous')
f3 = interp1d(x, y, kind='next')
xnew = np.linspace(0, 10, num=1001, endpoint=True)
plt.plot(x, y, 'o')
plt.plot(xnew, f1(xnew), '-', xnew, f2(xnew), '--', xnew, f3(xnew), ':')
plt.legend(["data", "nearest", "previous", "next"], loc="best")
plt.show()


# 1-D interpolation example
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
# defining x and y arrays: y=3x^2-e^(0.1x)
x = np.linspace(0, 100, 10)
y = 3*x**2 - np.exp(0.1*x)
# x array that will used for interpolating new point values
x_new = np.linspace(0, 100, 100)
# kind specifies the type of function that will be used in the interpolating process
kind = ['linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic', 'previous', 'next']
fig = plt.figure()
ax = fig.subplots()
for i in kind:
    f = interpolate.interp1d(x, y, kind=i)
    # array that contains the interpolated data points
    y_interp = f(x_new)
    ax.plot(x_new, y_interp, alpha=0.5, label=i)
ax.scatter(x, y)
plt.legend()
plt.show()


# 2 D interpolation
# since we are dealing with two dimensionla data points we need to create a grid of points
# then assign a specific value to all the points on the grid which will be our initial known data points
# from which we interpolate the values of other data points
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
x = np.linspace(0, 4, 13)
y = np.linspace(0, 4, 13)
# defining grid from these two arrays
X, Y = np.meshgrid(x, y)
# assigning  a special value to all the couples(x,y) to complete our definition of our initial set of data points
# z = arccos(-cos(2X).cos(2Y))
z = np.arccos(-np.cos(2*X)*np.cos(2*Y))
# denser grid of points that we want to interpolate
x2 = np.linspace(0, 4, 65)
y2 = np.linspace(0, 4, 65)
X2, Y2 = np.meshgrid(x2, y2)
# assigning the interpolating function to the variable f
# there are only three kinds; linear, cubic, quantic which describe the type of spline used in the interpolation
f = interpolate.interp2d(x, y, z, kind='cubic')
Z2 = f(x2, y2)
# plotting both the 13 by 13(left) and 65 by 65 (right)
# the plots will display the grid of points and describe  each value of x and y with a color scale, to achieve this we
# can exploit the matplotlib function .pcolormesh() which allows creating a pseudocolor plot
# with a non-regular rectangular grid
fig = plt.figure()
ax = fig.subplots(1, 2)
ax[0].pcolormesh(X, Y, z)
ax[1].pcolormesh(X2, Y2, Z2)
plt.show()

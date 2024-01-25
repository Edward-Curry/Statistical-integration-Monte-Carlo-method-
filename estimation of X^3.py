# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:28:36 2021

@author: edwar
"""

import matplotlib.pyplot as plt
import numpy as np


times = 2000

x_cube = np.linspace(0,1,100)
y_cube = x_cube**4/4
plt.plot(x_cube,y_cube)

fig = plt.figure()
fig.set_size_inches(5, 5)
xs = np.linspace(0, 1, 100)
plt.plot(xs, xs ** 3)
rx = np.random.rand(times)
ry = np.random.rand(times)
plt.plot(rx, ry, 'o', markersize=1)#

c_inside = np.cumsum(ry < rx ** 3)
integral = float(np.sum(ry < rx ** 3)) / float(times)
print("the approximate integral between 0 and 1 of x^3 is",integral)
vs = c_inside / np.arange(1, times + 1, dtype=np.float)
plt.plot(vs)


def cummean(arr):
    return np.cumsum(arr)/np.arange(1,len(arr)+1,dtype=np.float)
def cumstd(arr):
    return np.sqrt(cummean(arr ** 2) - cummean(arr) ** 2)

plt.plot(cumstd(vs))
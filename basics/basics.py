#!/usr/bin/python
#  -*- coding:utf-8 -*-

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":

    print('reshape之后的数组共享内存')
    a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    b = a.reshape(4,3)
    print('a.shape =',a.shape),'\n'
    print('b.shape =',b.shape),'\n'
    #共享内存，a,b中的值都会改变
    a[2][1] = 100
    print(a,'\n')
    print(b,'\n')

    print('切片数据是原数组的一个视图,可直接修改')
    a1 = np.array([1,2,3,4,5,6,7,8,9,10])
    print(a1,'\n')
    a1[1:3] = 20, 30
    print(a1,'\n')

    print('布尔数组取值')
    a2 = np.array([1,2,3,4,5,6,7,8,9,10])
    b2 = a2[a2 > 6]
    #b2不受影响
    a2[a2 > 6]=6
    print(a2,'\n')
    print(b2,'\n')

    print('正态分布概率密度函数')
    mu = 0
    sigma = 1
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 50)
    y = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
    print(x.shape)
    print('x = \n', x)
    print(y.shape)
    print('y = \n', y)
    plt.plot(x, y, 'g-', x, y, 'go', linewidth=2, markersize=4)
    plt.grid(True)
    plt.show()

    x = np.arange(1, 0, -0.001)
    y = (-4 * x * np.log(x) + np.exp(-(40 * (x - 1 / np.e)) ** 4) / 25) / 2
    plt.figure(figsize=(6,8))
    plt.plot(y, x, 'r-', linewidth=2)
    plt.axis('off')
    plt.show()


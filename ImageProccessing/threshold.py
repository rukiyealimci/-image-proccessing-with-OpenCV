# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:25:25 2023

@author: rukiy
"""

import cv2 as cv
from matplotlib import pyplot as plt

image= cv.imread('image.jpg')
image=cv.cvtColor(image, cv.COLOR_BGR2GRAY) #gri seviyeye dönüştürmek için kullanılır

ret, thresh1=cv.threshold(image,127,255,cv.THRESH_BINARY)
ret, thresh2=cv.threshold(image,50,255,cv.THRESH_BINARY)
ret, thresh3=cv.threshold(image,127,127,cv.THRESH_BINARY)


ret, thresh4= cv.threshold(image, 127, 255,cv.THRESH_BINARY_INV)

ret, thresh5= cv.threshold(image, 250, 255,cv.THRESH_MASK) # hepsini kapartıyor
# ret, thresh6= cv.threshold(image, 127, 255,cv.THRESH_OTSU)
# ret, thresh7= cv.threshold(image, 127, 255,cv.THRESH_TOZERO)
# ret, thresh8= cv.threshold(image, 127, 255,cv.THRESH_TOZERO_INV)
# ret, thresh9= cv.threshold(image, 127, 255,cv.THRESH_TRIANGLE)
# ret, thresh10= cv.threshold(image, 127, 255,cv.THRESH_TRUNC)

plt.subplot(231),plt.imshow(image),plt.title('orijinal')
plt.subplot(232),plt.imshow(thresh1, 'gray'),plt.title('127,255,cv.THRESH_BINARY')
plt.subplot(233),plt.imshow(thresh2, 'gray'),plt.title('50,255,cv.THRESH_BINARY')
plt.subplot(234),plt.imshow(thresh3, 'gray'),plt.title('127,127,cv.THRESH_BINARY')
plt.subplot(235),plt.imshow(thresh4, 'gray'),plt.title('THRESH_BINARY_INV')
plt.subplot(236),plt.imshow(thresh5, 'gray'),plt.title('THRESH_MASK')


cv.destroyAllWindows()

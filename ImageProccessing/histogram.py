# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:25:25 2023

@author: rukiy
"""

import cv2 
from matplotlib import pyplot as plt

image= cv2.imread("image.jpg",0)
# Histogram değerinin hesaplanması
histogram = cv2.calcHist([image], [0], None, [256], [0,
256])


# Grafik olarak çizdirilmesi
plt.plot(histogram)
plt.show()

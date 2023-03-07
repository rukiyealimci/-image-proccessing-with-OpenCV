# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:25:25 2023

@author: rukiy
"""

import cv2 

image= cv2.imread('image.jpg')

# Erosion ve dilation işlemleri içn kernelin oluşturulması 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

# Resme açma işleminin uygulanması
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Resme kapama işleminin uygulanması
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

cv2.imshow("opened_image",opened_image)
cv2.imshow("closed_image",closed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

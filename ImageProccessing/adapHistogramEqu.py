# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:25:25 2023

@author: rukiy
"""

import cv2 as cv

# adaptive histogram eşitleme clip limit --> 2.0
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

image= cv.imread('image.jpg')

# Apply adaptive histogram equalization 
equalized_image = clahe.apply(image)

cv2.imshow("equalized_image",equalized_image)

cv.waitKey(0)
cv.destroyAllWindows()

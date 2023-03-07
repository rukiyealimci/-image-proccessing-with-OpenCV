# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:25:25 2023

@author: rukiy
"""

import cv2 

image= cv2.imread('image.jpg')


# Erosion ve dilation işlemleri içn kernelin oluşturulması
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

# Resme erosion işleminin uygulanması 
eroded_image = cv2.erode(image, kernel)
# Resme dilation işleminin uygulanması 
dilated_image = cv2.dilate(image, kernel)

cv2.imshow("eroded_image",eroded_image)
cv2.imshow("dilated_image",dilated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

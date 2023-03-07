# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:25:25 2023

@author: rukiy
"""

import cv2
# RGB formatındaki resmin Siyah beyaz formata çevirilmesi
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
# ya da
image_gray = cv2.imread("input.jpg", 0)
# ya da
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("image", image)
cv2.imshow("image_gray", image_gray)
cv2.imshow("gray", gray)
#her üç dönüşümün sonucunun aynı olduğu gözlemlenir.

cv2.waitKey(0)
cv2.destroyAllWindows()

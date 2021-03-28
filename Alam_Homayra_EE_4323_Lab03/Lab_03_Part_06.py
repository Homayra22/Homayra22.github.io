#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:17:09 2021

@author: homayra
"""

import numpy as np
import cv2
import histogram_plotter
import matplotlib.pyplot as plt
from skimage.util import random_noise

image2=cv2.imread("cell.jpeg",0)
image1=cv2.imread("building.jpeg",0)


noise_img=random_noise (image1,mode='gaussian',var=0.05**2)
noise_img=(255*noise_img).astype(np.uint8)


histogram_plotter.his_img(image1)
histogram_plotter.his_img(noise_img)


HP=np.array([[1,1,1],[1,1,1],[1,1,1]])/9

Y=histogram_plotter.Conv_Cor(image1,HP,0)
histogram_plotter.his_img(Y)

img_fil_cv2=cv2.fastNlMeansDenoising(noise_img,7,12,7,21)
histogram_plotter.his_img(img_fil_cv2)

cv2.imshow("Original Image",image1)
cv2.imshow("Noise_Image",noise_img)
cv2.imshow("Convolution",Y)
cv2.imshow("After removing Noise",img_fil_cv2)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
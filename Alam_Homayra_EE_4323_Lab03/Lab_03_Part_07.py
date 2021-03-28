#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:00:37 2021

@author: homayra
"""
import numpy as np
import cv2
import histogram_plotter
import matplotlib.pyplot as plt
from skimage.util import random_noise


image1=cv2.imread("building.jpeg",0)

histogram_plotter.his_img(image1)

lp=np.array([[2,2,2],[2,2,2],[2,2,2],[2,2,2]])
hp=np.array([[0,-3,0],[-2,4,-2],[0,-3,0]])
hph=np.array([[-2,-2,-2],[3,3,3],[-2,-2,-2]])
hpv=np.array([[-1,3,-1],[-1,3,-1],[-1,3,-1],[-1,3,-1]])

img_LP=cv2.filter2D(image1,-1,lp)
img_HP=cv2.filter2D(image1,-1,hp)
img_HPH=cv2.filter2D(image1,-1,hph)
img_HPV=cv2.filter2D(image1,-1,hpv)


cv2.imshow("Original Image",image1)
cv2.imshow("LP",img_LP)
cv2.imshow("HP",img_HP)
cv2.imshow("HPH",img_HPH)
cv2.imshow("HPV",img_HPV)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:03:54 2021

@author: homayra
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2



def Conv_Cor(A,kernel,sel):
    n,m=A.shape
    if sel==1:
        kernel=np.flip(kernel)
    A_C=np.zeros([n+2,m+2])
    A_C[1:-1,1:-1]=A
    Y_new=np.zeros_like(A)
    
    for i in range (m):
        for j in range(n):
            Y_new[j,i]=np.sum(kernel*A_C[j:j+3,i:i+3])
    return Y_new

        
    

def his_img(A):
    n=int (np.ceil(np.log2(max(A.flatten()))))
    N=2**n-1
    hist,bins=np.histogram(A.flatten(),N+1,[0,N])
    cdf=hist.cumsum()
    cdf_normalized=cdf/cdf.max()
    
    fig,ax1=plt.subplots()
    
    ax1.hist(A.flatten(),N+1,[0,N+1],color='r')
    ax1.set_xlabel('Pixel Value')
    ax1.set_ylabel('Number of Pixel')
    
    
    ax2=ax1.twinx()
    ax2.plot(cdf_normalized,color='b')
    ax2.set_ylabel('CDF')
    
    
    plt.ylim([0,1.03])
    plt.xlim([0,N+1])
    fig.tight_layout()
    plt.legend(('cdf','histogram'),loc='upper left')
    plt.show()
    
    
if __name__=='__main__':
    A=np.zeros([200,200],'uint8')
    A[:,0:A.shape[0]//2]=10
    A[:,0:A.shape[0]//4]=0
    plt.figure('test1')
    plt.imshow(A,cmap='gray')
    his_img(A)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:34:11 2018

@author: apple
"""

# homework 0-1
# import image library

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#raw_fig = Image.open('westbrook.jpg')

raw_fig = mpimg.imread('westbrook.jpg')

plt.imshow(raw_fig)
plt.axis('off')
plt.show()
plt.close()

img_array = raw_fig * 0.5

img_array = img_array.astype(np.uint8)

plt.imshow(img_array)
plt.axis('off')
plt.show()
plt.close()


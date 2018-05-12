# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:37:15 2018

@author: AONE
"""

from PIL import Image
from PIL import ImageFilter
im = Image.open('C:\\Users\\AONE\\117060400101\\Dong.jpg')
om = im.filter(ImageFilter.CONTOUR)
om.save('DongContour.jpg')
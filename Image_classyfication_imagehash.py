# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

p = 'C:/Users/user/Downloads/obrazy2/'

import os
afiles1 = os.listdir(p)
afiles = afiles1[0:10]
from PIL import Image
import imagehash

import pandas as pd
aa = pd.DataFrame(columns=['im1' ,'im2' ,'sim'])

inum = 0
for i in afiles:
    inum += 1
    hash0 = imagehash.average_hash(Image.open(p+i)) 
    for k in afiles[inum:]:
        hash1 = imagehash.average_hash(Image.open(p+k)) 
        aa.append([i,k,hash0-hash1])
        print([i, k,hash0-hash1])
    
    
#im = Image.open(p+'3742508.jpg')
#im.show(p+'3742508.jpg')


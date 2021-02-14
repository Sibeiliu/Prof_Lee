# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:26:41 2021

@author: Sibei
"""
## push python into github
# 1) git init
# 2) git add . or git add ['filename']
# 3) git commit -m "My first File"
# 6) git push origin master


import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="1" 



import keras
from matplotlib import pyplot as plt
import numpy as np
import gzip
%matplotlib inline
from keras.layers import Input,Conv2D,MaxPooling2D,UpSampling2D
from keras.models import Model
from keras.optimizers import RMSprop

# import nii data

from nibabel.testing import data_path


























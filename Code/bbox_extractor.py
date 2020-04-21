
# coding: utf-8

# In[23]:


import cv2
import numpy as np
import os
import sys


# In[50]:


for i in sorted(os.listdir('./test_images/')):
    if '.jpg' in i:
        print('Finding faces in image',i)
        os.system("python yoloface/yoloface.py --image test_images/"+i+" --output-dir output_bbox/")
print('All bounding boxes extracted successfully')

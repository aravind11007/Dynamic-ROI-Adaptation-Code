#!/usr/bin/env python
# coding: utf-8

# In[14]:


import os
import torch
from torch.utils.data import Dataset
import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[11]:


class baby_loader(Dataset):
    def __init__(self,path):
        self.path=path
        self.files=self.all_files(path)
        
    @staticmethod
    def all_files(path):
        files=[]
        img_path=os.path.join(path,'img')
        mask_path=os.path.join(path,'mask')
        for dir in os.listdir(img_path):
            full_img=os.path.join(img_path,dir)
            full_mask=os.path.join(mask_path,dir)
            files.append((full_img,full_mask))
        return files
    
    def __len__(self):
        return len(self.files)
    
    def __getitem__(self,index):
        img=cv2.imread(self.files[index][0])
        mask=cv2.imread(self.files[index][1])
        
        img=np.transpose(img,(2,0,1))
        img=img/255
        img=torch.tensor(img).float()
        
        mask=mask[:,:,0]
        mask=torch.tensor(mask,dtype=torch.int32).unsqueeze(0)
        mask=mask.long()

        
        return img,mask


# In[ ]:





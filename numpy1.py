#!/usr/bin/env python
# coding: utf-8

# In[154]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


# # list array

# In[155]:


np.array([10,20,30])


# 
# # 1 D array

# In[156]:


array1=np.array([10,'a','m',10.7])


# In[157]:


array1.ndim


# # 2D Array

# In[158]:


array2=np.array([[10,20.2,30],[10,20,30]])


# In[159]:


pd.DataFrame(array2)


# In[ ]:


np.array([[1,6,8,9],[3,7,9,6]])


# In[ ]:


array2.ndim


# In[ ]:


array2.shape


# In[ ]:


array1.shape


# In[ ]:


array2.size


# In[ ]:


array1.size


# In[ ]:


array1.dtype


# In[ ]:


array2.dtype


# In[ ]:


array1.itemsize


# In[ ]:


array2.itemsize


# # zeros array

# In[ ]:


np.zeros((3,4))


# In[ ]:


np.zeros((3,3))


# In[ ]:


np.ones((3,3))


# # range

# In[ ]:


np.arange(6)


# In[ ]:


np.arange(-2,24,2)


# In[ ]:


df=pd.DataFrame(np.arange(6))


# In[ ]:


plt.plot(df)


# # Indexing and Slicing

# In[160]:


arr=np.array([10,20,3,30,9])


# In[161]:


arr[0]


# In[162]:


arr[2]


# In[163]:


arr2=np.arange(12,48,2)


# In[164]:


arr2[3]


# In[165]:


arr3=np.array([[20,30,40],[29,36,39]])


# In[166]:


pd.DataFrame(arr3)


# In[167]:


arr3[1]


# In[168]:


print(arr+arr)


# In[169]:


arr3[0,2]


# # slicing 1D array

# In[170]:


arr4=np.array=([10,3])


# In[171]:


arr4


# In[ ]:





# In[172]:


arr5=np.array=([10,20,33,44,66,69,97])


# In[173]:


arr5


# In[174]:


arr5[1:5]


# In[175]:


arr5[4:7]


# In[176]:


arr5[:4]


# In[177]:


arr5[0:6:2]


# In[178]:


arr5[::2]


# # Slicing 2D array

# In[181]:


arr6=np.array([[20,30,40,50,60],[39,49,98,65,44]])


# In[182]:


arr6


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





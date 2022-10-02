#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import packages
from utils.func_loader import *


# In[2]:


# main call
file_format = 'txt'
# dir_path = input('Enter directory path: ')
dir_path =  'dir'
no_of_files = [0]
no_of_lines = [0]

try:
    folder_explorer(path=dir_path, nfiles=no_of_files, nlines=no_of_lines, fformat=file_format)

    print("=====================")
    print('\nNumber of files found:  {}'.format(no_of_files[0]))
    print('Total number of lines:  {}'.format(no_of_lines[0]))
    print('Average lines per file: {}'.format(round(no_of_lines[0]/no_of_files[0], 2)))
except:
    print('Error: Unknown error Occured...')


# #### 

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 21:45:02 2018

@author: w-2579
"""

import os

# 将当前文件夹下所有文件名（路径）放进一个txt
path = "/home/raymond/project/AIIA/train-public/raw_images"
#path = "E:\Code\Python\XML_read"
files = os.listdir(path)

new_path = "/home/raymond/project/AIIA_YOLOv3_PyTorch/common/AIIA_train_image.txt"
f = open(new_path,'w')
for i in files:
    if os.path.splitext(i)[1] == ".jpg":  # 选择记录什么类型的文件的名字
        if i == 'AIIA_train_label.jpg':
            continue
        else:
            f.writelines(path + '/'+ i + '\n')
f.close()
#new_path = path + "\label_trans\AIIA_train_label.txt"
#new_path = path + "AIIA_train_label.txt"
#f = open(new_path,'w')
#f.writelines(os.listdir(new_path))
#f.close()
            
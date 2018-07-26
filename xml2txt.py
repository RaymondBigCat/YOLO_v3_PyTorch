# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 19:18:13 2018

@author: w-2579
"""

from xml_process import xml_process
import numpy as np
import os

#path = 'airport00012.xml'
#xml1 = xml_process(path)

# AIIA数据集的路径
path = "/home/raymond/project/AIIA/train-public/annotations"
files = os.listdir(path)

label_dic = {}
for i in files:
    if os.path.splitext(i)[1] == ".xml":  # 找出当前文件夹下所有的.xml文件
        label_path = path + '/' + i
        label_temp = xml_process(label_path).get_rectpoint()
        # 存放在其下的label_trans文件夹里
        label_path = path + "/label_trans/" + i
        txt_path = label_path.replace('.xml', '.txt')

        txt_file = open(txt_path,'w')
        for k in range(label_temp.shape[0]):
            for j in range(5):
                txt_file.write(str(label_temp[k][j]) + ' ')
            txt_file.write('\n')
        txt_file.close()


#label_file = open('train_lable.txt', 'w')
#for i in range(5):
#    label_file.write(str(txt_temp[0][0][i]))
#    label_file.write(' ')
#label_file.close()        

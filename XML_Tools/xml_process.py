
# coding: utf-8

# A class that used to analyse a XML file, which contains label data for training.


import xml.etree.ElementTree as ET
import numpy as np

class xml_process():
    def __init__(self, xml_path):
        self.path = xml_path
        
    def get_rectpoint(self):
        kind = {'airport':1, 'bridge':2, 'harbor':3}
        tree = ET.parse(self.path)
        root = tree.getroot()
        self.aims = root.findall('object')
        labels = np.zeros((len(self.aims),5), dtype = np.int32)
        for i in range(len(self.aims)):
            aim_name = self.aims[i].find('name').text
            labels[i][0] = kind[aim_name]
            aim_bndbox = self.aims[i].find('bndbox')
            labels[i][1] = str(aim_bndbox.find('xmin').text)
            labels[i][2] = str(aim_bndbox.find('ymin').text)
            labels[i][3] = str(aim_bndbox.find('xmax').text)
            labels[i][4] = str(aim_bndbox.find('ymax').text)
        self.labels = labels
        return self.labels


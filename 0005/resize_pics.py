# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 17:34:09 2017

@author: Rain Wei
"""

import os
from PIL import Image

def resize_pictures(path):
    """resize all the pictures in path"""
    os.chdir(path)
    file_in_current_dir = os.listdir()
    for i in file_in_current_dir:
        with Image.open(i) as im:
            w, h = im.size
            # 按比例偏大的边来计算整体需要缩小的比例
            n = w / 1136 if (w / 1136) >= (h / 640) else h / 640
            im.thumbnail((w / n, h / n))
            im.save(i.split('.')[0] + '.jpg', 'jpeg')

if __name__ == '__main__':
    resize_pictures('d:\\learn\\python\\pics')







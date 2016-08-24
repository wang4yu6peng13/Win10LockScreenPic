#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import shutil

# 锁屏画报路径，将xxx 替换为自己的user名称,new_path 根据自己的需要进行更改
PATH = r"C:\Users\Yupeng Wang" \
       r"\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\\"
NEW_PATH = r'E:\testPic\\'


def rename_and_save_pic(file_path, new_path):
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    if os.path.exists(new_path):
        i = len(os.listdir(path=new_path))
        for file in os.listdir(path=file_path):
            i += 1
            shutil.copy(file_path + file, new_path + 'picture_ %d' % i + '.jpg')


if __name__ == '__main__':
    rename_and_save_pic(PATH, NEW_PATH)

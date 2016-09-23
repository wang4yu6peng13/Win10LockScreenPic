#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import shutil
import argparse
from PIL import Image

# 锁屏画报路径，将xxx 替换为自己的user名称,new_path 根据自己的需要进行更改
# PATH = r"C:\Users\Yupeng Wang" \
#       r"\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\\"
# NEW_PATH = r'E:\testPic\\'
PATH = os.environ[
           'LOCALAPPDATA'] + "\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"


def rename_and_save_pic(file_path, new_path):
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    if os.path.exists(new_path):
        i = len(os.listdir(path=new_path))
        for file in os.listdir(path=file_path):
            # print(file,imghdr.what(file_path+file))
            # i += 1
            # shutil.copy(file_path + file, new_path + 'picture_%d' % i + '.jpg')
            # shutil.copy(file_path + file, new_path + file + '.' + str(imghdr.what(file_path + file)))
            try:
                im = Image.open(file_path + file)
                width, height = im.size
                if (width == 1080 and height == 1920) or (width == 1920 and height == 1080):
                    i += 1
                    rename = new_path + 'picture_%d' % i + '.jpg'
                    shutil.copy(file_path + file, rename)
                    print('\t', file, "=>", rename, width, height)
            except OSError as e:
                print('\t', file, "is not a picture!\nMSG:", e)


def main():
    parser = argparse.ArgumentParser(description='Get Win10 LockScreen Pictures')  # 命令行参数解析对象
    # parser.add_argument('-u', dest='username', help='Your account name on Windows 10(use "")')
    parser.add_argument('-t', dest='target', help=r'The target path which you want to copy to(end with "\")')

    args = parser.parse_args()  # 解析命令行参数
    # username = args.username
    target = args.target

    if target:
        # PATH = "C:\\Users\\%s\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\" % username
        NEW_PATH = target if target.endswith('\\') else target + '\\'
        rename_and_save_pic(PATH, NEW_PATH)
    else:
        print(parser.parse_args(['-h']))
        exit(0)


if __name__ == '__main__':
    # rename_and_save_pic(PATH, NEW_PATH)
    # rename_and_save_pic(os.environ['LOCALAPPDATA']+"\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\", "E:\\0test\\")
    # print(os.environ['LOCALAPPDATA'])
    # print(u"%LOCALAPPDATA%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets")
    # print(PATH)
    main()
# python3 Win10LockScreenPic.py -t E:\\0test

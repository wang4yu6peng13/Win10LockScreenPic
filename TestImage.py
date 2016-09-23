#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PIL import Image

try:
    # im = Image.open("Win10LockScreenPic.py")
    im = Image.open("png")
    # im = Image.open("gif")
    w, h = im.size
    print(w, h)
except OSError as e:
    print("It is not a pic! ====", e)

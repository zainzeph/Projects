#!/usr/bin/python
from PIL import Image
import os, sys

path = "C:\ProjectsFolder\RocketOpenCv\opencv\build\x64\vc15\bin\Rocket\PiData3\"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()

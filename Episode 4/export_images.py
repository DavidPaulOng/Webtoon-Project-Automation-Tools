import os
import zipfile
import cv2
import numpy as np
import ctypes

'''
Export saved images from all Krita files in the directory.

Place this script in the same directory as your .kra files and run it.
The exported images will be saved as .png files with the same name as the .kra files
in the same directory.
'''

krita_files = [d for d in os.listdir(".") if d.endswith('.kra')]
for file in krita_files:
    with zipfile.ZipFile(file, 'r') as f:
        img = f.read("mergedimage.png") 
    cv2.imwrite(file.replace("kra", "png"), cv2.imdecode(
        np.frombuffer(img, np.uint8), cv2.IMREAD_UNCHANGED))

ctypes.windll.shell32.SHChangeNotify(0x8000000, 0x1000, None, None)

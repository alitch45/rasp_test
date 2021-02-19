import cv2
import numpy as np
import glob
import subprocess
import time
import datetime
import shutil
from PIL import Image
face_cascade = cv2.CascadeClassifier('/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
files =glob.glob("/home/pi/test3/img/person/*")


for fname in files: 
    bgr = cv2.imread(fname, cv2.IMREAD_COLOR)
    src = bgr
    n = 0
    def mosaic(src, ratio=0.1):
     small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
     return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
    def mosaic_area(src, x, y, width, height, ratio=0.1):
     dst = src.copy()
     dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
     return dst
    dst_01 = mosaic(src)
    cv2.imwrite('./img/mozaic/{}_{}.{}'.format((datetime.datetime.fromtimestamp(time.time())),n,'.jpg'), dst_01)
    shutil.move(fname, './img/Backup/')
cv2.destroyAllWindows()

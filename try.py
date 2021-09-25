import cv2
from PIL import Image

from INPR import detect_plates
import matplotlib.pyplot as plt

im = 'test_img/kia.jpg'

grap,op,img = detect_plates(im)
plt.imshow(grap)
plt.savefig('grap3.png')
plt.show()
#plt.show() 
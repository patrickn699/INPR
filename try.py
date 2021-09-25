import cv2
from PIL import Image

from INPR import detect_plates,fetch_details
import matplotlib.pyplot as plt

im = 'test_img/kia.jpg'

grap,op,img = detect_plates(im)
#plt.imshow(grap)
#plt.savefig('grap3.png')
#print(op)
#print(img)
#plt.show() 

num_plate_text = fetch_details(op,img)
print(num_plate_text)
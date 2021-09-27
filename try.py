import cv2
from PIL import Image

from INPR import detect_plates,fetch_details
import matplotlib.pyplot as plt
import urllib.request
import os

im = 'test_img/kia.jpg'

grap,op,img = detect_plates(im)
#plt.imshow(grap)
#plt.savefig('grap3.png')
#print(op)
#print(img)
#plt.show() 

num_plate_text = fetch_details(op,img)
print(num_plate_text)

'''
if not os.path.isfile('model_final_pth'):
    url = "https://github.com/patrickn699/INPR/blob/main/model_final.pth"
    print ("download start!")
    filename, headers = urllib.request.urlretrieve(url, filename="model_final11.pth")
    print ("download complete!")
    print ("download file location: ", filename)
    print ("download headers: ", headers)
'''
import cv2
from PIL import Image
from INPR.inpr import detect_plates,fetch_details
#from INPR import detect_plates, fetch_details
import matplotlib.pyplot as plt
import urllib.request
import os
import zipfile as z
import requests
import gdown
from INPR import inpr


im = 'test_img/h20.jpg'

grap,op,img = detect_plates(im)
#plt.imshow(grap)
#plt.savefig('grap3.png')
#print(op)
#print(img)
#plt.show() 

num_plate_text = fetch_details(op,img,show_plates=True)
print(num_plate_text)

'''
if not os.path.isfile('model_final.pth'):
            url = "https://github.com/patrickn699/INPR/releases/download/inpr_v1.0/model_final.pth"
            #url1 = "https://github.com/patrickn699/INPR/blob/main/config.yaml"
            print ("downloading the model stay put...!")
            filename, headers = urllib.request.urlretrieve(url, filename="model_final.pth")
            #fi, he = urllib.request.urlretrieve(url, filename="config.yaml")
            print ("download complete!")
            print ("download file location: ", filename)
            print ("download headers: ", headers)
'''








'''


url = 'https://drive.google.com/file/d/1nX7AXkh7hfhgIrrExCRlVOs5pym_U25r/view?usp=sharing'
output = 'model_final.pth'
gdown.download(url, output, quiet=False)
'''

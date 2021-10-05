import os
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from .utils import Load_model
from .get_num_plate import get_number_plate
from .get_details import fetch
import pandas as pd
import urllib.request
#os.environ['KMP_DUPLICATE_LIB_OK']='True'

l = Load_model()
g = get_number_plate()
l.check_model()
cfg = l.load_model()
#det = details()
'''
def get_driver():
    url = "https://github.com/patrickn699/Indian-Number-Plate-Extraction/tree/master/chromedriver_win322/chromedriver.exe"
    print ("download start!")
    filename, headers = urllib.request.urlretrieve(url, filename="downloads/chromedriver.exe")
    print ("download complete!")
    print ("download file location: ", filename)
    print ("download headers: ", headers)
'''

#in_img = cv2.imread('test_img/bm.jpg')
im = 'test_img/bm.jpg'

def detect_plates(imgg):
    
    op, img = l.predict(imgg, cfg)
    grap = l.visulize(img, cfg, op)
    return grap,op,img

def fetch_details(op,img, show_plates=False):
    plts = g.run_easy_ocr(op, img,show_plates)
    #print(plts)
    for i in plts:

        if len(i) == 10 or len(i) == 9:
            print('Trying to fetch the details please wait...')
            #data = fetch(i)
            #return pd.DataFrame(data)
            return i

        else:
            return 'Oops....unable to fetch!'

'''
if __name__ == '__main__':
    grap,op,img = detect_plates(im)
    plt.imshow(grap)
    plt.show()
    df = fetch_details(op,img)
    print(df)
    print(op)
'''

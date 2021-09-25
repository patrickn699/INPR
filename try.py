from INPR import detect_plates
import matplotlib.pyplot as plt

im = 'test_img/bm.jpg'


grap,op,img = detect_plates(im)
plt.imshow(grap)
plt.show() 
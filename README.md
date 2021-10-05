
# Indian Number Plate Recognition

An open source Indian Number Plate Recogniton library built using deep learning.

For GUI version please go to this [repo](https://github.com/patrickn699/Indian-Number-Plate-Extraction).

![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)

![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)









## Version and updates

* v1.0.0: Initial release
    * Detect number plates and extract the texts from it.

* Docker image comming soon!





## Screenshots

![App Screenshot 1](https://github.com/patrickn699/INPR/blob/main/test_img/p1.png?raw=true)

![App Screenshot 1](https://github.com/patrickn699/INPR/blob/main/test_img/p2.png?raw=true)

![App Screenshot 1](https://github.com/patrickn699/INPR/blob/main/test_img/p3.png?raw=true)

![App Screenshot 1](https://github.com/patrickn699/INPR/blob/main/test_img/p4.png?raw=true)


## Installation

This library can be installed on windows and linux just follow the below steps based on your OS.

### for windows

1. I would suggest before installing please create an anaconda environment.

```python
conda create -n "env-name" python==3.7

```

2. Install torch and detectron2

```python
pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

python -m pip install git+https://github.com/facebookresearch/detectron2.git

```

3. Then install INPR package

```python
pip install INPR

```

### for linux

1. install torch and detectron2

```python
pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.7/index.html
```

2. Then simply install the INPR package

```python
pip install INPR

```



## Usage

To detect the plates here is an example

```python
    from INPR.inpr import detect_plates
    import matplotlib.pyplot as plt

    im = 'test_img/kia.jpg'
    grap,op,img = detect_plates(im)
    plt.imshow(grap)

```

In the above example the method "detect_plates" returns three
values which are:-

    1. the image along with detected plates
    2. the bounding boxes of the detected plates
    3. the passed image iteself

Optionally you can also try to extract the text present inside the detected plates by the following example:

```python

    from INPR.inpr import fetch_details, detect_plates

    im = 'test_img/kia.jpg'

    grap,op,img = detect_plates(im)
    num_plate_text = fetch_details(op,img)
    
    print(num_plate_text)   

```






## Feedback and queries

If you have any feedback, bugs, queries please reach out to me on [Linkedin](https://www.linkedin.com/in/prathmesh-patil-b151051a3) and also raise an GitHub issue about the same.

  
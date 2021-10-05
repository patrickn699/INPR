from setuptools import setup
import setuptools

with open("requirements.txt",'r') as f:
    requirements = f.read().splitlines()

with open("README.md",'r') as f:
    long_description = f.read()


setup(
    name='INPR',
    include_package_data=True,
    version='1.0.0',
    description='A deep learning based project to detect indian number plates',
    author='Prathmesh Patil',
    author_email='prathmesh.patil8899@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages= ['INPR'],
    keywords=['Deep Learning','Computer Vision','Pytorch','Detectron2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url = 'https://github.com/patrickn699/INPR',
    download_url= 'https://github.com/patrickn699/INPR.git',
    python_requires='>=3.6',
    py_modules=['INPR'],
    install_requires=requirements
    
)

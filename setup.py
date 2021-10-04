from setuptools import setup
import setuptools

with open("requirements.txt",'r') as f:
    requirements = f.read().splitlines()

with open("README.md",'r') as f:
    long_description = f.read()


setup(
    name='inpr',
    include_package_data=True,
    version='0.1',
    description='A deep learning based project to detect indian number plates',
    author='Prathmesh Patil',
    author_email='prathmesh.patil8899@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages= ['inpr'],
    keywords=['Deep Learning','Computer Vision','Pytorch','Detectron2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['INPR'],
    install_requires=requirements
    
)

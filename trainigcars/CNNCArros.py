from __future__ import print_function
import keras

from keras.datasets import mnist
from keras.models import sequential
from keras.layers import Dense,Dropout,Flatten
from keras.layers import Conv2D,MaxPooling2D


print(mnist.load_data())
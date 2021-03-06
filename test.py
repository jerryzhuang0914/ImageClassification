# -*- coding: utf-8 -*-
"""test.ipynb

Automatically generated by Colaboratory.

"""

from google.colab import drive
drive.mount('/content/drive/')

import tensorflow as tf
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator

# Please modify these file path before running test.py
# testdata file path

testdata_dir = '/content/drive/My Drive/app/testdata/'
# mode file path
file_path = '/content/drive/My Drive/app/model/model.h5'


def load_data():
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    test = test_datagen.flow_from_directory(testdata_dir, target_size=(300, 300), batch_size=1)
    return test


def evaluate_model(test):
    model = load_model(file_path)
    print("Loss and Accuracy of model:")
    loss, accuracy = model.evaluate(test)
    return loss, accuracy


if __name__ == '__main__':
    test = load_data()
    loss, accuracy = evaluate_model(test)
    print("loss={:.4f}, accuracy={:.4f}".format(loss, accuracy))
